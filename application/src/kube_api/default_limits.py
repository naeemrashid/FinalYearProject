import requests
from default_config import base_url
from default_config import headers
def add_default_limits(namespace):
	url=base_url+'/api/v1/namespaces/'+namespace+'/limitranges'
	payload={"apiVersion":"v1",
	"kind":"LimitRange",
	"metadata":{
		"annotations":{
			"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"v1\",\"kind\":\"LimitRange\",\"metadata\":{\"annotations\":{},\"name\":\"default-limits\",\"namespace\":namespace},\"spec\":{\"limits\":[{\"default\":{\"cpu\":\"200m\",\"memory\":\"512Mi\"},\"defaultRequest\":{\"cpu\":\"100m\",\"memory\":\"256Mi\"},\"type\":\"Container\"}]}}\n"},"name":"default-limits","namespace":namespace},"spec":{"limits":[{"default":{"cpu":"200m","memory":"512Mi"},"defaultRequest":{"cpu":"100m","memory":"256Mi"},"type":"Container"}]}}
	r=requests.post(url=url,json=payload,headers=headers)
	print(r.text)
	print(r.status_code)
	return r.status_code
def delete_default_limits(namespace):
	url= base_url+'/api/v1/namespaces/'+namespace+'/limitranges'
	r=requests.delete(url=url,headers=headers)
	print(r.text)
	print(r.status_code)
	return
def main():
	add_default_limits('anothertest')
if __name__=='__main__':
	main()
