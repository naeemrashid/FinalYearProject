import requests
from default_config import base_url
from default_config import headers
import default_limits as limit
import quotas as quota
def is_namespace_exist(name):
    url = base_url+'/api/v1/namespaces/'+name
    r = requests.get(url=url, headers=headers)
    print(r.text)
    print(r.status_code)
    if r.status_code==404:
        return False
    return True
def create_namespace(name):
    url = base_url+'/api/v1/namespaces'
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
    url = base_url+'/api/v1/namespaces/' + name
    r = requests.delete(url=url, headers=headers)
    print(r.text)
    print(r.status_code)
    return r.status_code
def delete_all_namespaces(namespaces):
    return
def setup_namespace(name):
    nm=create_namespace(name)
    #qts=quota.apply_quotas(name)
    #lim=limit.add_default_limits(name)
    print("",nm,qts,lim)
    #if nm==201 and qts==201 and lim==201:
    #    return 'Setup Successfull'
    return 'Something went wrong'
