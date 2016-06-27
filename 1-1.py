while(True):
	temp = input("Please input the number you guess(1-100): ")
	guess = int(temp)
	if guess==8:
		print("love you")
		print("you are so smart")
		break
	elif guess>8:
		print("The number you guess is bigger!")
	elif guess<8:
		print("The number you guess is smaller!")

