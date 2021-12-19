# Dividing a number by prime factors

while True:
	number = int(input("Enter the number: "))
	prime_numbers = [2,3,5,7]
	prime_possible = 8
	Col1 = []
	Col2 = []

	# Creating a prime numbers array (size <= number)
	while prime_possible <= number:
		probability = 0
		for i in prime_numbers:
			if not prime_possible % i == 0:	
				probability += 1
		if probability == len(prime_numbers):
			prime_numbers.append(prime_possible)
		prime_possible += 1

	# Checking for a prime number
	if number < 2: 
		print("Only numbers > 1")
	elif number in prime_numbers: 
		print("{} is a prime number.".format(number))
	else:
		# Dividing
		temp = 0
		while not number in prime_numbers:
			for j in prime_numbers:
				if number % j == 0:
					Col1.append(number)
					Col2.append(j)
					temp = j
					break
			number = int(number / temp)
		Col1.append(number)
		Col2.append(number)
		# Show result
		temp = 0
		while temp < len(Col1):
			print(str(Col1[temp])+" "*(len(str(Col1[0]))-len(str(Col1[temp]))+1)+"| "+str(Col2[temp]))
			temp += 1
		print("1"+" "*(len(str(Col1[0])))+"|")