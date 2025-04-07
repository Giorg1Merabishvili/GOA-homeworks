# 5) შექმენით სია, სადაც დაამატებთ მინიმუმ 5 ელემენტს. მომხმარებელს ჰკითხე სურს თუ არა სიის გასუფთავება. თუ დაგთანხმდება გაასუფთავე სია თუ არა მაშინ ჩვეულებრივად დაბეჭდე ეს სია ტერმინალში.

names = ["gio", "nika", "luka", "nana", "nini"]

user_answer = input("Enter yes if u want to clear list enter no if you don't: ")

if user_answer == "yes":
    names.clear()
    print(names)
elif user_answer == "no":
    print(names)
else:
    print("Please enter yes or no.")