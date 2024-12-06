import json

def lambda_handler(event, context):
    print(event)

    if (event['queryStringParameters']):
        queryParam = event['queryStringParameters']
        print('Query parameter : ' + json.dumps(queryParam))

    if (event['headers']):
        headers = event['headers']
        print('Headers : ' + json.dumps(headers))

    if (event['body']):
        # convert JSON formatted string to python object as dict
        payLoad = json.loads(event['body'])
        print('Body :' + json.dumps(payLoad, indent=2))

        customerData = payLoad['Data']['Customer']
        print('Customer Details : ' + json.dumps(customerData))

        VehicleData = payLoad['Data']['Vehicle']
        print('Vehicle Details :' + json.dumps(VehicleData))

    response = {'Status': 'Ok',
                'Message': "Proxy Integration Processed"
                }
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
