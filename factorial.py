def factorial(num: int) -> int:
	fact = 1
	for i in range(num, 1, -1):
		fact *= i
	return fact

print(factorial(5))