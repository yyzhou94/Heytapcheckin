# -*- coding: utf-8 -*-

import smtplib,traceback,os,requests,urllib,json
from email.mime.text import MIMEText


def sendEmail(email,content):
    try:
        #要发送邮件内容

        #接收方邮箱
        receivers = email
        #邮件主题
        subject = '欢太商城'
        param1 = '?address=' + receivers + '&name=' + subject + '&certno=' + content
        param2 = '?to=' + receivers + '&title=' + subject + '&text=' + content
        res1 = requests.get('http://liuxingw.com/api/mail/api.php' + param1)
        res1.encoding = 'utf-8'
        res1 = res1.json()
        if res1['Code'] == '1':
            print(res1['msg'])
        else:
            #备用推送
            requests.get('https://email.berfen.com/api' + param2)
            print('email push BER')
            #这里不知道为什么，在很多情况下返回的不是 json，
            # 但在测试过程中成功率极高,因此直接输出
    except Exception as e:
        print('邮件推送异常，原因为: ' + str(e))
        print(traceback.format_exc())

#钉钉群自定义机器人推送
def sendDing(webhook,content):
    try:
        data = {
            'msgtype': 'markdown',
            'markdown': {
                'title': '欢太商城',
                'text': content
            }
        }
        headers = {
            'Content-Type': 'application/json;charset=utf-8'
        }
        res = requests.post(webhook,headers=headers,json=data)
        res.encoding = 'utf-8'
        res = res.json()
        print('dinngTalk push : ' + res['errmsg'])
    except Exception as e:
        print('钉钉机器人推送异常，原因为: ' + str(e))
        print(traceback.format_exc())

#发送Tg通知
def sendTg(tgToken,tgUserId,apihost,content):
    try:
        token = tgToken
        chat_id = tgUserId
        tghost = apihost
        #发送内容
        data = {
            '欢太商城':content
        }
        content = urllib.parse.urlencode(data)
        #TG_BOT的token
        #token = os.environ.get('TG_TOKEN')
        #用户的ID
        #chat_id = os.environ.get('TG_USERID')
        if tghost == None:
            url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={content}'
        else:
            url = f'https://{tghost}/bot{token}/sendMessage?chat_id={chat_id}&text={content}'
        session = requests.Session()
        resp = session.post(url)
        print(resp)
    except Exception as e:
        print('Tg通知推送异常，原因为: ' + str(e))
        print(traceback.format_exc())

#发送push+通知
def sendPushplus(token,content):
    try:
        #发送内容
        content = content.replace("\n", "<br>")
        data = {
            "token": token,
            "title": "欢太商城",
            "content": content
        }
        url = 'http://www.pushplus.plus/send'
        headers = {'Content-Type': 'application/json'}
        body = json.dumps(data).encode(encoding='utf-8')
        resp = requests.post(url, data=body, headers=headers).json()
        print('Pushplus send : ' + resp['msg'])
    except Exception as e:
        print('push+通知推送异常，原因为: ' + str(e))
        print(traceback.format_exc())

#企业微信通知，普通微信可接收
def sendWechat(wex_id,wex_secret,wx_agentld,content,thumb_media_id=''):
    #获得access_token
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    token_param = '?corpid=' + wex_id + '&corpsecret=' + wex_secret
    token_data = requests.get(url + token_param)
    token_data.encoding = 'utf-8'
    token_data = token_data.json()
    access_token = token_data['access_token']
    #发送内容
    html = content.replace("\n", "<br/>")
    #创建要发送的消息
    if thumb_media_id:
        data = {
            "touser": "@all",
            "msgtype": "mpnews",
            "agentid": wx_agentld,
            "mpnews": {
                "articles": [
                    {
                        "title": "欢太商城",
                        "thumb_media_id": thumb_media_id,
                        "author": "签到小助手",
                        "content_source_url": "",
                        "content": html,
                        "digest": content
                    }
                ]
            }
        }
    else:
        data = {
        "touser": "@all",
        "msgtype": "text",
        "agentid": wx_agentld,
        "text": {"content": content}
    }
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    message = requests.post(send_url,json=data)
    message.encoding = 'utf-8'
    res = message.json()
    print('Wechat send : ' + res['errmsg'])

