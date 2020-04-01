# https://github.com/bear/python-twitter/blob/master/twitter/models.py

class TwitterModel(object):
    """Base class from which all twitter models will inherit
    """

    def __init__(self, **kwargs):
        self.param_defaults = {}
    
    def __str__(self):
        return self.as_json_str()
    
    def __eq__(self, other):
        return other and self._asdict() == other._asdict()
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        if hasattr(self, 'id'):
            return hash(self.id) 
        else:
            raise TypeError('unhashable type: {} (no id attribute)'
                            .format(type(self)))

    def as_json_str(self, ensure_ascii=True):
        return json.dumps(self.asdict(), ensure_ascii=ensure_ascii, sort_keys=True)

    def asdict(self):
        data = {}
        for (key, value) in self.param_defaults.items():
            # If the value is a list, we need to create a list to hold the
            # dicts created by an object supporting the AsDict() method,
            # i.e., if it inherits from TwitterModel. If the item in the list
            # doesn't support the AsDict() method, then we assign the value
            # directly. An example being a list of Media objects contained
            # within a Status object.
            if isinstance(getattr(self, key, None), (list, tuple, set)):
                data[key] = list()
                for subobj in getattr(self, key, None):
                    if getattr(subobj, 'asdict', None):
                        data[key].append(subobj.asdict())
                    else:
                        data[key].append(subobj)
            
            # not a list, but still a subclass and we can assign directly asdict
            elif getattr(getattr(self, key, None), 'asdict', None):
                data[key] = getattr(self, key).asdict()
            
            elif getattr(self, key, None):
                data[key] = getattr(self, key, None)
        return data  


class Media(TwitterModel):
    """A class representing Media component of a tweet"""

    def __init__(self, **kwargs):
        self.param_defaults = {
            'display_url': None,
            'expanded_url': None,
            'ext_alt_text': None,
            'id': None,
            'media_url': None,
            'media_url_https': None,
            'sizes': None,
            'type': None,
            'url': None,
            'video_info': None,
        }

        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))
    
    def __repr__(self):
        return "Media(ID={media_id}, Type={media_type}, DisplayURL='{url}'".format(
            media_id=self.id,
            media_type=self.type, 
            url=self.display_url)


class Trend(TwitterModel):

    """ A class representing a trending topic. """

    def __init__(self, **kwargs):
        self.param_defaults = {
            'events': None,
            'name': None,
            'promoted_content': None,
            'query': None,
            'timestamp': None,
            'url': None,
            'tweet_volume': None,
        }

        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return "Trend(Name={0!r}, Time={1}, URL={2})".format(
            self.name,
            self.timestamp,
            self.url)

    @property
    def volume(self):
        return self.tweet_volume
