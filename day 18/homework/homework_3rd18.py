# 4) შექმენით სია სადაც შეინახავთ 5 რიცხვს, მომხმარებელს აარჩევინეთ ამ სიიდან ერთ-ერთი რიცხვი და დათვალეთ თუ რამდენჯერ მეორდება ეს რიცხვი სიაში.

numbers = [1, 2, 3, 1, 4]

user_choice = int(input("Choose number from 1 to 4: "))

count = numbers.count(user_choice)

print(f"the number {user_choice} appears {count} times in the list.")