import requests
import json

class HttpLib():

    __MAX_TIMEOUT       = 6.0

    __ENCODING          = 'UTF-8'

    __CONTENT_TYPE_JSON = 'application/json'

    def __init__(self):
        pass

    def get(self, url, params, headers):
        data = self._request(url, 'get', params, headers)
        return data

    def post(self, url, params, headers, files):
        data = self._request(url, 'post', params, headers, files)
        return data

    def delete(self, url, params, headers):
        data = self._request(url, 'delete', params, headers)
        return data

    def head(self, url, params, headers):
        data = self._request(url, 'head', params, headers)
        return data

    def options(self, url, params, headers):
        data = self._request(url, 'options', params, headers)
        return data

    def _request(self, url, method, payload, headers, files=None):
        if headers.get("Content-Type") == self.__CONTENT_TYPE_JSON:
            payload = json.dumps(payload)
        try:
            req_fun = getattr(requests, method)
            res     = req_fun(url=url, data=payload, headers=headers, timeout=self.__MAX_TIMEOUT, files=files)
        except requests.exceptions.RequestException:
            print("url请求错误", payload)
        except Exception:
            print("未知请求错误", payload)
        res.encoding = self.__ENCODING
        data              = {}
        if res.headers.get("Content-Type") == self.__CONTENT_TYPE_JSON:
           data['body']   = json.loads(res.text)
        else:
            data['body']  = res.text
        data['code']      = res.status_code
        data['length']    = res.headers.get('Content-Length')
        return data