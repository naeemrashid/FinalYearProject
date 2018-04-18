base_url='http://127.0.0.1:8000'
headers={'content-type':'application/json'}
tiller_base_url='http://192.168.99.100:32410'
class Defaults:
    def __init__(self,base_url,_tiller_base_url):
        base_url=base_url
        headers={'content-type':'application/json'}
        tiller_base_url=_tiller_base_url
