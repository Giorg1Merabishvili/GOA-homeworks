# 1) ჩამოწერეთ ყველა პითონის ჩაშენებული ფუნქცია, რაც დღს განვიხილეთ.
# 2) დაწერეთ ამ ფუნქციების ორ-ორი მაგალითი და ახსენით თუ როგორ მუშაობს თითოეული.

# pop, remove, clear, extend, insert

fruits = ["apple", "banana", "orange"]

fruits.pop(0)

print(fruits)

# pop ფუნქციით ამოვშალე 0 ინდექსზე მდგომი ღირებულება.

fruits2 = ["apple", "banana", "orange"]

fruits2.remove("apple")

print(fruits2)

# remove-ც იგივე ნაირად მუშაობს მაგრამ ეს მითითბულ სიმბოლოებს შლის

fruits3 = ["apple", "banana", "orange"]

fruits3.clear()

print(fruits3)

# clear ფუნქცია შლის ყველაფერს რაც სიაში არის.

fruits4 = ["apple", "banana", "orange"]
fruits5 = ["apple", "banana", "orange"]

fruits4.extend(fruits5)

print(fruits4)

# extend ფუნქცია აერთიანებს ორ სიას ერთამნეთთან.

fruits6 = ["apple", "banana", "orange"]

fruits6.insert(1, "avocado")

print(fruits6)

# insert ამატებს სიაში ღირებულებას მითითბულ ინდექსზე.