def interest(a:float,b:float,c:float):
    d=(a*b*c)/100
    return d

principle=float(input("enter principle amount:"))
time=float(input("enter investing time in years:"))
rate=float(input("enter rate of interest:"))
inte= interest(principle,rate,time)
print(inte)