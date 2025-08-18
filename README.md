# 云湖用户API SDK
云湖用户API的SDK  
用法建议扒源码,文档还没写.  
由于项目的特殊性可能会随时停更.  
由于 ProtoBuf 官方的有病行为,导致其本 SDK 返回字典中所有在 proto 文件中定义为 int64 的数字都会变成str.无解(除非换第三方库来解proto).  
推荐使用下划线命名法 (例如 msg_id) 避免出现一些潜在问题.  
本项目最低 Python 版本要求为 3.12, 低于 3.12 版本的无法运行.  
tool 的部分代码参考了第三方仓库.详情见 tool 的注释.  

## 参与贡献
> 确保你的系统已经正确安装了 `uv` 和 `git` 然后通过下方操作开始项目贡献

### 1. 克隆项目

```bash
git clone https://github.com/yyyytawa-org/yh_user_sdk
cd yh_user_sdk
```

### 2. 环境搭建

使用 uv 同步项目环境:

```bash
uv sync

# 激活虚拟环境
source .venv/bin/activate   # macOS/Linux
# Windows: .venv\Scripts\activate
```

### 3. 安装sdk

```bash
uv pip install -e .
```
