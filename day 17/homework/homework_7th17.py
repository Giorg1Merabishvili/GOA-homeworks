# 8) წინა დავალების ანალოგიურად შექმენით ფუნქცია და გადაეცით რიცხვების სია არგუმენტად. ამ შემთხვევაში ფუნქციის მიზანი იქნება, რომ სიიდან დააბრუნოს მხოლოდ დადებითი რიცხვები.

def positive_numbers(numbers):
    result = []
    for num in numbers:
        if num >= 0:
            result.append(num)
    return result

print(positive_numbers([1, 2, 3, -1, -2, -3]))