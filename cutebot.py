import asyncio
import httpx
import publish
from datetime import datetime


def handle_private(uid, message):  # 处理私聊信息
    if message == "/开门":  # 简单的判断，只是判断其是否为空
        # print(message)
        asyncio.run(send_private(uid, f"好喜欢你🥰"))
        asyncio.run(publish.door_open())
    else:
        asyncio.run(send_private(uid, "喜欢你🥰"))


def handle_group(group_id, message):  # 处理私聊信息
    if message == "/开门":  # 判断是否为开门指令
        asyncio.run(send_group(group_id, f"好喜欢你🥰"))
        asyncio.run(publish.door_open())
    else:
        pass


async def send_private(uid, message, gid=None):
    """
    用于发送消息的函数
    :param uid: 用户id
    :param message: 发送的消息
    :param gid: 群id
    :return: None
    """
    async with httpx.AsyncClient(base_url="http://127.0.0.1:5700") as client:
        if gid is None:
            # 如果发送的为私聊消息
            print(uid, message)
            params = {
                "user_id": uid,
                "message": message,
            }
        await client.get("/send_private_msg", params=params)


async def send_group(group_id, message, gid=None):
    """
    用于发送消息的函数
    :param group_id:
    :param message: 发送的消息
    :param gid: 群id
    :return: None
    """
    async with httpx.AsyncClient(base_url="http://127.0.0.1:5700") as client:
        if gid is None:
            # 如果发送的为私聊消息
            print(group_id, message)
            params = {
                "group_id": group_id,
                "message": message,
            }
        await client.get("/send_group_msg", params=params)
