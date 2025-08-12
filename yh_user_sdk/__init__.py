# __init__.py
from .core import user # 自动获得所有延迟加载模块

class set_token:
    def __init__(self, token = None):
        self.token = token
    
    @property
    def user(self):
        from .core.user import user  # 延迟加载
        return user(self.token)
    
    @property 
    def msg(self):
        from .core.msg import msg
        return msg(self.token)