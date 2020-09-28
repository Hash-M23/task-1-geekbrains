n = abs(int(input("Введите целое положительное число, например 10, 20, 30")))
max = n % 10
while n >= 1:
	n = n // 10
	if n % 10 > max:
		max = n % 10
		if n >= 9:
			continue
		else:
			print("Максимальная цифра в числе", max)
			break