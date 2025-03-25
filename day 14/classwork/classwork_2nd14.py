# 2) მომხმარებელს შემოატანინეთ 5 სახეთი, შემდეგ კი კიდევ ერთი for loop გამოიყენეთ რათა გაიგოთ ამ სახელებში სიმბოლოების რაოდენობა აღემატება თუ არა 5-ს. თუ აღემატება დაუბეჭდეთ "the name consists of more than five letters)


names = []

for i in range(5):
    name = (input("Please enter name: "))
    names.append(name)

for name in names:
    if len(name) > 5:
        print("the name consists of more than five letters")
    else:
        print("name is correct")