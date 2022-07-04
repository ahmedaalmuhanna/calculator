def calculator(myFirstNumber, mySecondNumber, myOpration) :

	if myOpration == '+' or myOpration =='-' or myOpration == '*' or myOpration == '/':
		if myOpration == '+' :
			myResoult = myFirstNumber + mySecondNumber
			print("the results is :" +str(myResoult))
		elif myOpration == '-' :
			myResoult = myFirstNumber - mySecondNumber
			print("the results is :" +str(myResoult))
		elif myOpration == '*' :
			myResoult = myFirstNumber * mySecondNumber
			print("the results is :" +str(myResoult))
		elif myOpration == '/' :
			myResoult = myFirstNumber / mySecondNumber
			print("the results is :" +str(myResoult))

	else : print("your Opration is invalid")
		

def main():
	#write your code here
	#pass
	firstNumber = input("Enter the first number:")
	secondNumber = input("Enter the second number:")
	operation = input("Choose the operation (+, -, /, *):")

	print(type(firstNumber))

	print(type(secondNumber))
 
	if firstNumber.isdigit() and secondNumber.isdigit():
		calculator(int(firstNumber), int(secondNumber), operation)
	else:
		print("your numbers is invalid")

 


if __name__ == '__main__':
	main()
