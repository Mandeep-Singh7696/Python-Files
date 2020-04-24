##f1 to f2 having uppercase
f1=open("f1.txt",'r')
f2=open("f2.txt",'w')
for i in f1:
    if i[0] not in 'abcdefghijklmnopqrstuvwxyz':
        f2.write(i)
f2.close()
