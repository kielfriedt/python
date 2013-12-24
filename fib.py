
fib_array = []

def fib(prev, next, count):
	fib_array.append(next)
	while (count >= 0):
		count = count -1
		return fib(next, prev+next, count)
	fib_array.append(next)
	
notfound = 1		
fib_num = int(input("please enter in a number of the fib sequence you want to calculate. "))
if fib_num == 1:
	#print("0")
	fib_array.append(0)
if fib_num == 1:
	#print("1")
	fib_array.append(1)
else:
	fib_array.append(0)
	fib(0,1,(int(fib_num)-3))
	fib_array.reverse()
for i in fib_array:
	print(i)
