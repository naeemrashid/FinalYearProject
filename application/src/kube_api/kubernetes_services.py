from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
v1 = client.CoreV1Api()
list_services=v1.list_service_for_all_namespaces(watch=False)
for i in v1.list_node(watch=False).items:
    address=i.status.addresses
    for i in address:
        print("%s\t%s" % (i.type, i.address))
        if i.type=="InternalIP":
            minikube_address=i.address
def access_node_service(service_name):
    for service in list_services.items:
        if(service.metadata.name==service_name and service.spec.type=="NodePort"):
            ports=service.spec.ports
            for port in ports:
                print("name: %s\t NodePort: %s\t ClusterPort: %s\t NodeIP: %s\t"%(port.name,port.node_port,port.port,minikube_address))
                node_port=port.node_port
    return (minikube_address,node_port)
def acess_cluster_service(service_name):
    for service in list_services.items:
        if(service.metadata.name==service_name and service.spec.type=="ClusterIP"):
            ports=service.spec.ports
            cluster_ip=service.spec.cluster_ip
            for port in ports:
                print("name: %s\t ClusterPort: %s\t ClusterIP: %s\t"%(port.name,port.port,cluster_ip))
                node_port=port.node_port
    return (minikube_address,node_port)
# print(list_services)