import httpx
from .. import config
from google.protobuf import json_format

def request_api(url, headers = None , data = None, json = False): # 后面这个json是表明返回是不是json内容
    if isinstance(data,bytes): # 判断是不是二进制数据
        response = httpx.post("https://chat-go.jwzhd.com/v1/"+url,headers = headers,data = data)
    else:
        response = httpx.post("https://chat-go.jwzhd.com/v1/"+url,headers = headers,json = data)
    response.raise_for_status()
    if not json:
        return response.content
    else:
        return response.json()

class conversation:
    from ..proto import conversation_pb2

    def __init__(self, token):
        self.token = token
    
    def dismiss_notification(self, chat_id: str):
        headers = {"token": self.token}
        payload = {"chatId": chat_id}
        response = request_api("conversation/dismiss-notification", headers, data = payload, json = True)
        return response
    
    def list(self):
        headers = {"token": self.token}
        response = request_api("conversation/list", headers)
        list = self.conversation_pb2.list()
        list.ParseFromString(response)
        list = json_format.MessageToDict(list)
        return list