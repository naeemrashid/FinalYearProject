import src.kube_api.namespace as nm
import src.kube_api.helm_proxy as helm
from src.kube_api.default_config import base_url
def install_app(app_name,chart_url,namespace,extra_config):
    message=None
    if nm.is_namespace_exist(namespace)==False:
        message=nm.setup_namespace(namespace)
        print(message)
    if helm.exist(namespace,app_name)==False:
        response=helm.install(chart_url,namespace,app_name)
        print(response)
        if response==201 or response==200:
            #ingress.update_ingress('ingress', namespace)
            message='Application Install Successful'
        else:
            message='Exception Occured'
    return message
def remove_app(namespace,app_name):
    return helm.uninstall(namespace,app_name)
def list_apps(namespace):
    return
def main():
    message=install_app('jupyterhub','https://jupyterhub.github.io/helm-chart/jupyterhub-v0.6.tgz','user-321','type: NodePort')
    print(message)
if __name__=='__main__':
    main()
