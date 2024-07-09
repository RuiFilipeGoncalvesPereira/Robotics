import os
import glob

path = r"C:\Users\Rui Pereira\Desktop\Desktop\Modulos\Oracle"

l = os.listdir(path)
print(l)

#for root, dirs, files in os.walk(path):
#         if files == 'gal' :
#            for f in files:
#             print(os.path.join(root, f))
#         elif files == 'log' :
#            for f in files:
#             print(os.path.join(root, f))
#         elif files == 'tra' :
#            for f in files:
#             print(os.path.join(root, f))
for root, dirs, files in os.walk(path):
            for f in files:
             print(os.path.join(root, f))
#g = glob.glob('*')
#g = glob.glob('*')
#for f in g:
 #   print(os.path.join(path, f))     
#print(g)
