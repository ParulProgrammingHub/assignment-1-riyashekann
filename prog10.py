def simple_interest(principal,time,rate):
    ans=(principal*time*rate)
    print "The simple interest is:",ans

principal=input("enter the principal amount")
time=input("enter the time in years")
rate=input("enter the rate(in decimal)")
simple_interest(principal,time,rate)
