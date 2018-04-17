import requests
from default_config import base_url
from default_config import headers
def list_namespaced_services(namespace):
    url=base_url+'/api/v1/namespaces/'+namespace+'/services'
    response=requests.get(url=url,headers=headers).json()
    # print(response)
    apps=[]
    for service in response['items']:
        # print(service['metadata']['name']
        # for port in service['spec']['ports'][0]:
        #     print(port['port'])
        #     ports.append(port['port'])
        port=service['spec']['ports'][0]['port']
        item={'name':service['metadata']['name'],
              'port':port}
        apps.append(item)
    return apps

def main():
    apps=list_namespaced_services('kube-system')
    for app in apps:
        print('Name ',app['name'])
        print(' Port ',app['port'])
if __name__ == '__main__':
    main()