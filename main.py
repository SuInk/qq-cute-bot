#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import asyncio

from flask import Flask, request
from flask_restful import Resource, Api
import cutebot

app = Flask(__name__)

api = Api(app)


class AcceptMes(Resource):

    def post(self):
        # 这里对消息进行分发，暂时先设置一个简单的分发
        msg = request.json
        if msg.get("message_type") == "private":  # 说明有好友发送信息过来
            uid = msg["sender"]["user_id"]  # 获取发信息的好友qq号
            message = msg["raw_message"]  # 获取发送过来的消息
            cutebot.handle_private(uid, message)
        elif msg.get("message_type") == "group": # 说明有群消息发送过来
            group_id = msg["group_id"] # 获取发信息的群号
            message = msg["raw_message"]  # 获取发送过来的消息
            cutebot.handle_group(group_id, message)


api.add_resource(AcceptMes, "/", endpoint="index")
if __name__ == '__main__':
    app.run("0.0.0.0", "5701")  # 注意，这里的端口要和配置文件中的保持一致
