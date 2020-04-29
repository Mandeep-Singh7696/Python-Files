##Solution-1
f=open("salary.txt",'w+')
f.write('10000\n')
f.write('2000\n')
f.write('1200\n')
f.write('13400\n')
f.write('21000')
f.seek(0)
l=f.readlines()
s=0
for i in l:
   print(int(i))
   s+=int(i) 
print(l)
print(s)
f.close()
