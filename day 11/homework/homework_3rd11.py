email = "Email11@gmail.com"
password = "paroli123"

email_response = input("Enter email: ")
password_response = input("Enter password: ")

while email_response != email and password_response != password:
    email_response = input("Please try again, Enter email: ")
    password_response = input("Please try again, Enter password: ")
print("Accsess granted.")
