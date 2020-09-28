profit = float(input("Введите выручку фирмы"))
costs = float(input("Введите издержки фирмы"))
if profit > costs:
	print(f"фирма работает с прибылью. Выручка составила {profit / costs}")
	workers = int(input("Введите количество сотрудников"))
	print(f"Прибыль в расчете на одного сотрудника составила {profit / workers}")
elif profit == costs:
	print("Фирма работает в ноль")
else:
	print("Фирма работает в убыток")