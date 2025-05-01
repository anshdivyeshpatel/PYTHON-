def calculate_net_sales(gross_sales:float):
    return gross_sales * 0.90  

gross_sales = float(input("Enter gross sales: "))
print("Net Sales:",calculate_net_sales(gross_sales))