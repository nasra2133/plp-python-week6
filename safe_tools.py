def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"
    
def get_field(learner, key):
    try:
        return learner[key]
    except KeyError:
        return "Field not found"

print(safe_divide(10, 0))

print(safe_number("25"))
print(safe_number("hello"))

student = {"name": "Amina", "age": 20}
print(get_field(student, "name"))
print(get_field(student, "grade"))