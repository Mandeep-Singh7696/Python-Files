##largest line
f=open("demo.txt",'r')
c=0
l=''
lo=0
for i in f:
    c+=1
    print(f"Line no:{c}")
    print(i)
    print(f"No. of characters= ",len(i)-1)
    print("----------------------------")
    if len(i)>len(l):
        l=i
##        lo=i
print(f"long : {l} ",len(l))
f.close()
        
