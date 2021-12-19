#Palindrom check

def isPalindrom(word):
	back = list(word.lower())
	back.reverse()
	if back == list(word.lower()): return True
	return False	

while True:
	print(isPalindrom(input()))