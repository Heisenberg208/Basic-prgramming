def F(Number):
	if Number == 0:
		return 0
	elif Number == 1:
		return 1
	else:
		return F(Number - 1) + F(Number - 2)


n = int(input("enter the no of terms:"))
if n<0:
 print("Error:Invalid input")
else:
 print("Fibonacci series:", end=' ')
 for n in range(0, n):
   print(F(n), end=' ')