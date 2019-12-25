##################################################
#  AWS Hooks 
##################################################
# https://github.com/apache/airflow/blob/master/airflow/contrib/hooks/aws_hook.py

'''
base AWS hook
'''
def _parse_s3_config(config_file_name, config_format='boto', profile=None):
    """
    parses a config file for s3 credentials 
    """
    pass  
    # basically lots of config parser to return access_key, secret_key

class AwsHook(BaseHook):
    """
    Interact with AWS. Wrapper around the boto3 library
    """
    def __init__(self, aws_conn_id='aws_default', verify=None):
        self.aws_conn_id = aws_conn_id
        self.verify = verify
    
    def _get_credentials(self, region_name):
        # return a boto3 session iwth access key and region name
        # input is from the info from the connection 
        aws_access_key_id = None 
        aws_secret_access_key = None 
        aws_session_token = None 
        endpoint_url = None 

        if self.aws_conn_id:
            try: 
                connection_object = self.get_connection(self.aws_conn_id)
                # this get_connection method is from the BaseHook, returning a conn object
                extra_config = connection_object.extra_dejson
                if connection_object.login:
                    aws_access_key_id = connection_object.login
                    aws_secret_access_key = connection_object.password

                # code below gets AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and optional AWS_SESSION_TOKEN which are needed for creating boto3 sesssion
                # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#method-parameters
                elif 'aws_secret_access_key' in extra_config:
                    aws_access_key_id = extra_config['aws_access_key_id']
                    aws_secret_access_key = extra_config['aws_secret_access_key']

                elif 's3_config_file' in extra_config:
                    aws_access_key_id, aws_secret_access_key = \
                        _parse_s3_config(
                            extra_config['s3_config_file'],
                            extra_config.get('s3_config_format')
                            extra_config.get('profile'))
                
                if region_name is None:
                    region_name = extra_config.get('region_name')
                
                role_arn = extra_config.get('role_arn')
                external_id = extra_config.get('external_id')
                aws_account_id = extra_config.geet('aws_account_id')
                aws_iam_role = extra_config.get('aws_iam_role')
                
                if 'aws_session_token' in extra_config and aws_session_token is None:
                    aws_session_token = extra_config['aws_session_token']
                
                if role_arn is None and aws_account_id is not None and aws_iam_role is not None:
                    role_arn = "arn:aws:iam::{}:role/{}" \
                        .format(aws_account_id, aws_iam_role)

                if role_arn is not None: 
                    # using the credentials to get a sts_client
                    sts_session = boto3.session.Session(
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=region_name,
                        aws_session_token=aws_session_token
                    )
                    # sts assume role 
                    # https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html#examples
                    # The output of the command contains an access key, secret key, and session token 
                    # that you can use to authenticate to AWS and access resources not normally accessible
                    sts_client = sts_session.client('sts')

                    if external_id is None:
                        sts_response = sts_client.assume_role(
                            RoleArn=role_arn,
                            RoleSessionName='Airflow_' + self.aws_conn_id)
                    else:
                        sts_response = sts_client.assume_role(
                            RoleArn=role_arn,
                            RoleSessionName='Airflow_' + self.aws_conn_id,
                            ExternalId=external_id)
                    
                    # sts response contains credentials for temporary access to AWS resources
                    credentials = sts_response['Credentials']
                    aws_access_key_id = credentials['AccessKeyId']
                    aws_secret_access_key = credentials['SecretAccessKey']
                    aws_session_token = credentials['SessionToken']
                
                endpoint_url = extra_config.get('host')
            
            except AirflowException:
                pass 
        
        return boto3.session.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_access_key_id,
            aws_session_token=aws_session_token,
            region_name=region_name), endpoint_url
    
    def get_client_type(self, client_type,region_name=None, config=None):
        """get the underlying boto3 client using boto3 session"""
        session, endpoint_url = self._get_credentials(region_name)

        return session.client(client_type, endpoint_url=endpoint_url,
                              config=config, verify=self.verify)
    
    def get_resource_type(self, resource_type, region_name=None, config=None):
        """get the underlying bot3 resource using boto3 session"""
        session, endpoint_url = self._get_credentials(region_name)

        return session.resource(resource_type, endpoint_url=endpoint_url,
                                config=config, verify=self.verify)

    def get_session(self, region_name=None):
        """get the underlying boto3.session"""
        session, _ = self._get_credentials(region_name)
        return session 
    
    def get_credentials(self, region_name=None):
        """get the underlying botocore.Credentials object"""
        session, _ = self._get_credentials(region_name)
        return session.get_credentials().get_frozen_credentials()
    
    def expand_role(self, role):
        """
        if the IAM role is a role name, get 
        """
        pass 
    




##################################################
#  HTTP Hooks 
##################################################
# https://github.com/apache/airflow/blob/master/airflow/hooks/http_hook.py

import requests
import tenacity

from airflow.exceptions import AirflowException
from airflow.hooks.base_hook import BaseHook 

class HttpHook(BaseHook):
    """
    Interact with HTTP servers

    :param http_conn_id: connection that has the base API URL 
        and optional authentication credentials. Default headers in the Extra field in json format
    :type http_conn_id: str
    :param method: the API method to be called 
    :type method: str
    """

    def __init__(
        self,
        method='POST',
        http_conn_id='http_default'
    ):
        self.http_conn_id = http_conn_id
        self.method = method.upper()
        self.base_url = None 
        self._retry_obj = None 
    
    # headers maybe passed through directly or in the "extra" field
    def get_conn(self, headers=None):
        """
        Returns http session for use with requests
        :param headers: additional headers to be passed through as a dict 
        :type headers: dict
        """
        # not only return the requests session but also populate the base_url 
        # start a blank session
        session = requests.Session()
        if self.http_conn_id:
            # get the conn object via the get_connection method of BaseHook
            conn = self.get_connection(self.http_conn_id)

            # construct base_url (with host, schema, and port)
            if conn.host and "://" in conn.host:
                self.base_url = conn.host 
            else:
                schema = conn.schema if conn.schema else "http"
                host = conn.host if conn.host else ""
                self.base_url = schema + "://" + host 
            
            if conn.port:
                self.base_url = self.base_url + ":" + str(conn.port)
            if conn.login:
                session.auth = (conn.login, conn.password)
            if conn.extra:
                try:
                    session.headers.update(conn.extra_dejson)
                except TypeError:
                    self.log.warning('Connection to %s has invalid extra field', conn.host)
            if headers:
                session.headers.update(headers)
            
            return session 

    def run(self, endpoint, data=None, headers=None, extra_options=None):
        """
        Performs the request 
        :param endpoint: the endpoint to be called 
        :param data: payload to be uploaded or request parameters
        :param headers: additional headers to be passed through 
        :param extra_options: additional options to be used when executing the request 
        """
        extra_options = extra_options or {}

        session = self.get_conn(headers)

        # construct request url from base url and endpoint
        if self.base_url and not self.base_url.endswith('/') and 
           endpoint and not endpoint.startwith('/'):
            url = self.base_url + '/' + endpoint 
        else:
            url = (self.base_url or '') + (endpoint or '')

        # construct request object based on the method, url and other inputs
        req = None 
        if self.method = 'GET':
            # get uses params 
            req = requests.Request(self.method, 
                                   url,
                                   params=data,
                                   headers=headers)
        elif self.method = 'HEAD':
            # HEAD doesn't use params 
            req = requests.Request(self.method,
                                  url,
                                  headers=headers)
        else:
            # Others use data 
            req = requests.Request(self.method,
                                   url,
                                   data=data,
                                   headers=headers)
        # session prepare_request https://requests.readthedocs.io/en/master/user/advanced/
        prepped_request = session.prepare_request(req)
        self.log.info("sending '%s' to url: %s", self.method, url)
        return self.run_and_check(session, prepped_request, extra_options)

    # helper function to check response - raise AirflowException for status code except 2XX and 3XX
    def check_response(self, response):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            self.log.error("HTTP error: %s", response.reason)
            if self.method not in ['GET', 'HEAD']:
                self.log.error(response.text)
            raise AirflowException(str(response.status_code) + ":" + response.reason)
    
    # if extra options mute the status check then don't check 
    def run_and_check(self, session, prepped_request, extra_options):
        extra_options = extra_options or {}
        
        try:
            response = session.send(
                prepped_request,
                stream=extra_options.get("stream", False)
                verify=extra_options.get("verify", True),
                proxies=extra_options.get("proxies", {}),
                cert=extra_options.get("cert"),
                timeout=extra_options.get("timeout"),
                allow_redirects=extra_options.get("allow_redirects", True))
            
            if extra_options.get('check_response', True):
                self.check_response(response)
            return response 

        except requests.exceptions.ConnectionError as ex:
            self.log.warning(str(ex) + ' Tenacity will retry to execute the operation')
            raise ex
    

##################################################
#  Postgres Hooks 
##################################################

# https://github.com/apache/airflow/blob/master/airflow/hooks/postgres_hook.py

import os
from contextlib import closing

import psycopg2
import psycopg2.extensions
import psycopg2.extras

from airflow.hooks.dbapi_hook import DbApiHook

class PostgresHook(DbApiHook):
    """
    Interact with Postgres.

    Can specify ssql parameters in the extra field 

    For AWS IAM authentication, use something like extras example: ``{"iam":true, "aws_conn_id":"my_aws_conn"}``
    """
    conn_name_attr = 'postgres_conn_id'
    default_conn_name = 'posgres_default'
    supports_autocommit = True 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = kwargs.pop("schema", None)
        self.connection = kwargs.pop("connection", None)

    def _get_cursor(self, raw_cursor):
        _cursor = raw_cursor.lower()
        if _cursor == 'dictcursor':
            return psycopg2.extras.DictCursor
        if _cursor == 'realdictcursor':
            return psycopg2.extras.RealDictCursor
        if _cursor == 'namedtuplecursor':
            return psycopg2.extras.NamedTupleCursor
        raise ValueError('Invalid cursor passed {}'.format(_cursor))
    
    def get_conn(self):

        conn_id = getattr(self, self.conn_name_attr)
        conn = self.connection or self.get_connection(conn_id)

        # check for authentication via AWS IAM
        if conn.extra_dejson.get('iam', False):
            conn.login, conn.password, conn.port = self.get_iam_token(conn)

        # construct the conn args dict
        conn_args = dict(
            host=conn.host,
            user=conn.login,
            password=conn.password,
            dbname=self.schema or conn.schema
            port=conn.port)
        raw_cursor = conn.extra_dejson.get('cursor', False)
        if raw_cursor:
            conn_args['cursor_factory'] = self._get_cursor(raw_cursor)
        # check for ssl parameters in conn.extra 
        for arg_name, arg_val in conn.extra_dejson.items():
            if arg_name in ['sslmode', 'sslcert', 'sslkey',
                            'sslrootcert', 'sslcrl', 'application_name',
                            'keepalives_idle']:
                conn_args[arg_name] = arg_val
        
        self.conn = psycopg2.connect(**conn_args)
        return self.conn 

    def copy_expert(self, sql, filename, open=open):
        """
        Executes SQL using psycopg2 copy_expert method
        """
        if not os.path.isfile(filename):
            with open(filename, 'w'):
                pass 
        
        with open(filename, 'r+') as file:
            with closing(self.get_conn()) as conn:
                with closing(conn.cursor()) as cur:
                    cur.copy_expert(sql, file)
                    file.truncate(file.tell())
                    conn.commit()

    def bulk_load(self, table, tmp_file):
        """
        Loads a tab-delimited file into a database table 
        """
        self.copy_expert("COPY {table} FROM STDIN".format(table=table), tmp_file)

    def bulk_dump(self, table, tmp_file):
        """
        Dumps a database table into a tab-delimted file
        """
        self.copy_expert("COPY {table} TO STDOUT".format(table=table), tmp_file)

    # helper function to retrieve temporary credentials to connect to Postgres/ Redshift
    get_iam_token(self, conn):
    """
    Use AWSHook to retrieve a temporary password to connection to Postgres / Redshift
    """
        from airflow.contrib.hooks.aws_hook import AwsHook 

        redshift = conn.extra_dejson.get('redshift', None)
        aws_conn_id = conn.extra_dejson.get('aws_conn_id', 'aws_default')
        aws_hook = AwsHook(aws_conn_id)
        login = conn.login
        if conn.port is None:
            port = 5439 if redshift else 5432
        else:
            port = conn.port 
        if redshift:
            cluster_identifier = conn.extra_dejson.get('cluster-identifier', conn.host.split('.')[0])
            client = aws_hook.get_client_type('redshift')
            cluster_creds = client.get_cluster_credentials(
                DbUser=conn.login,
                DbName=self.schema or conn.schema,
                ClusterIdentifier = cluster_identifier,
                AutoCreate=False)
            token = cluster_creds['DbPassword']
            login = cluster_creds['DbUser']
        else:
            client = aws_hook.get_client_type('rds')
            token = client.generate_db_auth_token(conn.host, port, conn.login)
        return login, token, port 

        
##################################################
#  S3 Hook
##################################################

# https://github.com/apache/airflow/blob/master/airflow/providers/amazon/aws/hooks/s3.py

"""
Interact with AWS S3 using the boto3 library
"""

import fnmatch
import io
import re
from functools import wraps
from urllib.parse import urlparse

from botocore.exceptions import ClientError

from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.exceptions import AirflowException


def provide_bucket_name(func):
    """
    Function decorator that provides a bucket name taken from the connection
    in case no bucket name has been passed to the function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        func_params = func.__code__.code_varnames

        def has_arg(name):
            name_in_args = name in func_params and func_params.index(name) < len(args)
            name_in_kwargs = name in kwargs
            return name_in_args or name_in_kwargs
        
        if not has_arg('bucket_name') and not (has_arg('key') or has_arg('wildcard_key')):
            self = args[0]
            connection = self.get_connection(self.aws_conn_id)
            kwargs['bucket_name'] = connection.schema 
        
        return func(*args, **kwargs)
    return wrapper 


class S3Hook(AwsHook):
    """
    Interact with AWS S3, using the boto3 library
    """

    def get_conn(self):
        return self.get_client_type('s3')
    
    @staticmethod
    def parse_s3_url(s3url):
        """
        Parse S3 URL into a bucket name and key
        """
        parsed_url = urlparse(s3url)
        
        if not parsed_url.netloc:
            raise AirflowException('Please provide a bucket_name instead of "{s3url}"'.format(s3url=s3url))

        bucket_name = parsed_url.netloc
        key = parsed_url.path.strip('/')

        return bucket_name, key

    @provide_bucket_name
    def check_for_bucket(self, bucket_name=None):
        """
        Check if bucket_name exists
        """
        try:
            self.get_conn().head_bucket(Bucket=bucket_name)
            return True
        except ClientError as e:
            self.log.info(e.response["Error"]["Message"])
            return False

    @provide_bucket_name
    def get_bucket(self, bucket_name=None):
        """
        Returns a boto3.S3.Bucket object
        """
        s3_resource = self.get_resource_type('s3')
        return s3_resource.Bucket(bucket_name)
    
    @provide_bucket_name
    def create_bucket(self, bucket_name=None, region_name=None):
        """
        Creates an Amazon S3 bucket
        """
        # get conn returns a s3 client 
        s3_conn = self.get_conn()
        if not region_name:
            region_name = s3_conn.meta.region_name
        if region_name == 'us-east-1':
            self.get_conn().create_bucket(Bucket=bucket_name)
        else:
            self.get_conn().create_bucket(Bucket=bucket_name,
                                          CreateBucketConfiguration={
                                              'LocationConstraint': region_name
                                          })

    @provide_bucket_name
    def check_for_prefix(self, prefix, delimiter, bucket_name=None):
        """
        Checks that a prefix exists in a bucket
        """
        pass
        # relies on list_prefixes

    @provide_bucket_name
    def list_prefixes(self, bucket_name=None, prefix='', delimiter='', 
                      page_size=None, max_items=None):
        """
        List prefixes in a bucket under prefix 
        """
        pass 
        # calls self.get_conn().get_paginator

    @provide_bucket_name
    def list_keys(self, bucket_name=None, prefix='', delimiter='', 
                  page_size=None, max_items=None):
        """
        List keys in a bucket under prefix and not containing delimiter
        """
        config = {
            'PageSize': page_size,
            'MaxItems': max_items,
        }

        paginator = self.get_conn().get_paginator('list_objects_v2')
        response = paginator.paginate(Bucket=bucket_name,
                                      Prefix=prefix,
                                      Delimiter=delimiter,
                                      PaginationConfig=config)
        has_results = False 
        keys = []
        for page in response:
            if 'Contents' in page: 
                has_results = True 
                for k in page['Contents']:
                    keys.append(k['Key'])
        
        if has_results:
            return key 
        return None 

    @provide_bucket_name
    def check_for_key(self, key, bucket_name=None):
        """
        Checks if a key exists in a bucket
        """
        if not bucket_name:
            (bucket_name, key) = self.parse_s3_url(key)

        try:
            self.get_conn().head_object(Bucket=bucket_name, key=key)
            return True 
        except ClientError as e:
            self.log.info(e.response["Error"]["Message"])
            return False 
    
    @provide_bucket_name
    def get_key(self, key, bucket_name=None):
        """
        Returns a boto3.s3.Object (the key object from the bucket)
        """
        if not bucket_name:
            (bucket_name, key) = self.parse_s3_url(key)
        
        obj = self.get_resource_type('s3').Object(bucket_name, key)
        obj.load()
        return obj
    
    @provide_bucket_name
    def read_key(self, key, bucket_name=None):
        """
        Reads a key from S3
        Returns a boto3.s3.Object (the content of the key)
        """
        obj = self.get_key(key, bucket_name)
        return obj.get()['Body'].read().decode('utf-8')
    
    @provide_bucket_name
    def select_key(self, key, bucket_name=None,
                   expression='SELECT * FROM S3Object',
                   expression_type='SQL',
                   input_serialization=None,
                   output_serialization=None):
        pass
    
    @provide_bucket_name
    def check_for_wildcard_key(self,
                               wildcard_key, bucket_name=None, delimiter=''):
        pass 

    @provide_bucket_name
    def get_wildcard_key(self, wildcard_key, bucket_name=None, delimiter=''):
        pass

    @provide_bucket_name
    def load_file(self,
                  filename,
                  key,
                  bucket_name=None,
                  replace=False,
                  encrypt=False):
        """
        loads a local file to s3 
        :param key: S3 key that will point to the file
        :param bucket_name: name of the bucket in which to store the file
        """
        if not bucket_name:
            (bucket_name, key) = self.parse_s3_url(key)
        
        if not replace and self.check_for_key(key, bucket_name):
            raise ValueError("They key {key} already exists.".format(key=key))

        # construct ExtraArgs for client.upload_file  
        extra_args = {}
        if encrypt:
            extra_args['ServerSideEncryption'] = "AES256"
        
        client = self.get_conn()
        client.upload_file(filename, bucket_name, key, ExtraArgs=extra_args)

    # below are functions to upload alernative formats
    @provide_bucket_name
    def load_string(self,
                    string_data,
                    key,
                    bucket_name=None,
                    replace=False,
                    encrypt=False,
                    encoding='utf-8'):
        """
        Loads a string to S3
        This is provided as a convenience to drop a string in S3. It uses the
        boto infrastructure to ship a file to s3.
        """
        bytes_data = string_data.encode(encoding)
        file_obj = io.BytesIO(bytes_data)
        self._upload_file_obj(file_obj, key, bucket_name, replace, encrypt)
    

    @provide_bucket_name
    def load_bytes(self,
                   bytes_data,
                   key,
                   bucket_name=None,
                   replace=False,
                   encrypt=False):
        """
        Loads bytes to S3
        """
        file_obj = io.BytesIO(bytes_data)
        self._upload_file_obj(file_obj, key, bucket_name, replace, encrypt)

    @provide_bucket_name
    def load_file_obj(self,
                      file_obj,
                      key,
                      bucket_name=None,
                      replace=False,
                      encrypt=False):
        """
        Loads a file object to S3
        """
        self._upload_file_obj(file_obj, key, bucket_name, replace, encrypt)

    # this is the helper function for uploading a file obj 
    def _upload_file_obj(self,
                         file_obj,
                         key,
                         bucket_name=None,
                         replace=False,
                         encrypt=False):
        if not bucket_name:
            (bucket_name, key) = self.parse_s3_url(key)
        
        if not replace and self.check_for_key(key, bucket_name):
            raise ValueError("The key {key} already exists".format(key=key))
            
        extra_args = {}
        if encrypt:
            extra_args['ServerSideEncryption'] = "AES256"

        client = self.get_conn()
        client.upload_fileobj(file_obj, bucket_name, key, ExtraArgs=extra_args)

    def copy_object(self,
                    source_bucket_key,
                    dest_bucket_key,
                    source_bucket_name=None,
                    dest_bucket_name=None,
                    source_version_id=None):
        """
        Creates a copy of an object that is already stored in S3 
        """
        # example code for copy_object https://docs.aws.amazon.com/code-samples/latest/catalog/python-s3-copy_object.py.html
        if dest_bucket_name is None:
            dest_bucket_name, dest_bucket_key = self.parse_s3_url(dest_bucket_key)
        else:
            parsed_url = urlparse(dest_bucket_key)
            if parsed_url.scheme != '' or parsed_url.netloc != '':
                raise AirflowException('If dest_bucket_name is provided, ' +
                                       'dest_bucket_key should be relative path ' +
                                       'from root level, rather than a full s3:// url')

        if source_bucket_name is None:
            source_bucket_name, source_bucket_key = self.parse_s3_url(source_bucket_key)
        else:
            parsed_url = urlparse(source_bucket_key)
            if parsed_url.scheme != '' or parsed_url.netloc != '':
                raise AirflowException('If source_bucket_name is provided, ' +
                                       'source_bucket_key should be relative path ' +
                                       'from root level, rather than a full s3:// url')

        copy_source = {'Bucket': source_bucket_name,
                       'Key': source_bucket_key,
                       'VersionId': source_version_id}
        response = self.get_conn().copy_object(Bucket=dest_bucket_name,
                                               Key=dest_bucket_key,
                                               CopySource=copy_source)
        return response


    def delete_objects(self, bucket, keys):
        """
        Delete keys from the bucket
        """
        if isinstance(keys, list):
            keys = keys
        else:
            keys = [keys]
        
        delete_dict={"Objects": [{"Key":k} for k in keys]}
        response = self.get_conn().delete_objects(Bucket=bucket, Delete=delete_dict)

        return response 



    