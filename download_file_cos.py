#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from ibm_botocore.client import Config
import ibm_boto3
def download_file_cos(credentials, local_file_name, key):  
    cos = ibm_boto3.client(service_name='s3',
    ibm_api_key_id=credentials['IBM_API_KEY_ID'],
    ibm_service_instance_id=credentials['IAM_SERVICE_ID'],
    ibm_auth_endpoint=credentials['IBM_AUTH_ENDPOINT'],
    config=Config(signature_version='oauth'),
    endpoint_url=credentials['ENDPOINT'])
    try:
        res = cos.download_file(Bucket=credentials['BUCKET'], Key=key, Filename=local_file_name)
    except Exception as e:
        print(Exception, e)
    else:
        print("Dowloaded:", key, 'from IBM COS to local:', local_file_name)

def import():
	file=input("Insert the full filename: ")
	cred=input("Insert the credentials name: ")
	download_file_cos(eval(cred), file , file) 


