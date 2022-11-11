import boto3
import json
import time
import csv
import random
import datetime
from datetime import timedelta

with open("secret.json") as f:
        SECRET = json.load(f)

with open("config.json") as f:
        CONFIG = json.load(f)

clientkinesis = boto3.client('kinesis', region_name = CONFIG["Region"], aws_access_key_id = SECRET["AWSAccessKeyId"], aws_secret_access_key = SECRET["AWSSecretKey"])

id = 0

while True:
        sensor = {}
        sensor["id"] = str(id)
        sensor["location"] = "kitchen"
        sensor["termometer_sensor"] = "termometer"
        sensor["termometer_value"] = random.randint(25, 35)
        sensor["humidity_sensor"] = "humidity"
        sensor["humidity_value"] = random.randint(30, 45)
        sensor["time"] = str(datetime.datetime.now())
        id += 1
        time.sleep(CONFIG["Frequency"])
        response = clientkinesis.put_record(StreamName=CONFIG["KinesisDataStreamName"], Data=json.dumps(sensor), PartitionKey=str(id))

        print("Id:" + str(id) + ", ReqID:" + response['ResponseMetadata']['RequestId'] + ",HTTPStatusCode:" + str(response['ResponseMetadata']['HTTPStatusCode']))
