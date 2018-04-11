import namespace as nm
import default_limits as limit
import quotas as quota
import helm_proxy as helm
def install_app(app_name,chart_url,namespace,extra_config):
    if nm.is_namespace_exist(namespace)==False:
        nm.create_namespace(namespace)
        quota.apply_quotas(namespace)
        limit.add_default_limits(namespace)
    if helm.exist(namespace,app_name)==False:
        response_code=helm.install(chart_url,namespace,app_name)
    return
def remove_app(app_name,namespace):
    return
def list_apps(namespace):
    return
def app_url(app_name,namespace):
    return
def main():
    install_app('mongodb','stable/mongodb','user-123','type: NodePort')
if __name__=='__main__':
    main()
