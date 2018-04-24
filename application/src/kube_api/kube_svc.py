import requests
from src.kube_api.default_config import base_url
from src.kube_api.default_config import headers
def list_namespaced_services(namespace):
    url=base_url+'/api/v1/namespaces/'+namespace+'/services'
    response=requests.get(url=url,headers=headers).json()
    print(response)
    apps=[]
    for service in response['items']:
        # print(service['metadata']['name']
        # for port in service['spec']['ports'][0]:
        #     print(port['port'])
        #     ports.append(port['port'])
        port=service['spec']['ports'][0]['port']
        type=service['spec']['type']
        if type == 'NodePort':
            port = service['spec']['ports'][0]['nodePort']
        item={'name':service['metadata']['name'],
              'port':port,
              'type':type}
        apps.append(item)
    return apps
def get_nodes():
    url=base_url+'/api/v1/nodes'
    response=requests.get(url=url,headers=headers).json()
    nodes=[]
    for node in response['items']:
        node_name = ""
        node_ip = ""
        for address in node['status']['addresses']:
            if address['type']=='InternalIP':
               # print('node ip {}'.format(address['address']))
                #node_ip=address['address']
                node_ip=address['address']
            elif address['type']=='Hostname':
                node_name=address['address']
                #print('node name {}'.format(address['address']))
        node={'hostname':node_name, 'ip':node_ip}
        nodes.append(node)
    return nodes
    #print(response['items'][0]['status']['addresses'])
# def main():
#     #apps=list_namespaced_services('kube-system')
#     nodes=get_nodes()
#     for node in nodes:
#         print(node['ip'])
#     # for app in apps:
#     #     print('Name ',app['name'])
#     #     print(' Port ',app['port'])
# if __name__ == '__main__':
#     main()