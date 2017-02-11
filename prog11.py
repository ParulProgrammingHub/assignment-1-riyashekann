def compound_interest(principal,rate,time):
    num=input("enter number of times the interest compounds each year")
    amount=principal*(1+(rate/num))**(num*time)
    print "THe compound interest is:",amount

principal=input("enter the principal amount")
rate=input("enter the rate(in decimal form)")
time=input("enter the time in years of the deposit")

compound_interest(principal,rate,time)
