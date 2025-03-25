# 4) ცვლადში შეინახეთ ცარიელი სია. input-ის მეშვეობით მომხმარებელს შემოატანინეთ ინფორმაცია საკუთარი თავის შესახებ. (მაგ. სახელი, გვარი, ასაკი, დაბადების თარიღი, სიმაღლე და ა.შ.)მომხმარებელმა მინიმუმ უნდა შემოიტანოს 8 input. ეს ყოველივე input დაამატეთ თქვენს მიერ შექმნილ ცარიელ სიაში.

information = []

for i in range(8):
    user_response = input("Information about yourself, (age/name/lastname/height/birthday/etc): ")
    information.append(user_response)
    print(information)