# 5) შექმენით ფუნქცია და გადაეცით არგუმენტად სია. ფუნქციამ უნდა დააბრუნოს ახალი სია, რომლის თითოეული ელემენტიც უნდა იყოს კვადრატში აყვანილი.

def numbers(nums):
    square_nums = []
    for i in nums:
        square_nums.append(i * i)
    return square_nums

print(numbers([2, 3, 4, 5]))