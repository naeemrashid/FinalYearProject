import requests
from default_config import _base_url
from default_config import _headers
from default_config import _tiller_base_url
def install(chart_url,namespace,app_name):
    if exist(namespace,app_name):
	uninstall(namespace,app_name)
    data=  {
	            "chart_url": chart_url,
		    "namespace": namespace
            }
    response=requests.post(url=_tiller_base_url+'/tiller/v2/releases/'+namespace+app_name+'/json',headers=headers,json=data)
    print(response.text)
def uninstall(namespace,app_name):
    	response=requests.delete(url=_tiller_base_url+'/tiller/v2/releases/'+namespace+app_name+'/json?purge=true',headers=headers)
	print(response.text)
def exist(namespace,app_name):
	release_name=namespace+app_name
	response=requests.get(url=_tiller_base_url+'/tiller/v2/releases/json?namespace='+namespace,headers=headers).json()
	releases=(response['releases'])
	for release in releases:
		print(release['name'])
		if release_name==release['name']:
			return True
	return False
def main():
	exist('testnamespace','test-release')
if __name__=='__main__':
	main()
