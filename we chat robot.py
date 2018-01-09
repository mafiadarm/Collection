from wxpy import *
# bot = Bot(cache_path=True)   # 实例化，并登录微信
# tuling = Tuling(api_key='6c6f623861db4f5ca0ed59ad509c69f6')  # 调用图灵机器人API
# @bot.register()
# def auto_reply(msg):
#     tuling.do_reply(msg)
# embed()

# 单独和某人聊天
bot = Bot(cache_path=True)  # 实例化，并登录微信
my_friend = ensure_one(bot.search(u'࿉ ᒑ ༏ 倪 悦.'))  # 查找到要使用机器人来聊天的好友
tuling = Tuling(api_key='b6a51bd00f054c82a1510d083ac8da49')  # 调用图灵机器人API
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)
embed()

# http://www.tuling123.com
# 1105884536