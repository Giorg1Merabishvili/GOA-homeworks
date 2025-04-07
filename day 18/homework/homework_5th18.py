# 6) შექმენით სია სახელად Fruits და ჩაამატეთ მასში ხილი. მომხმარებელს შემოატანინეთ ინდექსი და შემდეგ  ამ ინდექსზე მდგომი ელემენტი ამოშალე სიიდან. საბოლოოდ დაბეჭდე სიის საბოლოო ვერსია.

fruits = ["apple", "banana", "orange", "pineapple", "grape"]

user = int(input("Choose which fruit u want to delete by indexing: "))

fruits.pop(user)

print(fruits)