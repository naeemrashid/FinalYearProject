import requests
from default_config import base_url
from default_config import headers
from default_config import tiller_base_url
def install(chart_url,namespace,app_name):
	if exist(namespace,app_name):
		uninstall(namespace,app_name)
	data=  {
	            "chart_url": chart_url,
		        "namespace": namespace,
				"values":{
					"raw":"{\"proxy\":{\"secretToken\":\"df9b0056bb6e47580b9ea01124d6347dbb73b33e0a76cda27c2ce78e56191b4c\"}}"
				}
            }
	response=requests.post(url=tiller_base_url+'/tiller/v2/releases/'+namespace+app_name+'/json',headers=headers,json=data)
	print(response.text)
	return response.status_code
def uninstall(namespace,app_name):
	response=requests.delete(url=tiller_base_url+'/tiller/v2/releases/'+namespace+app_name+'/json?purge=true',headers=headers)
	print(response.text)
	return response.status_code()
def exist(namespace,app_name):
	release_name=namespace+app_name
	response=requests.get(url=tiller_base_url+'/tiller/v2/releases/json?namespace='+namespace,headers=headers).json()
	if 'releases' in response:
		releases=(response['releases'])
		for release in releases:
			if release_name==release['name'] and release['info']['status']['code']=='DEPLOYED':
				return True
		print('Does not Exist !')
	return False
