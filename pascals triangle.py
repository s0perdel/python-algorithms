print("Pascal's Triangle")

while True:
	n = int(input("Enter the number of lines: "))
	if n == 0:
		pass
	elif n == 1:
		print("\n1")
	elif n == 2:
		print("\n 1")
		print("1 1")
	else:
		print("\n" + " "*n + "1")
		print(" "*(n-1) + "1 1")
		counter = 2
		line = [1, 1]
		while counter <= n:
			new_line = [1]
			index = 0
			while index < len(line) - 1:
				new_line.append(line[index]+line[index+1])
				index += 1
			new_line.append(1)
			line = new_line
			result = " " * (n - counter)
			for number in line:
				result += str(number) + " "
			print(result)
			counter += 1
