import requests
def install(chart_url,namespace,release_name):
    base_url='http://192.168.99.100:32747'
    headers={'content-type': 'application/json'}
    data=  {
	            "chart_url": chart_url,
		    "namespace":"testnamespace"
            }

    response=requests.post(url=base_url+'/tiller/v2/releases/'+release_name+'/json',headers=headers,json=data)
    print(response)
def main():
	install('stable/mongodb','testnamespace','mongodb')
if __name__=='__main__':
	main()
