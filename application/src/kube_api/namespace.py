import requests
from default_config import _base_url
from default_config import _headers
def is_namespace_exist(name):
    url = _base_url+'/api/v1/namespaces/'+name
    r = requests.get(url=url, headers=headers)
    print(r.text)
    print(r.status_code)
    if r.status_code==404:
        return False
    return True
def create_namespace(name):
    url = _base_url+'/api/v1/namespaces'
    payload = {
        "apiVersion": "v1",
        "kind": "Namespace",
        "metadata": {
            "name": name
        }
    }
    r = requests.post(url=url, json=payload, headers=headers)
    print(r.text)
    print(r.status_code)
    return r.status_code
def delete_namespace(name):
    url = _base_url+'/api/v1/namespaces/' + name
    r = requests.delete(url=url, headers=headers)
    print(r.text)
    print(r.status_code)
    return r.status_code
def delete_all_namespaces(namespaces):
    return
def setup_namespace(name):
    return
