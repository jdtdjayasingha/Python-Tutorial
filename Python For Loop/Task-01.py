x = [1,2,3,4,5]

print(5 in x)
print(37 in x)

for num in x:   
 print(num)


m = {"Name": "John",
     "Age": 30,
     "gender": "Male"}

for num2 in m.keys():
    print(num2)

for num3 in m.values():
    print(num3)

for num4 in m.items():
    print(num4)

for num5, num6 in m.items():
    print(num5, num6)


for num7 in range(5):
    print(num7)

for num8 in range(2, 10):
    print(num8)

for num9 in range(2, 10, 2):
    print(num9)