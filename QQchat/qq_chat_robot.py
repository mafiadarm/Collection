#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           04_11_2018  16:27
    File Name:      /Collection/qq_chat_robot
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    https://github.com/pandolia/qqbot

==============================
"""

import random
import re

from qqbot import QQBotSlot as qqbotslot, RunBot
from run_sqlite import *

__author__ = 'Loffew'


@qqbotslot
def onQQMessage(bot, contact, member, content):
    thme = datetime.datetime.now()
    hour = thme.hour
    reply1 = re.compile(r"@|墨墨|亲亲|亲你|爱你|吃饭|睡觉")
    sentence1 = reply1.findall(content)
    reply2 = re.compile(r"@|墨墨|makelovewithyou")
    sentence2 = reply2.findall(content)

    if member and contact.name == "Empire😘😘":  # and not bot.isMe(contact, member):
        if content == "墨墨":
            socker = random.randint(100, 666)

            if socker == 666:
                bot.SendTo(contact, "@" + member.name + "\n*-❤*-心情美丽-*❤-*\n爱你爱你$^%s^$么么哒\n想和墨墨睡午觉么\nO(∩_∩)O" % (socker, ))

            obj = qq.querySocker(member.name)

            if qq.flag == 1:
                bot.SendTo(contact, "@" + member.name + "\n知道啦知道啦\n\n╭(╯^╰)╮\n\n今天已经打过招呼啦！")
            else:
                bot.SendTo(contact, "@" + member.name + "\n哦哟哟~您来啦~啦啦啦\n给你一个♥(ˆ◡ˆԅ)\n增加了 -* %d *-爱您值哦~\n\n墨墨有 -* %d *- 爱您了呢~！" % (socker, obj[0][1]+socker))

            qq.checkIn(member.name, socker)

        if "@" in sentence1[:2] and "墨墨" in sentence1[:2]:
            if "亲亲" in sentence1 or "亲你" in sentence1:
                if 8 < hour < 12 or 13 < hour < 17 or 19 < hour < 22:
                    bot.SendTo(contact, "mua~mua~mua~mua~")
                    qq.checkIn(member.name, random.randint(5, 10))
            if "爱你" in sentence1:
                if 8 < hour < 12 or 13 < hour < 17 or 19 < hour < 22:
                    bot.SendTo(contact, "❤❤❤❤❤\n  ❤❤❤❤\n    ❤❤❤\n      ❤❤\n        ❤")
                    qq.checkIn(member.name, random.randint(10, 20))
            if "吃饭" in sentence1:
                if 8 <= hour < 9 or 12 <= hour <= 13 or 18 <= hour <= 19:
                    bot.SendTo(contact, "墨墨正咋吃饭呢！❤\n\n喂您一口~啊~~")
                    qq.checkIn(member.name, random.randint(30, 50))
            if "睡觉" in sentence1:
                if hour >= 22:
                    bot.SendTo(contact, "呼~呼~z~z~Z~Z~Z~")
                    qq.checkIn(member.name, random.randint(30, 50))

        if len(sentence2) == 3:
            bot.SendTo(contact, "❤❤❤❤❤❤❤\n\n❤❤ orz ❤❤\n❤❤ owx ❤❤\n\n❤❤❤❤❤❤❤")

        if "rua" in content:
            if hour < 22:
                bot.SendTo(contact, "rua 好长的舌头")
        elif "豆豆" in content:
            if hour < 22:
                bot.SendTo(contact, "吃饭睡觉打^墨墨^~")
        elif content == "签到" :
            bot.SendTo(contact, "@" + "ʚ墨墨ɞ" + "快来啊~有人签到啦")
        elif content == "墨墨❤":
            obj = qq.querySocker(member.name)
            bot.SendTo(contact, "@" + member.name + "墨墨说：%s 代表我的心" % obj[0][1])
        elif "还真的上当了" in content:
            bot.SendTo(contact, "@" + member.name + "骗纸~你个大骗纸！")
        elif "mmp" in content or "MMP" in content:
            bot.SendTo(contact, "@" + member.name + "叫人家干嘛啊？人家不负责签到~但是我会讲笑话哦~")
        elif "笑话" in content:
            bot.SendTo(contact, "@" + member.name + joke.queryJoke())
        elif "美女" in content:
            pass


if __name__ == '__main__':
    joke = Jokes()
    qq = SqliteQQ()
    RunBot()
