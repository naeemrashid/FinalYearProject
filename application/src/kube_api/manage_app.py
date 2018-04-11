from kubernetes import client, config
import src.kube_api.namespace as nm
import src.kube_api.default_limits as limit
import src.kube_api.quotas as quota
import sre.kube_api.helm_proxy as helm
config.load_kube_config()
def install_app(app_name,chart_url,namespace,extra_config):
    if nm.is_namespace_exist(namespace)==False:
        nm.create_namespace(namespace)
        quota.apply_quotas(namespace)
        limit.add_default_limits(namespace)
    if helm.exist(namespace,app_name)==False:
        response_code=helm.install_app(chart_url,namespace,app_name)
        else:
            print 'application is already installed'
    return
def remove_app(app_name,namespace):
    return
def list_apps(namespace):
    return
def app_url(app_name,namespace):
    return