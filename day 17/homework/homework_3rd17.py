# 4) შექმენით ფუნქცია, რომელსაც არგუმენტად გადასცემთ სიას (ჩათვალეთ, რომ სიაში ინახება Integer-ი რიცხვები). ამ ფუნქციამ საბოლოოდ უნდა დააბრუნოს სიიდან მხოლოდ ლუწი რიცხვები.

def even_numbers(num):
    even = []
    
    for i in num:
        if i % 2 == 0:
            even.append(i)
    return even
 
print(even_numbers([2, 3, 5, 6]))