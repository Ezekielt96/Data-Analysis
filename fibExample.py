# Fib program
# Michael Lewis


def fib(n) :
	if n == 0 or n == 1 :
		return 1
	value = fib(n-1) + fib(n-2) 
	return value


finalValue = fib(10)
print(finalValue)

