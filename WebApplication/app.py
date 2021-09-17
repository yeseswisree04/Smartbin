
from flask import Flask, render_template
from flask import request
import paho.mqtt.client as mqtt_client
from flask_sqlalchemy import SQLAlchemy
from Telegram import sendTelegram 
import pandas as pd



import time

app = Flask(__name__)


database = {'Bin ID':['B1','B2','B3'],
      'Bin Status':['EMPTY','EMPTY','EMPTY'],
      'Driver ID':['D1','D2','D3'],
      'Driver ChatID':['@Smartbin1','@Smartbin2','@Smartbin3'],
      'Driver Contact':['bot1925206689:AAEtSxswtMrbicRhJCJeYgimZs6B8WzY9Vc','bot2043471254:AAGgD6tHJW2DjSLP5w4zXQ4FXBtdlmoruIU','bot2038238671:AAEXTO6fNXzgG3DUBntyVnZy1At0tRkZG1w'],
      'Work Status':['COMPLETED','COMPLETED','COMPLETED'],
     'GMaps Link':['GPS1','GPS2','GPS3']}

global df

df = pd.DataFrame(database)
df = df.set_index('Bin ID')


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



# @app.route('/update', methods=['POST', 'GET'])
# def update():
#     global smartbin
#     global smartbin_dic
#     global bin_id
#     global bin_status
#     global work_status
#     global gmap_link

#     smartbin = request.get_data()
#     smartbin = smartbin.decode('utf-8')

#     print(smartbin)

#     bin_id, bin_status, work_status = smartbin.split(' ')
#     smartbin_dic[bin_id] = [bin_status,work_status]

#     return ''


@app.route('/update1', methods=['POST', 'GET'])
def update():
    global smartstring
    global bin_id
    global bin_status
    global work_status
    global gmap_link

    smartstring = request.get_data()
    smartstring = smartstring.decode('utf-8')

    bin_id, bin_status, work_status, gmap_link = smartstring.split(' ')

    if bin_status == 'FILLED':
        print(bin_id + ' FILLED')
        sendTelegram(df.loc[bin_id,'Driver ChatID'],df.loc[bin_id,'Driver Contact'], 'The Bin is FULL!!')
        sendTelegram(df.loc[bin_id,'Driver ChatID'],df.loc[bin_id,'Driver Contact'],gmap_link)

        work_status='CONTACTED'
    else: work_status='COMPLETED'

    df.loc[bin_id,:] = {'Bin Status': bin_status,'Driver ID':df.loc[bin_id,'Driver ID'],'Driver ChatID':df.loc[bin_id,'Driver ChatID'],'Driver Contact':df.loc[bin_id,'Driver Contact'],'Work Status':work_status,'GMaps Link':gmap_link}

    return ''

@app.route('/data', methods = ['POST','GET'])
def data():
        # 
       
        return render_template('Hello.html', data = df.to_html())
        # else:
        #     return render_template('Hello.html', bin_status = bin_status, work_status = work_status)

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