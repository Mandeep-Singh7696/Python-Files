##grades
f=open("num.txt",'r')
stu=(f.readline())
print(f"Total number of students:{stu}")
for i in range(int(stu)):
    print("Student",i+1,':',end="")
    l=f.readline().split()
    print(l)
    s=0
    for j in range(len(l)):
       s=s+int(l[j])
       per=float((s/500)*100)
    print(f"Sum={s} Percentage={per}")
f.close()

    
