import httpx
from google.protobuf import json_format
from ..proto import group_pb2
import logging

def request_api(url, headers = None , data = None, json = False): # 后面这个json是表明返回是不是json内容
    if isinstance(data,bytes): # 判断是不是二进制数据
        response = httpx.post("https://chat-go.jwzhd.com/v1/group/"+url,headers = headers,data = data, timeout = 60)
    else:
        response = httpx.post("https://chat-go.jwzhd.com/v1/group/"+url,headers = headers,json = data, timeout = 60)
    response.raise_for_status()
    if not json:
        return response.content
    else:
        return response.json()

def status_only(data): # 专门负责解只有一种status的情况
    status = group_pb2.edit_group()
    status.ParseFromString(data)
    status = json_format.MessageToDict(status)
    return status

class group:
    def __init__(self, token = None):
        self.token = token
    
    def info(self, group_id: str):
        headers = {"token": self.token}
        request = group_pb2.info_send()
        request.group_id = group_id
        payload = request.SerializeToString()
        response = request_api("info", headers, data = payload)
        group_info = group_pb2.info()
        group_info.ParseFromString(response)
        group_info = json_format.MessageToDict(group_info)
        return group_info
    
    def list_member(self, group_id: str, size = 50, page = 1):
        headers = {"token": self.token}
        request = group_pb2.list_member_send()
        request.group_id = group_id
        request.data.size = int(size)
        request.data.page = int(page)
        payload = request.SerializeToString()
        response = request_api("list-member", headers, data = payload)
        member = group_pb2.list_member()
        member.ParseFromString(response)
        member = json_format.MessageToDict(member)
        return member
    
    def edit_group(self, group_id: str, data = {}):
        headers = {"token": self.token}
        group_info = self.info(group_id)
        if group_info.get("status", {}).get("code") != 1:
            logging.error(group_info.get("status").get("msg"))
            return group_info
        group_data = group_info["data"]
        info_send = {
            "group_id": group_id,
            "name": group_data.get("name", ""),
            "introduction": group_data.get("introduction", ""),
            "avatar_url": group_data.get("avatarUrl", ""),
            "direct_join": group_data.get("directJoin", 0),
            "history_msg": group_data.get("historyMsg", 0),
            "category_name": group_data.get("categoryName", ""),
            "category_id": group_data.get("categoryId", 0),
            "private": group_data.get("private", 0)
        }
        info_send.update(data)
        request = group_pb2.edit_group_send()
        json_format.ParseDict(info_send, request, ignore_unknown_fields=False)
        payload = request.SerializeToString()
        response = request_api("edit-group", headers, data = payload)
        status = status_only(response)
        return status