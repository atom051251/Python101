Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = 'Atom'
print(name)
Atom
type(name)
<class 'str'>
name.lower()
'atom'
name.upper()
'ATOM'
friend = 'PP'
print('สวัสดี',friend,'สบายดีไหม')
สวัสดี PP สบายดีไหม
money = 10
print(friend,'ยืมเงิน',money,'บาท')
PP ยืมเงิน 10 บาท
type(money)
<class 'int'>
print(friend + 'ยืมเงิน' + str(money) + 'บาท')
PPยืมเงิน10บาท
print('{}ยืมเงิน {} บาท'.format(friend,money))
PPยืมเงิน 10 บาท

print('{} ยืมเงิน {} บาท'.format(friend,money))
PP ยืมเงิน 10 บาท
print('{} ให้เงิน{} {} บาท'.format(friend,name,money))
PP ให้เงินAtom 10 บาท
print(f'{friend}ยืมเงิน{money}บาท')
PPยืมเงิน10บาท
money = 123390845948
print(f'{money:,}')
123,390,845,948
print(f'{money}:,.2f')
123390845948:,.2f
print(f'{money:,.2f}')
123,390,845,948.00
print('{:,.2f}'.format(money))
123,390,845,948.00
import math
math.pi
3.141592653589793
math.pi * (5**2)
78.53981633974483
from datetime import datetime
dattime.now()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    dattime.now()
NameError: name 'dattime' is not defined. Did you mean: 'datetime'?
datetime.now()
datetime.datetime(2023, 2, 10, 20, 56, 17, 876548)
datetime.now('%d%m%Y %H:%M')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    datetime.now('%d%m%Y %H:%M')
TypeError: tzinfo argument must be None or of a tzinfo subclass, not type 'str'
datetime.now().strtime('%d%m%Y %H
                       
SyntaxError: incomplete input
datetime.now().strtime('%d%m%Y %H:%M')
                       
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    datetime.now().strtime('%d%m%Y %H:%M')
AttributeError: 'datetime.datetime' object has no attribute 'strtime'. Did you mean: 'strftime'?
datetime.now().strftime('%d%m%Y %H:%M')
                       
'10022023 21:02'
datetime.now().strftime('%d/%m/%Y %H:%M')
                       
'10/02/2023 21:03'
import random
random.randint(1,5)
3
store = ['เสื้อพ่อ','เสื้อplayboy','เสื้อชมพู']
random.choice(store)
'เสื้อพ่อ'

= RESTART: C:/Users/User/OneDrive/Desktop/ง่วงงง/smodule.py
Atom

= RESTART: C:/Users/User/OneDrive/Desktop/ง่วงงง/smodule.py
Traceback (most recent call last):
  File "C:/Users/User/OneDrive/Desktop/ง่วงงง/smodule.py", line 2, in <module>
    import study
ModuleNotFoundError: No module named 'study'
>>> 
= RESTART: C:/Users/User/OneDrive/Desktop/ง่วงงง/smodule.py
Traceback (most recent call last):
  File "C:/Users/User/OneDrive/Desktop/ง่วงงง/smodule.py", line 2, in <module>
    import study,py
ModuleNotFoundError: No module named 'study'
>>> 
= RESTART: C:/Users/User/OneDrive/Desktop/ง่วงงง/smodule.py
Traceback (most recent call last):
  File "C:/Users/User/OneDrive/Desktop/ง่วงงง/smodule.py", line 2, in <module>
    import study,py
ModuleNotFoundError: No module named 'py'
>>> 
= RESTART: C:/Users/User/OneDrive/Desktop/ง่วงงง/smodule.py
Atom
2500
>>> 
= RESTART: C:/Users/User/OneDrive/Desktop/ง่วงงง/knowledge.py
>>> 
= RESTART: C:/Users/User/OneDrive/Desktop/ง่วงงง/knowledge.py
>>> 
= RESTART: C:/Users/User/OneDrive/Desktop/ง่วงงง/knowledge.py
>>> 
= RESTART: C:/Users/User/OneDrive/Desktop/ง่วงงง/knowledge.py
Traceback (most recent call last):
  File "C:/Users/User/OneDrive/Desktop/ง่วงงง/knowledge.py", line 2, in <module>
    from tkonter import ttk #theme of tk
ModuleNotFoundError: No module named 'tkonter'
>>> 
= RESTART: C:/Users/User/OneDrive/Desktop/ง่วงงง/knowledge.py
