import qrtools, pyqrcode, sys, os
from qrtools import QR

def scan():
 os.system('clear')
 a=('+'*50)
 print('\033[1;37m'+a+'\n\t    \033[1;36m     QR Code \033[1;37m[ \033[1;36mScan \033[1;37m]\n'+a)
 print('\nGenerate \033[1;32mQR Code ')
 code=raw_input(' \033[1;37mInput Image :\033[1;32m ')

 cd=QR(filename=code)

 if cd.decode():
  dat=cd.data
  data=pyqrcode.create(dat)
  print(data.terminal(quiet_zone=1))
  print '\n \033[1;32mResult : \n \033[1;37m'+dat



def gen():
 os.system('clear')
 a=('+'*50)
 print('\033[1;37m'+a+'\n\t      \033[1;36m QR Code \033[1;37m[ \033[1;36mGenerate \033[1;37m]\n'+a)
 print('\nGenerate \033[1;32mQR Code ')
 code=raw_input(' \033[1;37mInput Text :\033[1;32m ')
 nam=raw_input(' \033[1;37m Save As : \033[1;32m')
 cd=pyqrcode.create(code)
 cre=(nam)
 cd.png(cre,scale=4)
 print(cd.terminal(quiet_zone=1))


def help():
 os.system('clear')
 a=('+'*55)
 print('\033[1;37m'+a+'\n\t\t    \033[1;36mQR Code \n\t       \033[1;36mGenerate \033[1;37mAnd \033[1;36mScan\033[1;37m')
 print('\n'+a+'\033[1;33m\n\tIf U Dont Know How To Use This Program, \n\tU can see \033[1;31mREADME.md \033[1;33mand read it ^_\n\033[1;37m'+a)



def menu():
 os.system('clear')
 a=('+'*50)
 print('\033[1;37m'+a+'\n\t\t    \033[1;36mQR Code \n\t       \033[1;36mGenerate \033[1;37mAnd \033[1;36mScan\n\033[1;37m'+a)
 print('''
 \033[1;37m1 \033[1;33m= \033[1;37mGenerate \033[1;32mQR Code
 \033[1;37m2 \033[1;33m= \033[1;37mScan \033[1;32mQR Code
 \033[1;37m3 \033[1;33m= \033[1;35mHelp
 ''')
 pil=int(input(' \033[1;37mChoose : '))
 if pil == 1:
  gen()
 elif pil == 2:
  scan()
 elif pil == 3:
  help()
menu()



