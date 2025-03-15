import re
with open('D:\Data Science\Playing With Data\\feq.txt','r') as readfile:
    text=readfile.read()
    print(text)
text=text.strip().split()
if text :
    print('Data Loaded Successfully')
else :
    print('Data Load Failed')
try :
 dict={}
 for word in text :
    dict[word]=text.count(word)
 print(dict.items())
    
except Exception as e :
   print(f'Error {e} occured')

if dict :
   with open('result.txt','w+') as writefile:
      for item in dict.items():
       exp=re.sub(r'[,()'']','',str(item)) 
       writefile.write(str(exp)+'\n')
      print(writefile.read())
else :
   print("Failed to write the file dict found to be empty")
      