from kubernetes import client, config
import src.kube_api.namespace as nm
import src.kube_api.default_limits as limit
import src.kube_api.quotas as quota
config.load_kube_config()
def install_app(app_name,chart_url,namespace,extra_config):
    nm.is_namespace_exist(namespace)
    nm.create_namespace(namespace)
    quota.apply_quotas(namespace)
    limit.add_default_limits(namespace)
    return
def remove_app(app_name,namespace):
    return
def list_apps(namespace):
    return
def app_url(app_name,namespace):
    return