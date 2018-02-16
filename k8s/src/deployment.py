from os import path
import yaml
# import urllib.request
from kubernetes import client, config
def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()
    # response = urllib.request.urlopen()
    with open(path.join(path.dirname(__file__), "nginx-deployment.yaml")) as f:
        dep = yaml.load(f)
        # v1 = client.CoreV1Api()
        k8s_beta = client.ExtensionsV1beta1Api()
        resp = k8s_beta.create_namespaced_deployment(body=dep, namespace="default")
        print("Deployment created. status='%s'" % str(resp.status))

if __name__ == '__main__':
    main()