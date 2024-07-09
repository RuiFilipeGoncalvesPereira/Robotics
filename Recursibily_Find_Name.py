import os

target = 'c:\\Users\\Rui Pereira\\Desktop\\Desktop\\Modulos'

for root,dir,filelist in os.walk(target):
      for name in dir:
          if (name == 'tab'):
            print(os.path.join(root, name))
    
             
    
