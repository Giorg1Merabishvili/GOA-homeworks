guess_number = 8
user_response = int(input("Please enter number: "))

while user_response != guess_number:
    user_response = int(input("Please try again: "))

print("Correct answer, good job. ")