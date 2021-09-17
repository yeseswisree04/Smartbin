
from flask import Flask, render_template
from flask import request
import paho.mqtt.client as mqtt_client
from flask_sqlalchemy import SQLAlchemy

import time

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def hello():
    global test

    test = request.get_data()
    test = test.decode('utf-8')
    print('{}'.format(test))
    return 'Output is: {}'.format(test)

@app.route('/h')
def value():
        return test

@app.route('/data')
def data():
        return render_template('Hello.html', message = test)

if __name__ == '__main__':
    app.debug = True
    app.run()


















    # #Function to connect
# def connect_mqtt():
#         def on_connect(client, userdata, flags, rc):
#             if rc == 0:
#                 print("Connected to MQTT Broker!")
#             else:
#                 print("Failed to connect, return code %d\n", rc)

#     client = mqtt_client.Client(client_id)
#     client.username_pw_set(username, password)
#     client.on_connect = on_connect
#     client.connect(broker, port)
#     return client

# #Function to publish message to MQTT Broker
# def publish(client,message):
#         msg_count = 0

#         time.sleep(1)
#         result = client.publish(topic, message)
#         # result: [0, 1]
#         status = result[0]
#         if status == 0:
#             print(f"Send `{message}` to topic `{topic}`")
#         else:
#             print(f"Failed to send message to topic {topic}")
#         msg_count += 1

# @app.route('/')
# def hello_world():


#     mqtt_client = connect_mqtt()
#     publish(mqtt_client,'Yo Bros This is Awesome')

#     return 'Hello from SmartRoom!'

# @app.route('/ifttt', methods=['POST','GET'])
# def handler():
#     global SmartRoom_json
#     SmartRoom_State = request.get_data()
#     SmartRoom_json['SmartRoom_State']=SmartRoom_State
#     print('Smart Room state is : {}'.format(SmartRoom_State))
#     return ''

# @app.route('/SmartRoom')
# def SmartRoom():
#     return SmartRoom_json

# if __name__ == "__main__":
#     app.run(host='0.0.0.0')