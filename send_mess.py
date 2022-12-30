import requests
class Send_mess:
    def __init__(self,cookies) -> None:
        self.cookies=cookies
    def Check_live_uid(self):
        self.headers = {
            'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': self.cookies,
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        }
        response = requests.get('https://mbasic.facebook.com/', headers=self.headers).text
        try:
            self.id_acc = self.cookies.split('c_user=')[1].split(';')[0]
            self.fb_dtsg = response.split('name="fb_dtsg" value="')[1].split('"')[0]
            self.jazoest = response.split('name="jazoest" value="')[1].split('"')[0] 
            self.eav = response.split('eav=')[1].split('"')[0]
            return True
        except:
            return False
    def send(self,uid,content):
        params = {
            'icm': '1',
            'eav': self.eav,
            'paipv': '0',
        }
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'body': content,
            'send': 'Gửi',
            'tids': f'cid.c.{uid}:{self.id_acc}',
            'wwwupp': 'C3',
            f'ids[{uid}]': f'{uid}',
        }
        response = requests.post('https://mbasic.facebook.com/messages/send/', params=params,headers=self.headers, data=data)
        if 'send_succes' in response.text:
            return True
        else:
            return False
#cookies acc cần send message (cookies)
cookies = ''
#id mess đối tác (uid)
uid = '' 
#nội dung tin nhắn (content)
content = '''happy new year!
Năm mới như con cac nhaaaa! <3'''
p = Send_mess(cookies)
if p.Check_live_uid() == False:#kiểm tra tài khoản live hay die và get info trả kết quả true false
    quit('Facebook Cookie ERROR')
if p.send(uid,content) == True:#gửi tin nhắn với uid và nội dung
    print('Message Sent Successfully')
else:
    print('Message Sent Failed')

      