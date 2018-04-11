import requests
from default_config import base_url
from default_config import headers
def apply_quotas(namespace):
    payload = {"apiVersion": "v1",
               "kind": "ResourceQuota",
               "metadata": {
                   "name": "student-quota",
                   "namespace": namespace
               },
               "spec": {
                   "hard": {
                       "limits.cpu": "3",
                       "limits.memory": "4Gi",
                       "persistentvolumeclaims": "5",
                       "pods": "20",
                        "replicationcontrollers": "10",
                       "requests.cpu": "2",
                       "requests.memory": "2Gi",
                        "services": "10",
                       "services.loadbalancers": "5"
                   }
               }
               }
    url = base_url+'/api/v1/namespaces/'+namespace+'/resourcequotas'
    headers = {'content-type': 'application/json'}
    r = requests.post(url=url, json=payload, headers=headers)
    print(r.text)
    print(r.status_code)
    return
def modify_quota(namespace,body):
    return
def delete_quotas(namespace):
    url = base_url+'/api/v1/namespaces/' + namespace + '/resourcequotas'
    headers = {'content-type': 'application/json'}
    r = requests.delete(url=url, headers=headers)
    print(r.text)
    print(r.status_code)
    return
def get_quota(namespace):
    url = base_url+'/api/v1/namespaces/' + namespace + '/resourcequotas'
    headers = {'content-type': 'application/json'}
    r = requests.get(url=url, headers=headers)
    print(r.text)
    print(r.status_code)
    return r.text
