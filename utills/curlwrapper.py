
from src import *
from src.util.logger import logger
logger = logger('Curl Wrapper')

class responsewrapper:
    # Full wrapper in paid only bc of skiddies 👍👍👍👍👍
    def __init__(self, response=None, error=None):
        if response:
            self._response = response
            self.status_code = response.status_code
            self.headers = dict(response.headers) if response.headers else {}
            self.text = response.text
            self.cookies = response.cookies
            self.error = None

        else:
            self._response = None
            self.status_code = 0
            self.headers = {}
            self.text = str(error) if error else 'Error'
            self.cookies = None
            self.error = error
    
    def json(self) -> dict:
        if self.error:
            logger.error(text=f'Cannot parse JSON', error=self.error, ts=True)
            return {}
            
        try:
            return self._response.json()
        except Exception as e:
            logger.error(text=f'Failed to parse JSON', error=self.error, ts=True)
            return {}

class sessionwrapper:
    def __init__(self, impersonate=None):
        self.session = curlcffi.Session(impersonate=impersonate)
        self.proxies = self.session.proxies
        self.cookies = self.session.cookies
        self.headers = dict(self.session.headers) if self.session.headers else {}
        
    def adddata(self, kwargs):
        headers = kwargs.get('headers', {})
        
        if 'json' in kwargs:
            payload = kwargs.pop('json')
            kwargs['data'] = json.dumps(payload, separators=(',', ':')).encode()
            if 'Content-Type' not in headers:
                headers['Content-Type'] = 'application/json'
            
        if headers:
            kwargs['headers'] = headers
            
        return kwargs
   
    def request(self, method, url, **kwargs):
        headers = dict(kwargs.get('headers', {})) if kwargs.get('headers') else {}

        kwargs['headers'] = headers

        kwargs = self.adddata(kwargs)
        
        try:
            r = self.session.request(method, url, **kwargs)
            return responsewrapper(r)
        
        except curlcffi_.curl.CurlError as e:
            logger.error(f'Curl error', e)
            return responsewrapper(error=f'Curl error: {e}')
        
        except curlcffi.exceptions.ConnectionError as e:
            logger.error(f'Connection error', e)
            return responsewrapper(error=f'Connection error {e}')
        
        except curlcffi.exceptions.HTTPError as e:
            logger.error(f'HTTP error', e)
            return responsewrapper(error=f'HTTP error {e}')
        
        except curlcffi.exceptions.ReadTimeout as e:
            logger.error(f'Timeout', e)
            return responsewrapper(error=f'Read timeout {e}')
        
        except curlcffi.exceptions.Timeout as e:
            logger.error(f'Timeout', e)
            return responsewrapper(error=f'Request timeout {e}')
        
        except curlcffi.exceptions.TooManyRedirects as e:
            logger.error(f'Too many redirects', e)
            return responsewrapper(error=f'Too many redirects {e}')
        
        except curlcffi.exceptions.RequestException as e:
            logger.error(f'Request exception', e)
            return responsewrapper(error=f'Request exception {e}')

        except Exception as e:
            logger.error(e)
            return responsewrapper(error=e)
    
    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)
    
    def post(self, url, **kwargs):
        return self.request('POST', url, **kwargs)
    
    def put(self, url, **kwargs):
        return self.request('PUT', url, **kwargs)
   
    def patch(self, url, **kwargs):
        return self.request('PATCH', url, **kwargs)
    
    def delete(self, url, **kwargs):
        return self.request('DELETE', url, **kwargs)


class curlwrapper:
    def Session(impersonate=None):
        return sessionwrapper(impersonate=impersonate)