with open('3.txt', 'r', encoding='utf-8-sig') as file:
	message =[]
	for line in file:
		message = line.strip().split(' ')
		time = message[0][0:5]
		name = message[0][5:]
		print(time)
		print(name)

		


