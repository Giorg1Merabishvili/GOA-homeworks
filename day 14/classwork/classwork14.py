# 1) მომხმარებელს შემოატანინეთ 10 მნიშვნელობა სიაში (For loop-ის მეშვეობით. ) შემდეგ გამოიყენეთ კიდევ ერთი for loop, გადაუარეთ თითოეულ სიის ელემენტს და შამოწმეთ ეს რიცხვები ლუწია თუ კენტი


nums = []

for i in range(10):
    num = int(input("Please enter number: "))
    nums.append(num)

for num in nums:
    if num % 2 == 0:
        print("This number is even.")
    else:
        print("This number is odd")