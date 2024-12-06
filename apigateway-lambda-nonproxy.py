import json

def lambda_handler(event, context):
    print('event :' + json.dumps(event, indent=2))

    if (event['RequestPayload']):
        payLoad = event['RequestPayload']

        if (payLoad['QueryParam']):
            queryParam = payLoad['QueryParam']
            print('Query Parameter : ' + json.dumps(queryParam))

        if (payLoad['Headers']):
            headers = payLoad['Headers']
            print('Header : ' + json.dumps(headers))

        if (payLoad['Data']):
            allData = payLoad['Data']
            customerData = allData['Customer']
            print('Customer Details : ' + json.dumps(customerData))
            VehicleData = allData['Vehicle']
            print('Vehicle Details :' + json.dumps(VehicleData))

    response = {'Status': 'Ok',
                'Message': "Non-Proxy Integration Processed"
                }

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
