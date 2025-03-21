# 10) რთული:
# მომხმარებელს შემოატანინეთ რიცხვი და დაწერეთ პროგრამა, რომელიც შეამოწმებს ეს რიცხვი მარტივია თუ არა. (მარტივია რიცხვი, თუ მას მხოლოდ ორი გამყოფი აქვს). მინიშნება: გამოიყენეთ For loop და % გამყოფი ოპერატორი, ასევე აუცილებლად დაგჭირდებათ პროგრამაში Boolean ნიშვნელობების გამოყენება (True და False).

num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print("This number isn't prime number. ")
        break
else:
    print("This number is prime number.")