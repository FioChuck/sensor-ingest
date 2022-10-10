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

    input_str = str(request.get_data())

    processingtime = str(datetime.now())  # declare processing time

    # calculate embedded docs
    station_doc = str_to_dict(input_str, processingtime)

    publish(station_doc)

    return 'success'
