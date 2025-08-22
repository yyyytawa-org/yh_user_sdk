import yh_user_sdk as sdk
# from yh_user_sdk.core.other import bot

client = sdk.set_token("YOUR_TOKEN")

# 获取机器人信息
print(client.bot.info("76965303")) # bot id

# 获取自己创建的所有机器人信息
print(client.bot.bot_group_list())