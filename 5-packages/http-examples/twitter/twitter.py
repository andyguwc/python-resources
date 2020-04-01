# https://github.com/bear/python-twitter

import requests 

class Api(object):
    def __init__(self,
                 consumer_key=None,
                 access_token_key=None,
                 access_token_secret=None,
                 application_only_auth=False,
                 input_encoding=None,
                 request_headers=None,
                 timetout=None,
                 proxies=None
                 ):
        # method for auth 
        self._auth = None 
        # functions to intialize things
        self._initialize_request_headers(request_headers)
        self._initialize_user_agent()
        self._initialize_default_parameters()
        # ression used
        self._session = requests.Session()
        
    # request url based on verb, etc.
    def _request_url(self, url, verb, data=None, json=None, enforce_auth=True):
        """Request a url.
        Args:
            url:
                The web location we want to retrieve.
            verb:
                Either POST or GET.
            data:
                A dict of (str, unicode) key/value pairs.
        Returns:
            A JSON object.
        """
        if enforce_auth:
            if not self.__auth:
                raise TwitterError("The twitter.Api instance must be authenticated.")

            if url and self.sleep_on_rate_limit:
                limit = self.CheckRateLimit(url)

                if limit.remaining == 0:
                    try:
                        stime = max(int(limit.reset - time.time()) + 10, 0)
                        logger.debug('Rate limited requesting [%s], sleeping for [%s]', url, stime)
                        time.sleep(stime)
                    except ValueError:
                        pass

        if not data:
            data = {}

        # post media data (files), data, or json 
        if verb == 'POST':
            if data:
                if 'media_ids' in data:
                    url = self._BuildUrl(url, extra_params={'media_ids': data['media_ids']})
                    resp = self._session.post(url, data=data, auth=self.__auth, timeout=self._timeout, proxies=self.proxies)
                elif 'media' in data:
                    resp = self._session.post(url, files=data, auth=self.__auth, timeout=self._timeout, proxies=self.proxies)
                else:
                    resp = self._session.post(url, data=data, auth=self.__auth, timeout=self._timeout, proxies=self.proxies)
            elif json:
                resp = self._session.post(url, json=json, auth=self.__auth, timeout=self._timeout, proxies=self.proxies)
            else:
                resp = 0  # POST request, but without data or json

        elif verb == 'GET':
            data['tweet_mode'] = self.tweet_mode
            url = self._BuildUrl(url, extra_params=data)
            resp = self._session.get(url, auth=self.__auth, timeout=self._timeout, proxies=self.proxies)

        else:
            resp = 0  # if not a POST or GET request

        if url and self.rate_limit and resp:
            limit = resp.headers.get('x-rate-limit-limit', 0)
            remaining = resp.headers.get('x-rate-limit-remaining', 0)
            reset = resp.headers.get('x-rate-limit-reset', 0)

            self.rate_limit.set_limit(url, limit, remaining, reset)

        return resp

    # process the response data 
    def _ParseAndCheckTwitter(self, json_data):
        """Try and parse the JSON returned from Twitter and return
        an empty dictionary if there is any error.
        This is a purely defensive check because during some Twitter
        network outages it will return an HTML failwhale page.
        """
        try:
            data = json.loads(json_data)
        except ValueError:
            if "<title>Twitter / Over capacity</title>" in json_data:
                raise TwitterError({'message': "Capacity Error"})
            if "<title>Twitter / Error</title>" in json_data:
                raise TwitterError({'message': "Technical Error"})
            if "Exceeded connection limit for user" in json_data:
                raise TwitterError({'message': "Exceeded connection limit for user"})
            if "Error 401 Unauthorized" in json_data:
                raise TwitterError({'message': "Unauthorized"})
            raise TwitterError({'Unknown error': '{0}'.format(json_data)})
        self._CheckForTwitterError(data)
        return data

    @staticmethod
    def _CheckForTwitterError(data):
        """Raises a TwitterError if twitter returns an error message.
        Args:
            data (dict):
                A python dict created from the Twitter json response
        Raises:
            (twitter.TwitterError): TwitterError wrapping the twitter error
            message if one exists.
        """
        # Twitter errors are relatively unlikely, so it is faster
        # to check first, rather than try and catch the exception
        if 'error' in data:
            raise TwitterError(data['error'])
        if 'errors' in data:
            raise TwitterError(data['errors'])

    def GetUsersSearch(self,
                       term=None,
                       page=1,
                       count=20,
                       include_entities=None):
        """Return twitter user search results for a given term.
        Args:
          term:
            Term to search by.
          page:
            Page of results to return. Default is 1
            [Optional]
          count:
            Number of results to return.  Default is 20
            [Optional]
          include_entities:
            If True, each tweet will include a node called "entities,".
            This node offers a variety of metadata about the tweet in a
            discrete structure, including: user_mentions, urls, and hashtags.
            [Optional]
        Returns:
          A sequence of twitter.User instances, one for each message containing
          the term
        """
        # Build request parameters
        parameters = {}

        if term is not None:
            parameters['q'] = term

        if page != 1:
            parameters['page'] = page

        if include_entities:
            parameters['include_entities'] = 1

        try:
            parameters['count'] = int(count)
        except ValueError:
            raise TwitterError({'message': "count must be an integer"})

        # Make and send requests
        url = '%s/users/search.json' % self.base_url
        resp = self._RequestUrl(url, 'GET', data=parameters)
        data = self._ParseAndCheckTwitter(resp.content.decode('utf-8'))
        return [User.NewFromJsonDict(x) for x in data]

