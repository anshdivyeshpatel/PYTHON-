def calculate_total_and_average(sub1:float,sub2:float,sub3:float):
    total=sub1+sub2+sub3
    average=total/3
    return total,average

subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

total,average =calculate_total_and_average(subject1,subject2,subject3)

print("total marks:",total)
print("average marks:", average)
