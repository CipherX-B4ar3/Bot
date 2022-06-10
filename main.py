# -*- coding: utf-8 -*-

# = = = = = = = = = = = = = = = = = = [ IMPORTED ] = = = = = = = = = = = = = = = = >

from __future__ import unicode_literals
from pyrogram import Client, filters
from pyrogram.types import Message
import time
from requests import get
import requests
import asyncio, random
import json
from pyrogram.types import InputPhoneContact
import os.path
import pyuseragents
# < = = = = = = = = = = = = = = = = = = = = [ CODE ] = = = = = = = = = = = = = >
Fosh = ["کص ننت","کونی","ننتو گاییدم","کص مادرت","کیرم لا پا ننت زجه نزن","ریدم ت کص مادرت","کص نصلت","ننت زیرمه خارجنده","کیرمی بصیک","بدو نبینمت خارجنده😂😂","کیرم ت کص مردع و زندت\nخارتو میگام زنازاده کیرم لا ممه ننت خارجنده حرومی کیرمو میدم دس ننت ننه فیشری ننه کیر دزد ننه حروم لقمه کیرم ت اولو اخرت کیروم ت قبر مردهات کیرم ت کون بابات ننتو عمودی میگام ننتو رو هوا میگام خارکصه","مادر زنازاده😂","هعیی ننتو گاییدم زجه بزن","توپ تانک فشفشه مادر تو کونکشه","ننتو ع کون گاییدم😂😂","ننتو انال گاییدم ","خارجنده ننت پیشمه","خبری از  خواهرت داری ؟ میدونی دارم میگامش ؟","کیر برع ت مادر کیر پرستت","هعی کص  ناموصت","زجه بزن درت بیارم😂😂","خار کیر دزد","ابجی بچه سالتو گاییدم😂😂","زیرمی زجه بزن","مادرتو یام یام کردم😂😂"]
req = requests.session()
platform = pyuseragents.random()
headers = {"content-type":"application/json","user-agent":platform}
#                          [ SET API HASH ]                           #

admin = "1469547340"

#                          [ SET API HASH ]                           #

proxy = {
	"scheme": "socks5",
	"hostname": "127.0.0.1",
	"port": 9050,
	"username": "",
	"password": ""
 }
app = Client('CipherX',config_file="config.ini")
print('----------------------------------------')
print('\033[37m======>.. \033[32m[  CIPHER-X  ]\033[37m ..<=======')
print('----------------------------------------')
print('\n\033[32mSuccessfully!\n\n\033[0m')

#----------------------------

@app.on_message(filters.me)
async def Bot(c:Client, m:Message):
	try:
		text = m.text

		chat_id = m.chat.id

		user_id = m.from_user.id

		message_id = m.message_id

		reply_id = m.reply_to_message_id

		reply_message = m.reply_to_message

		if text == ".help" or text == ".Help" or text == "Help" or text == "help":
			user = await c.get_me()
			url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
			url2 = get("https://api.codebazan.ir/ping/?url=www.google.com").text

			await m.reply(f"""

	**CIPHER-X** __V1.0.0__ ☠️

	├ • **M**O**D**E** S**e**t**t**i**n**g**s** ↬ (`.mode`)
	├ • **T**oo**l**s** ↬ (`.tools`)
	├ • **E**N**E**`M`**Y** ↬ (`.Enemy`)
	├ • **F**U**`N` ↬ (`.fun`)

	 ᴹᵞ ᴵᴰ [{user.username}](tg://openmessage?user_id={user.id})

	**P**`I`**N**`G` ↬\t`{url2}`**MS** | [{url['result']['time']}](tg://openmessage?user_id={user.id})
	""",quote=True)
		if text == ".fun":
			await m.edit("""
**F**U**N** **L**I**S**T**
`UPDATE Fun LIST`

├ • `update`
├ • `lolo`

				""")
		if text == ".mode" or text == "mode":
			user = await c.get_me()
			url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
			await m.reply(f"""
	**MODE** S**e**T**T**i**N**g**S** | __[{url['result']['time']}](tg://openmessage?user_id={user.id})__

	├ • `.ti  	  | [on] [off] `
	├ • `.echo   | [on] [off] `
	├ • `.for    | [on] [off] `
	├ • `.cot 	  | [on] [off] `
	├ • `.Hyper  | [on] [off] `
	├ • `.kmode  | [on] [off] `
	├ • `.bold 	 | [on] [off] `
	├ • `.mes 	  | [on] [off] `
	├ • `.list   |`   **None**
	├ • `.clear  |`   **None**

	""",quote=True)
		if text == ".Enemy" or text == "Enemy":
			user = await c.get_me()
			url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
			await m.reply(f"""
	**EN**`E`**My** S**e**T**T**i**N**g**S** ☠️ | __[{url['result']['time']}](tg://openmessage?user_id={user.id})__

	├ • `.enemy    | [on] [off] `
	├ • `.senemy   | [id] `
	├ • `.ListEnemy|`   **None**
	├ • `.delenemy |`   **None**
	├ • `.list     |`   **None**
	├ • `.clear    |`   **None**
	""",quote=True)
		if text == ".tools" or text == "tools":
			user = await c.get_me()
			url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
			await m.reply(f"""
	**Tools** S**e**T**T**i**N**g**S**   | __[{url['result']['time']}](tg://openmessage?user_id={user.id})__

	├ •	`.openuser | [id]`
	├ • `.phishing | [site] `
	├ • `.b 	      | [username][Reply] `
	├ • `.un       | [username][Reply] `
	├ • `.ping     | [site] `
	├ • `.font     | [text] `
	├ • `.Shot     | [text] `
	├ • `.i        | [user] `
	├ • `.text     | [text] `
	├ • `.num      | [Number] `
	├ • `.card     | [Number Card] `
	├ • `.join     | [link] `
	├ • `.pin      | [username][Reply] `
	├ • `.upin     | [username][Reply] `
	├ • `.ban      | [username][Reply] `
	├ •	`.id       | [pv] `
	├ • `.v        | [text] `
	├ •	`.ip       | [ip] `
	├ •	`.setbio   | [bio] `
	├ •	`.bomber   | [912^^^^^] `
	├ • `.list     |`   **None**
	├ • `.clear    |`   **None**
	├ • `.date `
	├ • `.bio`
	├ • `.jok` 
	├ • `.FullHelp`	
	""",quote=True)


	#                      [ CIPEHR-X ]                      #

		if text.startswith(".phishing "):
			url = json.loads(get(f"https://api.codebazan.ir/fishinfo/index.php?link={text.replace('.phishing','').strip()}").text)
			time.sleep(0.88)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n{url['t']} ➤ [+]")

		if text.startswith(".bio"):
			url = get("https://api.codebazan.ir/bio/").text
			time.sleep(0.88)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n`{url}` ➤ [+]")

		if text.startswith(".card"):
			url = json.loads(get(f"https://api.codebazan.ir/codemelli/?code={text.replace('.card','').strip()}").text)
			time.sleep(0.88)
			if url["Result"] == "The code is valid":
				URLR = "کد معبر است . "
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n{URLR}")
			else: 
				URLR = "کد نامعبر است . "
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n{URLR}")


		if text.startswith(".b "):
			await c.block_user(text.replace('.b','').strip())
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nBlock {text.replace('.b','').strip()}")

		if text == ".b":
			await c.block_user(chat_id)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nBlock @{m.chat.username}")

		if text.startswith(".un "):
			await c.unblock_user(text.replace('.un','').strip())
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nUnBlock {text.replace('.un','').strip()}")


		elif text == ".un":
			await c.unblock_user(chat_id)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nUnBlock @{m.chat.username}")


		if text.startswith(".ping "):
			url = get(f"https://api.codebazan.ir/ping/?url=www.{text.replace('.ping','').strip()}").text
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nPING ➤ {url}")

		if text.startswith(".date"):
			for i in range(10):
				url = json.loads(get(f"http://api.codebazan.ir/time-date/?json=en").text)
				await m.edit(f"𝕮𝕴text**T**`i`**m**`e` ➤ **{url['result']['time']}**")
		if text.startswith(".i "):
			try:
				url = await c.get_users(text.replace('.i','').strip())
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n[+] **I**`D` ➤ `{url.id}`\n[+] **u**`s`**e**`r` ➤ @{url.username}\n[+] **User** `Bot` ? ➤ {url.is_bot}\n[+] `F``i`**r**`s`**t** `nam`**e** ➤ {url.first_name}\n[+] **S**`t``a``t`**us** ➤ {url.status}\n[+] **d**`c` ➤ {url.dc_id}\n[+] **L**a`s`t **N**am**e**  ➤ {url.last_name}")
			except:
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nUser Not Find\nOr Channel {text.replace('.i','').strip()}")
		elif text == ".i":
			try:
				url = await c.get_users(reply_message.from_user.username)
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n[+] **I**`D` ➤ `{url.id}`\n[+] **u**`s`**e**`r` ➤ @{url.username}\n[+] **User** `Bot` ? ➤ {url.is_bot}\n[+] `F``i`**r**`s`**t** `nam`**e** ➤ {url.first_name}\n[+] **S**`t``a``t`**us** ➤ {url.status}\n[+] **d**`c` ➤ {url.dc_id}\n[+] **L**a`s`t **N**am**e**  ➤ {url.last_name}")
			except:
				pass
		elif text == ".id":
			try:
				url = await c.get_users(chat_id)
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n[+] **I**`D` ➤ `{url.id}`\n[+] **u**`s`**e**`r` ➤ @{url.username}\n[+] **User** `Bot` ? ➤ {url.is_bot}\n[+] `F``i`**r**`s`**t** `nam`**e** ➤ {url.first_name}\n[+] **S**`t``a``t`**us** ➤ {url.status}\n[+] **d**`c` ➤ {url.dc_id}\n[+] **L**a`s`t **N**am**e**  ➤ {url.last_name}")
			except:
				pass
		if text.startswith(".font "):
			url = get(f"https://api.codebazan.ir/font/?text={text.replace('.font','')}").json()
			await m.edit(f"\n".join(list(url["result"].values())[:110]))

		if text.startswith(".text "):
			time.sleep(0.88)
			await c.send_photo(chat_id, f"https://api.codebazan.ir/image/?type=texttopic&text={text.replace('.text','').strip()}",reply_to_message_id=message_id)

		if text.startswith(".Shot "):
			time.sleep(0.88)
			await c.send_photo(chat_id,f"https://api.otherapi.tk/carbon?type=create&code={text.replace('.Shot','').strip()}",reply_to_message_id=message_id)


		if text.startswith(".num "):
			url = json.loads(get(f"https://api.codebazan.ir/num/?num={text.replace('.num','').strip()}").text)
			await app.send_message(chat_id, f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n{url['result']['num']} ➤ [+]")


		if text.startswith(".v "):
			url = json.loads(get(f"https://api.codebazan.ir/vajehyab/?text={text.replace('.v','').strip()}").text)
			time.sleep(0.88)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n[+] Fa ➤ `{url['result']['fa']}`\n[+] En ➤ `{url['result']['en']}`\n[+] Mani ➤ `{url['result']['mani']}`\n[+] Fmoein ➤ `{url['result']['Fmoein']}`")

		if text.startswith(".ip "):
			url = json.loads(get(f"https://api.codebazan.ir/ipinfo/?ip={text.replace('.ip','').strip()}").text)
			time.sleep(0.88)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n[+] IP ➤ {url['ip']}\n[+] CITY ➤ {url['city']}\n[+] ISP ➤ {url['isp']}")


		if text.startswith(".join "):
			await c.join_chat(text.replace('.join','').strip())
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nJoin Group :)")

		if text.startswith(".c "):
			name_group = random.choice(["CipherX","CIPHER-X","CIPHERX","1",'2','3','4','Cqq','aa'])
			await c.create_group(name_group, text.replace('.c','c').strip())
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nCreated Group `{name_group}`")

		if text.startswith(".bomber"):
			number_spam = text.replace(".bomber","").strip()
			open("Tools/NumberSpam","w").write(number_spam)
			await m.edit("**𝕮𝕴**𝕻𝕳`𝕰𝕽-𝖃` ↴ \n**SPAM** `SMS` **RU**__N__...")
			try:
				for i in range(3):
						print("OK")
						req.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",headers=headers,data=dumps({"cellphone": f"+98{number_spam}"}).encode())
						time(4)
						req.post("https://api.divar.ir/v5/auth/authenticate",headers=headers,data=dumps({"phone": f'0{number_spam}'}))
						time(4)
						req.post("https://www.sheypoor.com/api/v10.0.0/auth/send",headers=headers,data=dumps({"username":"0"+number_spam}))
						time(4)
						req.post("https://app.snapp-box.com/api/v2/auth/otp/send",headers=headers,data=dumps({"phoneNumber": "0"+number_spam}))
						time(4)
						req.post("https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",headers=headers,data=dumps({"UserName":"+98"+number_spam}).encode())
						time(4)
						req.post("https://api.toopmarket.com/api/v1/auth/login/number",headers=headers,data=dumps({"mobile":"0"+number_spam}))
						time(4)
						req.post("https://www.filimo.com/api/fa/v1/user/Authenticate/country_code",headers=headers,data=dumps({"mobile":"0"+number_spam,"guid":"ADB3488E-E512-E311-42FF-7EE1DE87F4FA"}).encode())
				await m.edit("𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n**SPAM** __D__`ONE`")
			except:
				print("ERROR SMS BOMBER")



		if text.startswith(".ban "):
			await c.ban_chat_member(chat_id, text.replace('.ban ','').strip())
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nBan Member @{reply_message.from_user.username}")

		elif text.startswith(".ban"):
			await c.ban_chat_member(chat_id, reply_message.from_user.username)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nBan Member @{reply_message.from_user.username}")
		if text == ".pin":
			await app.pin_chat_message(chat_id, reply_id)
			await m.edit("𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**P**`I`**N** `MESSAGE`")
		if text == ".upin":
			await app.unpin_chat_message(chat_id, reply_id)
			await m.edit("𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**UN**`PIN` **MESSAGE**")

		if os.path.exists("Tools/boldmode"):
			mode = open("Tools/boldmode").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.edit(f"**{text}**")
		if text.startswith(".bold "):
			command = text.replace(".bold", "").strip()
			if command == "on"or"off":
				open("Tools/boldmode","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**Bold** **M**O**D**E `{command}`")


		if os.path.exists("Tools/TIMODE"):
			mode = open("Tools/TIMODE").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.edit(f"__{text}__")
		if text.startswith(".ti "):
			command = text.replace(".ti", "").strip()
			if command == "on"or"off":
				open("Tools/TIMODE","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n__TI__ **M**O**D**E `{command}`")

		if os.path.exists("Tools/Kmode"):
			mode = open("Tools/Kmode").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.edit(f"||{text}||")
		if text.startswith(".kmode "):
			command = text.replace(".kmode", "").strip()
			if command == "on"or"off":
				open("Tools/Kmode","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n||K||**MO**`DE` `{command}`")
		if text.startswith(".jok"):
			url = get("https://api.codebazan.ir/jok/").text
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n\n{url}")

		if text.startswith(".for "):
			command = text.replace(".for", "").strip()
			if command == "on"or"off":
				open("Tools/For","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**F**`O`__R__ **M**O**D**E `{command}`")

		if os.path.exists("Tools/tagmode"):
			mode = open("Tools/tagmode").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.edit(f"`{text}`")
		if text.startswith(".cot "):
			command = text.replace(".cot", "").strip()
			if command == "on"or"off":
				open("Tools/tagmode","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n`C`**O**`T` **M**O**D**E `{command}`")
		if os.path.exists("Tools/Hyper"):
			mode = open("Tools/Hyper").read()
		else: 
			mode = "off"
		if mode == "on":
			user = await c.get_me()
			await m.edit(f"[{text}](tg://openmessage?user_id={user.id})")
		if text.startswith(".Hyper "):
			command = text.replace(".Hyper", "").strip()
			if command == "on"or"off":
				open("Tools/Hyper","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n[Hyper](tg://openmessage?user_id=1469547340) **M**O**D**E `{command}`")

		if m.text.startswith(".lock "):
			command = m.text.replace(".lock", "").strip()
			if command == "on"or"off":
				open("Tools/lock","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n`L`**O**`CK` **M**O**D**E `{command} 🔐`")

		if text.startswith(".reply "):
			command = text.replace(".reply","").strip()
			if command == "on"or"off":
				open("Tools/reply","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n`RE`**P**`LY` **M**O**D**E `{command}` 🔐")

		if text.startswith(".senemy "):
			command = text.replace(".senemy", "").strip()
			int(open("Tools/ListEnemy","w").write(command))
			open("Tools/Enemy","a+").write("on")
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n`En`**E**`My` **U**`S`**E**`R` ➤ `{command}` 👾")

		if text.startswith(".openuser "):
			command = text.replace(".openuser", "").strip()
			user = await c.get_users(command)
			link = "tg://openmessage?user_id="
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\nSuccessfully! ✅\n**LI**`NK` ➤ ||[CLICK]({link}{command})||")

		if text.startswith(".enemy "):
			command = text.replace(".enemy","").strip()
			if command == "on"or"off":
				open("Tools/Enemy","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n`En`**E**`My` **M**O**D**E `{command}` 👾 ")	

		if text.startswith(".mes "):
			command = text.replace(".mes","").strip()
			if command == "on"or"off":
				open("Tools/Message","w").write(command)
				open("Tools/ID","w").write(str(chat_id))
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**ME**SS**A**GE** **M**O**D**E `{command}` 🔰 ")	
		if text == "lolo" or text == "لولو":
			await m.edit("""
😐<><><><><><><><><><><><><><><><><><><><><><><>👻
""")
			time.sleep(0.07)
			await m.edit("""
😐<><><><><><><><><><><><><><><><><><><><>👻
		""")
			time.sleep(0.07)
			await m.edit("""
😐<><><><><><><><><><><><><><><><><>👻
		""")
			time.sleep(0.7)
			await m.edit("""
😐<><><><><><><><><><><><><><>👻
		""")

			time.sleep(0.07)
			await m.edit("""
😐<><><><><><><><><><><><👻
		""")
			time.sleep(0.07)
			await m.edit("""
😐<><><><><><><><><>👻
		""")
			time.sleep(0.7)
			await m.edit("""
😐<><><><><><>👻
""")	

			await m.edit("""
😐<><><>👻

		""")
			time.sleep(0.07)
			await m.edit("""
😐<>👻
		""")
			time.sleep(0.07)
			await m.edit("""
😲👻
		""")
		if text.startswith(".delenemy"):
			Lists = open("Tools/ListEnemy").read()
			open("Tools/ListEnemy","w")
			open("Tools/Enemy","w").write("off")
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**E**`N`**E**`M`**Y** `LI`**ST** `DELE`**TED** 👾 ➤ {Lists}")
		if text == "اپدیت" or text == "update":
			await m.edit("""
🟩 **10** %

		""")
			time.sleep(0.07)
			await m.edit("""
🟩🟩 **20** %	
		""")
			time.sleep(0.07)
			await m.edit("""
🟩🟩🟩 **30** %
		""")
			time.sleep(0.7)
			await m.edit("""
🟩🟩🟩🟩 **40** %
		""")

			time.sleep(0.07)
			await m.edit("""
🟩🟩🟩🟩🟩 **50** %
		""")
			time.sleep(0.07)
			await m.edit("""
🟩🟩🟩🟩🟩🟩 **60** %
		""")
			time.sleep(0.7)
			await m.edit("""
🟩🟩🟩🟩🟩🟩🟩 **70** %
		""")

			time.sleep(0.07)
			await m.edit("""
🟩🟩🟩🟩🟩🟩🟩🟩 **80** %	
		""")
			time.sleep(0.07)
			await m.edit("""
🟩🟩🟩🟩🟩🟩🟩🟩🟩 **90** %
		""")
			time.sleep(0.7)
			await m.edit("""
❗️ERROR, Update Failed❗️
		""")


		if "text".startswith(".setbio "):
			command = text.replace(".setbio", "").strip()
			await c.update_profile(bio=command)
			await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\nSuccessfully! ✔️")
		if text.startswith(".clear"):
			a = open("Tools/Enemy","w").write("off")
			b = open("Tools/ListEnemy","w")
			c = open("Tools/lock","w").write("off")
			d = open("Tools/tagmode","w").write("off")
			e = open("Tools/boldmode","w").write("off")
			f = open("Tools/reply","w").write("off")
			g = open("Tools/TIMODE","w").write("off")
			h = open("Tools/Kmode","w").write("off")
			i = open("Tools/Echo","w").write("off")
			j = open("Tools/For","w").write("off")
			k = open("Tools/Hyper","w").write("off")

			await m.edit(f"""
	**AC**__T__`IO`[N](tg://openmessage?user_id=1469547340) **CL**`EA`**R**

	├ • **ENEMY** ➤ `off`
	├ • **LIST ENEMY** ➤ `DELE`**T**__E__**D**
	├ • **LOCK** ➤ `off`
	├ • **TAG** ➤ `off`
	├ • **BOLD** ➤ `off`
	├ • **REPLY** ➤ `off`
	├ • **TI MODE** ➤ `off`
	├ • **K MODE** ➤   `off`
	├ • **EC**`HO` ➤ 	`off`
	├ • **HY**__P__`ER` ➤ `off`
	├ • **F**`O`__R__ ➤ `off`

	""")
		if text.startswith(".ListEnemy"):
			Lists = open("Tools/ListEnemy").read()
			tabdel = int(Lists)
			user = await c.get_users(user_ids=tabdel)
			await m.edit(f"""
			**LI**`ST` __ENE__**MY

			├ • **ID** ➤ `{user.id}`
			├ • **Us**`Er`**NA**`ME` ➤ @{user.username}
			""")
		if text.startswith(".FullHelp"):
			await m.edit("𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\nSuccessfully! ✔️\nPlease....")
			await c.send_document(chat_id, "Tools/HELP.txt",caption="**HELP** `FULL`\nتمام دستورات ربات داخل این فایل هست به زبان فارسی قبل استفاده حتما این فایل رو بخوانید.")
		if text.startswith(".echo "):
			command = text.replace(".echo", "").strip()
			if command == "on"or"off":
				open("Tools/Echo","w").write(command)
				char = "on"if command == "on" else "off"
				await m.edit(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**EC**`HO` **MO**__D__`E` `{command}`")
		if text.startswith(".list"):
			Enemy = open("Tools/Enemy").read()
			ListEnemy = open("Tools/ListEnemy").read()
			lock = open("Tools/lock").read()
			tag = open("Tools/tagmode").read()
			bold = open("Tools/boldmode").read()
			reply = open("Tools/reply").read()
			ti = open("Tools/TIMODE").read()
			Kmode = open("Tools/Kmode").read()
			Hyper = open("Tools/Hyper").read()
			echo = open("Tools/Echo").read()
			fOr = open("Tools/For").read()
			mes = open("Tools/Message").read()
			await m.edit(f"""
	S**e**t**t**i**n**g**s** **AC**`TI`**O**`N`

	├ • **EN**`E`**M**`Y` ➤ `{Enemy}`
	├ • **LO**`CK` ➤     `{lock}`
	├ • **TA**`G` ➤       `{tag}`
	├ • **Bo**`L`**D** ➤    `{bold}`
	├ • **R**`E`**P**`LY` ➤  `{reply}`
	├ • **TI**`MODE` ➤ `{ti}`
	├ • **K** `MODE` ➤ `{Kmode}`
	├ • **EC**`HO` ➤ 	  `{echo}`
	├ • **HY**__P__`ER` ➤ `{Hyper}`
	├ • **F**`O`__R__ ➤      `{fOr}`
	├ • **MES** ➤     `{mes}`
	""")

	except:
		pass
@app.on_message(filters.private)
async def Enemy1(c:Client, m:Message):
	try:
		if os.path.exists("Tools/Enemy"):
			mode = open("Tools/Enemy").read()
		else:
			mode = "off"
		if mode == "on":
			try:
				ListEnemy = open("Tools/ListEnemy").read()
				inter = int(ListEnemy)
				user = m.chat.id
				if user == inter:
					await m.reply(random.choice(Fosh),quote=True)
			except:
				pass 
	except ValueError:
		open("Tools/Enemy","w").write("off")
		await c.send_message("me", f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**EN**`EM`**Y** **o**`f`**f**")
@app.on_message(filters.private)
async def Lock(c:Client, m:Message):
	try:
		if os.path.exists("Tools/lock"):
			mode = open("Tools/lock").read()
		else: 
			mode = "off"
		if mode == "on":
			await c.delete_messages(m.chat.id, m.message_id)
		if os.path.exists("Tools/Echo"):
			mode = open("Tools/Echo").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.copy(m.chat.id)
		if os.path.exists("Tools/For"):
			mode = open("Tools/For").read()
		else: 
			mode = "off"
		if mode == "on":
			await m.forward(m.chat.id)
	except ValueError:
		print("LOCK ERROR")
@app.on_message()
async def Enemy(c:Client, m:Message):
	try: 
		if m.text == "@EBLETSM" or text =="EBLETSM":
			await c.send_video(m.chat.id, "Tools/video/1.mp4",reply_to_message_id=m.message_id)
	except:
		pass
	try:
		if os.path.exists("Tools/Enemy"):
			mode = open("Tools/Enemy").read()
		else:
			mode = "off"
		if mode == "on":
			try:
				ListEnemy = open("Tools/ListEnemy").read()
				inter = int(ListEnemy)
				user = m.from_user.id
				if user == inter:
					await m.reply(random.choice(Fosh),quote=True)
			except:
				pass
	except ValueError:
		open("Tools/Enemy","w").write("off")
		await c.send_message("me", f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴\n**EN**`EM`**Y** **o**`f`**f**")
@app.on_message() 
async def Messages(c:Client,m:Message):
	try:
		if os.path.exists("Tools/Message"):
			mode = open("Tools/Message").read()
		else: 
			mode = "off"
		if mode == "on":
			file = open("Tools/ID").read()
			inter = int(file)
			if m.chat.id == inter:
				print(f"\033[32m=====>\033[37m {m.text}\n")
	except:pass
app.run()
