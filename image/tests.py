from django.test import TestCase

# Create your tests here.
import os

a = 'F:\pycharm\MySite\media/images/2019/04/02/Biao-Qing-Bao-1.png'
b = a.rsplit('/',1)
print(b)  #  ['F:\\pycharm\\MySite\\media/images/2019/04/02', 'Biao-Qing-Bao-1.png']
b = a.rsplit('/',2)
print(b)  #['F:\\pycharm\\MySite\\media/images/2019/04', '02', 'Biao-Qing-Bao-1.png']
if not os.listdir(b[0]):
    print('文件夹为空')
else:
    print('have something')

