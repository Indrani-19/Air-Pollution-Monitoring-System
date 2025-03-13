import json
import boto3
from pynput import keyboard
import requests
import json
import time

# set up the AWS client with the correct region
region_name = 'us-east-1'
client = boto3.client('sns', region_name=region_name)


a = 0
b = 0
c = 0

THRESHOLD = 5

def on_press(key):
    global a, b, c
    if key == keyboard.Key.up:
        a += 1
    elif key == keyboard.Key.down:
        a -= 1
    elif key == keyboard.Key.left:
        b += 1
    elif key == keyboard.Key.right:
        b -= 1
    elif key == keyboard.KeyCode(char='a'):
        c += 1
    elif key == keyboard.KeyCode(char='s'):
        c -= 1

def on_release(key):
    pass

def send_payload_to_lambda(payload):
    # Create a boto3 client for AWS Lambda
    client = boto3.client('lambda')
   
    # Create a dictionary with the payload
    data = {'payload': payload}
   
    # Convert the dictionary to a JSON string
    payload = json.dumps(data)
   
    # Invoke the Lambda function with the JSON payload
    response = client.invoke(FunctionName='IOTProject', Payload=payload)
   
    # Print the response from Lambda
    print(response['Payload'].read())

def send_email_notification(payload):
    # Create a boto3 client for SNS
    client = boto3.client('sns',region_name=region_name)
   
    # Create a message for the email
    message = f"Alert: {payload}"
   
    # Publish the message to the SNS topic
    response = client.publish(TopicArn='arn:aws:sns:us-east-1:514663767995:IOTEmail', Message=message)
   
    # Print the response from SNS
    print(response)

#Harshal Arun Yeole
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    while True:
        print("CO:", a, "CO2:", b,"AQI:",87, "gas leak:", c)
        if a >= THRESHOLD or b >= THRESHOLD or c >= THRESHOLD:
            payload = {"serialNumber":"000","AQI": a, "CO": b, "CO2": c}
           
            if a >= THRESHOLD or b >= THRESHOLD or c >= THRESHOLD:
               
                payload = {'CO': a, 'C02': b, 'AQI':87 ,'gas leakage': c}
                headers = {'Content-Type': 'application/json'}
                url = 'https://wj7vblxcwd.execute-api.us-east-1.amazonaws.com/default/FinalIoTProject'

                try:
                    response = requests.post(url, headers=headers, data=json.dumps(payload))
                    response.raise_for_status()
                    print('Payload sent successfully')
                except requests.exceptions.HTTPError as err:
                    break
