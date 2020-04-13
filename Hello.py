# Non return
def hello(name):
    print("Hello %s" % name)


hello("Nawat")


# Return Value
def area(width, height):
    total = width * height
    return total


print(area(3, 4))


# Default Agrument Value
def show_info(name="", salary = 30000, lang = "Non Define"):
    print("Name = %s" % name)
    print("Salary = %d" % salary)
    print("Languages = %s" % lang)


show_info()
print()
show_info("Nawat", 50000)
print()
show_info("Nawat", 60000, "Python")

