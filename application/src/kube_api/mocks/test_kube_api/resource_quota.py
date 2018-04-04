import requests
def create_quota(namespace):
	payload={"apiVersion":"v1","kind":"ResourceQuota",
	"metadata":{"name":"student-quota","namespace":namespace},
	"spec":{"hard":{"limits.cpu":"3","limits.memory":"4Gi","persistentvolumeclaims":"5","pods":"20",
	"replicationcontrollers":"10","requests.cpu":"2","requests.memory":"2Gi","services":"10","services.loadbalancers":"5"}}}
	url='http://127.0.0.1:8000/api/v1/namespaces/testnamespace/resourcequotas'
	headers={'content-type': 'application/json'}
	r=requests.post(url=url,json=payload,headers=headers)
	print(r.text)
def delete_quota(namespace):
	url='http://127.0.0.1:8000/api/v1/namespaces/'+namespace+'/resourcequotas'
	headers={'content-type': 'application/json'}
	r=requests.delete(url=url,headers=headers)
	print(r.text)
def main():
	create_quota('testnamespace')
	delete_quota('testnamespace')
if __name__=='__main__':
	main()
