import requests
def add_default_limits(namespace):
	url='http://127.0.0.1:8000/api/v1/namespaces/'+namespace+'/limitranges'
	payload={"apiVersion":"v1","kind":"LimitRange","metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"v1\",\"kind\":\"LimitRange\",\"metadata\":{\"annotations\":{},\"name\":\"default-limits\",\"namespace\":\"testnamespace\"},\"spec\":{\"limits\":[{\"default\":{\"cpu\":\"200m\",\"memory\":\"512Mi\"},\"defaultRequest\":{\"cpu\":\"100m\",\"memory\":\"256Mi\"},\"type\":\"Container\"}]}}\n"},"name":"default-limits","namespace":"testnamespace"},"spec":{"limits":[{"default":{"cpu":"200m","memory":"512Mi"},"defaultRequest":{"cpu":"100m","memory":"256Mi"},"type":"Container"}]}}
	headers={'content-type': 'application/json'}
	r=requests.post(url=url,json=payload,headers=headers)
	print(r.text)
def delete_default_limits(namespace):
	url='http://127.0.0.1:8000/api/v1/namespaces/'+namespace+'/limitranges'
	headers={'content-type': 'application/json'}
	r=requests.delete(url=url,headers=headers)
	print(r.text)