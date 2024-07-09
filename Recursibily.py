import os

target = 'c:\\Users\\Rui Pereira\\Desktop\\Desktop\Modulos'

for root, dirnames, files in os.walk(target):
     for x in files:
         if x.endswith('.sql'):
           print(root + '\\' +x)
   
