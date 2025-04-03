# 6) შექმენით ფუნქცია და არგუმენტად გადაეცით String-ი. ფუნქციამ ეგრედწოდებულად უნდა "გაფილტროს" ეს სტრინგი თანხმოვანი ასოებისგან და მხოლოდ დააბრუნოს ის ხმოვანი ასოები, რომლებსაც ეს სტრინგი შეიცავს.

def filter_vowels(text):
    result = ""
    for i in text:
        if i in "aeiouAEIOU":
            result += i
    return result

print(filter_vowels("giorgi"))