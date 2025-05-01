def areaoftriangle(a:float,b:float):
    c=(1/2)*a*b
    return c
length=float(input("enter length of triangle:"))
height=float(input("enter height of triangle:"))

print("area of triangle is",areaoftriangle(length,height))