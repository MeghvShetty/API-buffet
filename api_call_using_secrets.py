from email import header
from lib2to3.pgen2 import token
import os
import secrets
from urllib import response
from wsgiref import headers
import requests
import secrets_mgr



os.environ['AWS_DEFAULT_REGION'] = 'eu-east-2' 
token = secrets_mgr.get_secret("secrets") # The name used in secrects manager 

headers = {
    "Accept": "application/json",
    "X-ApiKeys": f"accessKey={token['accessKey']};secretKey={token['secretKey']}"
}

def api_call():
    url = "Url"
    response = requests.get(url,headers=headers)
    return response.json()


def main():
    output = api_call()
    print(output)

if __name__ == '__main__':
    main()