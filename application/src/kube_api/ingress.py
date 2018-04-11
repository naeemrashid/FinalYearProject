import requests
from default_config import _base_url
from default_config import _headers
def create_ingress(namespace,name):
    url=_base_url+'/apis/extensions/v1beta1/namespaces/'+namespace+'/ingresses'
    payload={
   "apiVersion":"extensions/v1beta1",
   "kind":"Ingress",
   "metadata":{
      "annotations":{
         "nginx.ingress.kubernetes.io/rewrite-target":"/"
      },
      "name": name,
      "namespace": namespace
   },
   "spec":{
      "backend":{
         "serviceName":"default-http-backend",
         "servicePort":80
      },
      "rules":[
         {
            "host":"apps.namal.edu.pk",
            "http":{
               "paths":[
                  {
                     "backend":{
                        "serviceName":"stilton-cheese",
                        "servicePort":80
                     },
                     "path":"/stilton"
                  },
                  {
                     "backend":{
                        "serviceName":"cheddar-cheese",
                        "servicePort":80
                     },
                     "path":"/cheddar"
                  }
               ]
            }
         }
      ]
   }
}
    r=requests.post(url=url,json=payload,headers=headers)
    print(r.text)
    print(r.status_code)
    return r.status_code
def update_ingress(ingress,namespace):
    return
def delete_ingress(ingress,namespace):
    url=_base_url+'/apis/extensions/v1beta1/namespaces/'+namespace+'/ingresses/'+ingress
    response=requests.delete(url=url,headers=headers)
    print(response.status_code)
    return response.status_code
def is_ingress_exist(ingress,namespace):
    url=_base_url+'/apis/extensions/v1beta1/namespaces/'+namespace+'/ingresses/'+ingress
    response=requests.get(url=url,headers=headers)
    print(response.status_code)
    if response.status_code==404:
        return False
    return True
def get_namespaced_services(namespace):
    url=_base_url+'/api/v1/namespaces/default/services?limit=500'
    headers={'content-type': 'application/json'}
    response=requests.get(url=url,headers=headers)
    print(response.text)
    for item in response.json()['items']:
        print(item['metadata']['name'])
        for port in item['spec']['ports']:
            print(port['targetPort'])
def main():
    get_namespaced_services('testnamespace')
if __name__=='__main__':
    main()
