# 11) მომხმარებელს შემოატანინეთ ნებისმიერი რიცხვი, შემდეგ კი 1-დან მომხმარებლის მიერ შეყვანილი რიცხვის ჩათვლით არსებული ყველა რიცხვის ჯამი გამოთვალეთ და გამოიტანეთ ეკრანზე.

sum = 0
num = int(input("Enter a number: "))

for i in range(1, num):
    sum = sum + i
    print(sum)