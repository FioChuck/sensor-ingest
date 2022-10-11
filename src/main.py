from functions.sensor_prep import *
from datetime import datetime
import json
from google.cloud import pubsub_v1
import os


def main(request):

    publisher = pubsub_v1.PublisherClient()

    GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')

    def publish(data):

        TOPIC_NAME = os.getenv('TOPIC_NAME')
        topic_path = publisher.topic_path(GCP_PROJECT_ID, TOPIC_NAME)

        message_json = json.dumps(data)
        message_bytes = message_json.encode('utf-8')

        try:
            publish_future = publisher.publish(topic_path, data=message_bytes)
            publish_future.result()
            return 'Message published.'
        except Exception as e:
            print(e)
            return (e, 500)

    # input_str = str(request.get_data())
    input_str = "b'PASSKEY=84DF7E47EB8EA73923151F15GA4DB898&stationtype=GW1100B_V2.0.6&dateutc=2022-08-24+23:53:53&tempinf=74.8&humidityin=49&baromrelin=29.034&baromabsin=29.034&soilmoisture1=28&soilmoisture2=29&soilmoisture3=18&soilbatt1=1.2&soilbatt2=1.3&soilbatt3=1.3&freq=915M&model=GW1100B"

    processingtime = str(datetime.now())  # declare processing time

    # calculate embedded docs
    station_doc = str_map_emb(input_str, processingtime)

    publish(station_doc)

    return 'success'
