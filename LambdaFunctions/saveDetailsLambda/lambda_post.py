import boto3
import json

dynamodb = boto3.client('dynamodb')
tableName = "CustomerDetails"

def lambda_handler(event, context):
    
	#1. Parse out query string params
	email = event['EmailID']
	first_name = event['FirstName']
	last_name = event['LastName']
	
	#2. Create Put query to DynamoDB
	response = dynamodb.put_item(
	    TableName=tableName, 
	    Item={
	        'LastName':{'S':last_name},
	        'FirstName':{'S':first_name},
	        'EmailID':{'S':email}
	    }
	)
	
	#3. Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = "Success"
	
	#4. Return the response object
	return responseObject
