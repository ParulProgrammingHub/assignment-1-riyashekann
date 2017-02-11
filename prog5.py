print " conversion of days into year month and days"

days=input("enter the no of days")
year=days/360
month=(days/30)/12
day=(days%360)%30
print"%d is equal to : %d years , %d months,%d days" % (days,year,month,day)
