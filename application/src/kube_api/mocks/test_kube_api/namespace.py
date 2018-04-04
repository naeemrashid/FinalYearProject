import requests

def create_namespace(namespace):
	url='http://127.0.0.1:8000/api/v1/namespaces'
	payload={
    	"apiVersion": "v1",
    	"kind": "Namespace",
    	"metadata": {
        "name": namespace
    		}
	}
	headers={'content-type': 'application/json'}
	r=requests.post(url=url,json=payload,headers=headers)
	print(r.text)
def delete_namespace(namespace):
	url='http://127.0.0.1:8000/api/v1/namespaces/'+namespace
	headers={'content-type': 'application/json'}
	r=requests.delete(url=url,headers=headers)
	print(r.text)
def namespace_exist(namespace):
	url='http://127.0.0.1:8000/api/v1/namespaces/'+namespace
	headers={'content-type': 'application/json'}
	r=requests.get(url=url,headers=headers)
	print(r.text)
def main():
	create_namespace('testnamespace')
	namespace_exist('testnamespace')
	#delete_namespace('testnamespace')
if __name__=='__main__':
	main()
