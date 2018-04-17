import requests
import json
from default_config import base_url
from default_config import headers
import kube_svc
def create_ingress(name,namespace):
    services=kube_svc.list_namespaced_services(namespace)
    paths=[]
    for service in services:
        path={
            "backend":{
                "serviceName": service['name'],
                "servicePort":service['port']
                },
            "path":"/"+service['name']
            }
        paths.append(path)
    print(json.dumps(paths))
    url=base_url+'/apis/extensions/v1beta1/namespaces/'+namespace+'/ingresses'
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
                  "paths": paths
            }
         }
      ]
   }
}
    r=requests.post(url=url,json=payload,headers=headers)
    print(r.text)
    print(r.status_code)
    return
def update_ingress(ingress,namespace):
    delete_ingress(ingress=ingress,namespace=namespace)
    create_ingress(ingress,namespace)
    return
def delete_ingress(ingress,namespace):
    url=base_url+'/apis/extensions/v1beta1/namespaces/'+namespace+'/ingresses/'+ingress
    response=requests.delete(url=url,headers=headers)
    print(response.status_code)
    return response.status_code
def is_ingress_exist(ingress,namespace):
    url=base_url+'/apis/extensions/v1beta1/namespaces/'+namespace+'/ingresses/'+ingress
    response=requests.get(url=url,headers=headers)
    print(response.status_code)
    if response.status_code==404:
        return False
    return True
# def main():
#     print(update_ingress('testing-ingress','user-123'))
# if __name__=='__main__':
#     main()
