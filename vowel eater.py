while True:
	user_word = input("Enter the word or type 'E' to exit: ")
	user_word = user_word.upper()
	if user_word == "E":
		exit()
	else:
		for letter in user_word:
			if letter == "A":
				continue
			elif letter == "E":
				continue
			elif letter == "I":
				continue
			elif letter == "O":
				continue
			elif letter == "U":
				continue
			else:
				print("\n",letter)

