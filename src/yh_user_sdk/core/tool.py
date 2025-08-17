import httpx
from .other import misc
import logging

class tool:
    def __init__(self, token = None):
        self.token = token

    def upload(self, type, file: bytes, name = None):
        """
        上传文件,部分代码参考了114514个三连的脚本
        """
        import hashlib
        try:
            type2bucket_name = {
                "file": "chat68-file",
                "image": "chat68",
                "audio": "chat68-file",
                "video": "chat68",
                "group_disk": "chat68-file"
            }
            client = misc(self.token)
            utoken = client.qiniu_token(type)["data"]["token"]
            uhost = httpx.get(f"https://api.qiniu.com/v4/query?ak={utoken.split(':')[0]}&bucket={type2bucket_name.get(type,'chat68-file')}").json()["hosts"][0]["up"]["domains"][0]
            # 三连两行解决战斗,可读性去世.
            if not name:
                md5 = hashlib.md5(file)
                name = md5.hexdigest()
            params = {
                "token": (None, utoken),
                "key": (None, name),
                "file": (name, file)
            }
            response = httpx.post("https://"+uhost, files=params)
            return response.json()
        except Exception as e:
            logging.error(f"发生错误 {e}")