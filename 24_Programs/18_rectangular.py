def areaofrectangle(a:float,b:float):
    c=a*b
    return c
def perimeterofrectangle(a:float,b:float):
    c=(2*(a+b))
    return c
length=float(input("enter length:"))
breadth=float(input("enter breadth:"))

print(areaofrectangle(length,breadth))
print(perimeterofrectangle(length,breadth))
