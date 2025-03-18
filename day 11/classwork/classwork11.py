sum = 0

for number in range(10):
    user_response = int(input("Enter numbers: "))
    sum = sum + user_response
    print(sum)
print(sum / 10)