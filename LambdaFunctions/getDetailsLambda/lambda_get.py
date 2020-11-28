import boto3
import json

dynamodb = boto3.client('dynamodb')
tableName = "CustomerDetails"

def lambda_handler(event, context):
	#1. Parse out query string params
	email = event['EmailID']
	
	#2. Construct the body of the response object
	
	response = dynamodb.get_item(TableName=tableName, Key={'EmailID':{'S':email}})
	
	#3. Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(response)
	
	#4. Return the response object
	return responseObject

