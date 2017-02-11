a=[]
sum=0
for i in range(0,5):
    marks=input("enter the marks out of 100")
    a.append(marks)
    sum=sum+marks

print a
mean=sum/5
print"The mean of the marks is:",mean
perc=float((sum*100)/500)
if perc<35:
    print "Fail","with percentage",perc
else:
    print"Pass","with percentage",perc



