import requests

r=requests.get('https://www.fast2sms.com/dev/bulk?authorization=FPYnw1x9CrHcIk6R3AqTpOeZzvi85lQyjLa4dDJgMGVmf02suKFjdvKuCfeWxa8oY59y6Xw1b3R7UlJH&sender_id=FSTSMS&message=Thisistestmessage&language=english&route=p&numbers=9154023236')

print(r.status_code) 
