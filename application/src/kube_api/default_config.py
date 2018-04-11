_base_url='http://127.0.0.1:8000'
_headers={'content-type':'application/json'}
_tiller_base_url='http://192.168.99.100:32747'
class Defaults:
    def __init__(self,base_url,_tiller_base_url):
        _base_url=base_url
        _headers={'content-type':'application/json'}
        _tiller_base_url=_tiller_base_url
