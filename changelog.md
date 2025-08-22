### 0.1.9
修正 msg 的 button_report 对按钮值的变量命名.  
新增 bot 的 info, bot_group_list  
新增 group.tag 的 member(s)

### 0.1.8
更新群云盘相关接口的SDK.  

### 0.1.7
添加超时时间设定,需要在初始化时设定 timeout 参数,当前版本部分模块默认超时时间(没写的是没超时时间设定的参数):  

|模块名|默认超时时间|
|--------|---------------|
|msg|60s|
|group|10s|

更新 user.proto, 加入解封时间相关描述.  
更新 web.py, 加入部分接口.  