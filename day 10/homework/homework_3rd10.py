password = "paroli123"

user_response = input("Enter passwrod: ")
while user_response != password:
    print("Incorrect password. Try again")
    user_response = input("Enter passwrod: ")
print("Correct password. You have successfully logged in.")