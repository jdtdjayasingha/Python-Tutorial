def my_function():
    print("Hello, World!")

my_function()


def my_message():
    return "This is my message."

print(my_message())


def my_sum(a, b):
    return a + b

result = my_sum(5, 10)
print(result)


def my_rectanglecl(length, width):
    perimeter = 2 * (length + width)
    area = length * width
    
    print("Perimeter:", perimeter)
    print("Area:", area)

my_rectanglecl(5, 10)
my_rectanglecl(7, 3)