numbers = []
for i in range (5): 
    num1 = float(input(f"Enter {i+1} number: ")) #მომხმარებელს ვუთხარი რომ შემოეტანა 5 რიცხვი.
    
    numbers.append(num1) #ეს პროგრამა ინახავს რიცხვებს სხვა რიცხვებთან ერთად.

    print(numbers) #ტერმინალში გამოვიტანე ყველა დაწერილი რიცხვი

    avg = sum(numbers) / len(numbers)
    print(f"The arithmetic mean of the entered numbers:  {avg}") #და საბოლოოდ პროგრამას გამოვათვლევინე საშუალო არითმეტიკული.
    