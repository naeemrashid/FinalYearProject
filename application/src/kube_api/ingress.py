from kubernetes import client, config

config.load_kube_config()
def __init__(username):
    _username=username
    _namespace=username

def create_ingress(namespace,body):
    return None
def update_ingress(ingress,namespace,body):
    return
def delete_ingress(ingress,namespace):
    return
def is_ingress_exist(ingress,namespace):
    return