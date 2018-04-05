import requests

def is_namespace_exist(name):
    url = 'http://127.0.0.1:8000/api/v1/namespaces/'+name
    headers = {'content-type': 'application/json'}
    r = requests.get(url=url, headers=headers)
    print(r.text)
    return True
def create_namespace(name):
    url = 'http://127.0.0.1:8000/api/v1/namespaces'
    payload = {
        "apiVersion": "v1",
        "kind": "Namespace",
        "metadata": {
            "name": name
        }
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(url=url, json=payload, headers=headers)
    print(r.text)
    return
def delete_namespace(name):
    url = 'http://127.0.0.1:8000/api/v1/namespaces/' + name
    headers = {'content-type': 'application/json'}
    r = requests.delete(url=url, headers=headers)
    print(r.text)
    return
def delete_all_namespaces(namespaces):
    return
def setup_namespace(name):
    return