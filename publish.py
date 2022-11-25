# encoding: utf-8
import paho.mqtt.client as mqtt

import config

# Client对象构造
MQTTHOST = config.host_ip
MQTTPORT = 1883
mqttClient = mqtt.Client(config.client_id)
mqttClient.username_pw_set(config.user, config.passwd)


# 连接MQTT服务器
def on_mqtt_connect():
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.loop_start()

# publish 消息
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)

# 消息处理函数
def on_message_come(lient, userdata, msg):

    print(msg.topic + " " + ":" + str(msg.payload))


# subscribe 消息
def on_subscribe():
    # 订阅监听自定义Topic
    mqttClient.subscribe("/********/pythondevice2/user/update1", 1)
    mqttClient.on_message = on_message_come # 消息到来处理函数


async def door_open():
    on_mqtt_connect()
    # 自定义Topic消息上行
    on_publish("/hz15AEyKUdF/phone/user/esp32c3/gate/open", "{\"id\":\"1\"}", 1)
    on_subscribe()
    while True:
        pass
