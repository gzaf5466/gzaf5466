class train:

    def __init__(self,name,fare,seat,time):
        self.name =name
        self.fare =fare
        self.seat =seat
        self.time =time
    def getinfo(self):
        print(f'                    here is details for {self.name}')
        print(f'                    the fare is {self.fare}')
        print(f'                    available seats {self.seat}')
        print(f'                    departure of train {self.time}')
    def ticketcancel(self):
        canceltket=input('do u want to cancel a your ticket \nenter your ticket numer\n')
        if canceltket==cancelrandom:
            print('your ticket is succesfully canceled')
        else:
            print('you have enterd an incorrect ticketnumber')
    def ticketnumber():
        ticketno = cancelrandom
from array import typecodes
import random
cancelrandom=random.randint(0,500)
randno2 =random.randint(0,9)
randno3 =random.randint(0,9)
randno4 =random.randint(0,9)
code1 = [randno2,randno3,randno4,]
randomnumber =random.randint(0,100)
print(randno2)
print('                    ########WELCOME TO LUCKNOW JUNCTION########')

# canceltkt=int(input('enter [1] if you want to cancel your ticket \n[2] to continue'))
# entertn=int(input ('if you want to exit enter alphabet\nenter your ticketno.\n'))
# if entertn ==1:
#     print('''here's a tip \nenter the ticketno. below 4 digits like\n123,234''')
#     print(f'your ticket {entertn} succesfully canceld')
# if entertn ==2:
a=input('where u want to go \nenter [m] if u want to go mahatashtra\nenter [b] to bhopal\nenter[d] for delhi\nfor chenni[c]\n')
if a == 'm'or 'M':
        print('you can take train {intercity},{lucknowexpress}')
elif a=='b'or'B':
    print('you can take train {rajdhaniexpress}or{chenniexpess}')
elif a== 'd'or 'D':
        print('you can take train {gorakhpurgokhaexpress},{lucknowexpress}')
elif a=="c"or"C":
        print('only this train takes you to chenni{chenniexpress}')
elif a=="h"or'H':
    print('you can go with {rajdhaniexpress}{pushpakexpess}{lokmanyatilakexpress}')
else :
    pass


print('here is available trains  ')

rajdhaniexpress =train('rajdhaniexpress',2000,45,'4:24')
tilakdhariexpress =train('tilakdhariexpress',2500,12,'3:34')
intercityexpress =train('intercityexpress',5000,43,'6:34')
lokmanyatilakexpress =train('lokmanyatilakexpress',9000,23,'2:53')
pushpakexpess=train('pushpakexpess',3000,98,'12:43')
gorakhpurgokhaexpress =train('gorakhpurgokhaexpress', 1200,50,'5:34')
chenniexpress =train('chenniexpress', 4000 , 99,'5:34')
lucknowexpress =train('lucknowexpress',9000,5,'2:45')
print('LUCKNOWEXPRESS')
lucknowexpress.getinfo()
print('TILAKDHARIEXPRESS')
tilakdhariexpress.getinfo()
print('PUSHPAKEXPRESS')
pushpakexpess.getinfo()
print('gorakhpurgokhaexpress')
gorakhpurgokhaexpress.getinfo()
print('rajdhaniexpress')
rajdhaniexpress.getinfo()
print('INTERCITYEXPRESS')
intercityexpress.getinfo()
b =print('chose your train')
if b =="y"or"Y":
    inpum =input ('rajdhaniexpress[r]\nintercityexpress[i]\ngorakhpurgokhaexpress[g]\npushpakexpess[p]\ntilakdhariexpress[t]\n')
input('to buy this ticket you will have to \nsubmit this form below @press enter to continue@\n')
name =input('ENTER YOUR NAME\n')
input('ENTER YOUR EMAIL ADDRESS\n')
ph =int(input('ENTER YOUR PHONE NUMBER\n'))
if ph<9999999999:
    print('this is not valid no.')
elif ph>1111111111:
    print('you will get a 8 digits code')
code = input(f'enter code to verify{code1}')
if code==code1:
    print('you are verified')
else :
    print('failed to verify')
input('HOW MUCH TICKETS YOU WANT TO BUY\n')
input('YOUR NICKNAME\n')
input('YOUR YOUTUBE CHANNEL(optional)\n')
print(f'YOUR TICKET NUMBER IS: {cancelrandom}\nYOUR SEAT IS CONFIRMED \n{name} SEAT NUMBER IS {randomnumber}')
# print('buying*\nbuying**\nbuying***\n something went wrong \nplease check your internet connection\nor check your cyypto account\nretrying*\nretrying**\nretrying***\n sorry user u cant buy this ticket\n failed to buy')
    