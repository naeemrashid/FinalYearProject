# Installtion of Helm
+ [Helm download from github](https://github.com/kubernetes/helm/releases)
+ Place the binaries into your path.
+ Install tiller(helm server) into kubernetes cluster [link](https://docs.helm.sh/using_helm/#installing-helm)
``helm init``

# Helm Charts and structure
+ Helm charts: [structure and details](https://github.com/kubernetes/helm/blob/master/docs/charts.md)
+ Search for a chart.
``helm search chart-name``
+ Install a chart to k8s cluster.
``helm install chart-name``
+ create a chart
``helm create chart.tgz``