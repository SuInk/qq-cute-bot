# encoding: utf-8
import paho.mqtt.client as mqtt

import config

# Client对象构造
MQTTHOST = config.host_ip
MQTTPORT = 1883
mqttClient = mqtt.Client("hz15AEyKUdF.phone|securemode=2,signmethod=hmacsha256,timestamp=1669307348992|")
mqttClient.username_pw_set(config.user, )


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


def door_open():
    on_mqtt_connect()
    # 系统属性Topic消息上行
    on_publish("/hz15AEyKUdF/phone/user/esp32c3/gate/open", "{\"method\":\"thing.service.property.set\",\"id\":\"1745506903\",\"params\":{\"Status\":1},\"version\":\"1.0.0\"}", 1)

