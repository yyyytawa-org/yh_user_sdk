import httpx
import logging
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

class conversation: # 对话列表
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

class misc:
    def __init__(self, token = None): # 初始化
        self.token = token

    def request_api(self, url, headers = None):
        if not headers:
            headers = {"token": self.token}
        transport = httpx.HTTPTransport(retries = 3)
        with httpx.Client(transport = transport, base_url = "https://chat-go.jwzhd.com/v1/misc/") as client:
            response = client.get(url, headers = headers)
            response.raise_for_status()
            return response.json()
    
    def configure_distribution(self):
        response = self.request_api("configure-distribution")
        return response
    
    def qiniu_token(self, type: str):
        type2url = { # 转 URL 的字典
            "image": "qiniu-token",
            "audio": "qiniu-token-audio",
            "file": "qiniu-token2",
            "video": "qiniu-token-video",
            "group_disk": "qiniu-token-group-disk"
        }
        url = type2url.get(type)
        if not url:
            logging.error(f"输入的 {type} 无效")
            return
        response = self.request_api(url)
        return response

    def setting(self):
        response = self.request_api("setting")
        return response

    def gray_status(self): # 没用的东西+1
        response = self.request_api("gray-status", headers = {"token": "114514"})
        return response