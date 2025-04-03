# 3) შექმენით ფუნქცია სახელწოდებით double_values რომელიც არგუმენტად მიიღებს სიას და დააბრუნებს ახალ სიას, სადაც თითოეული ელემენტი გაორმაგებული იქნება.

def double_values(list):
    double = []
    for i in list:
        double.append(i * 2)
    return double

print(double_values([1, 2, 3, 4, 5,]))
