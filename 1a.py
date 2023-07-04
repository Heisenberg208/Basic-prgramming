m1 = int (input("Enter the marks in the first test: "))
m2 = int (input("Enter the marks in second test: "))
m3 = int (input("Enter the marks in third test: "))

total=(m1+m2+m3-min(m1,m2,m3))
    
Avg = total / 2
print(f"The average of {m1} the best two test marks is: {Avg}")
