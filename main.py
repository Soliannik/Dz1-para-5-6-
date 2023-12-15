def divider(a, b):
   try:
       return a / b
   except ZeroDivisionError:
       print("You cant divide one")
   except TypeError:
       print("Please enter number!")
   except ValueError:
       print("Please, enter number,not a word")

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
result = []
for key in data:
   res = divider(key, data[key])
   result.append(res)
print(result)