from google.protobuf import json_format
import httpx
from ..proto import user_pb2
import logging

def request_api(url, headers, data = None, json = False): # 后面这个json是表明返回是不是json内容
    if isinstance(data,bytes): # 判断是不是二进制数据
        response = httpx.post("https://chat-go.jwzhd.com/v1/user/"+url,headers = headers,data = data)
    else:
        response = httpx.post("https://chat-go.jwzhd.com/v1/user/"+url,headers = headers,json = data)
    response.raise_for_status()
    if not json:
        return response.content
    else:
        return response.json()

class user:
    def __init__(self, token):
        self.token = token
    
    def info(self):
        try:
            headers = {"token": self.token}
            response = httpx.get("https://chat-go.jwzhd.com/v1/user/info",headers = headers)
            response.raise_for_status()
            user_info = user_pb2.info()
            user_info.ParseFromString(response.content)
            user_info = json_format.MessageToDict(user_info)
            return user_info
        except Exception as e:
            logging.error(e)
            return
    
    def get_user(self,user_id: str):
        try:
            headers = {"token": "4a76aaaa-bbbb-cccc-0721-c9dead825555"}
            user = user_pb2.get_user_send()
            user.id = user_id
            data = user.SerializeToString()
            response = request_api("get-user", headers, data = data)
            user_info = user_pb2.get_user()
            user_info.ParseFromString(response)
            user_info = json_format.MessageToDict(user_info)
            return user_info
        except Exception as e:
            logging.error(e)
            return

logging.debug("模块user被导入")