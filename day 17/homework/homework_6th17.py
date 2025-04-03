# 7) შექმენით ფუნქცია და გადაეცით რიცხვების სია არგუმენტად. ფუნქციის მიზანი იქნება, რომ სიიდან დააბრუნოს მხოლოდ უარყოფითი რიცხვები.

def negative_numbers(numbers):
    result = []
    for num in numbers:
        if num < 0:
            result.append(num)
    return result

print(negative_numbers([-1, 2, -4, 4]))