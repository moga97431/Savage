import requests
import json
import time
from time import sleep
import random
import sys
import os
idd=("6200075970")
Token=("6905761459:AAEd5KHV4f8DnJissiBaHpRewK0Gr9XS7Lw")




def make():
	
	for i in range(1000):
		sok = "QWERTYUIOPASDFGHJKLZXCVBNM"
		so="QWERTYUIOPASDFGHJKLZXCVBNM_1234567890"
		s = random.choice(sok)
		#amir_0098
		d = random.choice(so)
		f = random.choice(so)
		t = random.choice(so)
		k = random.choice(so)
		user = s+d+f+t+k
		kota = requests.get('https://t.me/'+user)
		messeg=(f"""◆━━━━━◆ ✲ ◆━━━━━◆
✅| New User Telegram 
◆━━━━━◆ ✲ ◆━━━━━◆
🔢| User : @{user}
OBJECT:TELEGRAM
◆━━━━━◆ ✲ ◆━━━━━◆
👨🏻‍💻| Developer : @id_MoDeM
⚒️| Channel : https://t.me/c7A8P6vuqqI4YWU0
◆━━━━━◆ ✲ ◆━━━━━◆""")
		reba = (kota.text)
		if ('name="robots"') in reba:
			requests.post(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={idd}&text='+messeg)
			print('\033[32m OK TeLeGrAm: '+user)
		else:
			print('\033[31m NO TeLeGrAm: '+user)
		kota = requests.get('https://instagram.com/'+user)
		messeg=(f"""◆━━━━━◆ ✲ ◆━━━━━◆
✅| New User INSTAGRAM
◆━━━━━◆ ✲ ◆━━━━━◆
🔢| User : @{user}
OBJECT:INSTA
◆━━━━━◆ ✲ ◆━━━━━◆
👨🏻‍💻| Developer : @id_MoDeM
⚒️| Channel : https://t.me/c7A8P6vuqqI4YWU0
◆━━━━━◆ ✲ ◆━━━━━◆""")
		reba = (kota.text)
		if ('name="robots"') in reba:
			requests.post(f'https://api.telegram.org/bot{Token}/sendMessage?chat_id={idd}&text='+messeg)
			print('\033[32m OK iNsTa: '+user)
		else:
			print('\033[31m NO iNsTa:'+user)
sleep(4)
make()
sleep(4)
#amir_0098
#xp_media
