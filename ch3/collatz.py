def collatz(number):
	try:
		number = int(number)

		if number % 2 == 0:
			print(number // 2)
			return number // 2
		else:
			print(3 * number + 1)
			return 3 * number + 1
	except ValueError:
		print('Noninteger string!')

print('Enter a number for collatz.')
num = input()

while True:
	num = collatz(num)
	if num == 1:
		break