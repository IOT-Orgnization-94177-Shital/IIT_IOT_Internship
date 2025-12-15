
def greet(name="Student", message="Welcome to Python"): 
 print(f"Hello {name}! {message}")
greet()                     
def student_info(name, age, course="Python"): 
 print("Name  :", name)
 print("Age   :", age) 
 print("Course:", course)
student_info("shital", 20, "Java")
print("-")
student_info(age=22, name="kishori", course="Data Science") 
student_info(name="yash", age=21)
def add(a, b): 
 return a + b
def multiply(a, b): 
  return a * b
def calculate(operation, x, y):
 result = operation(x, y) 
 return result
print("Addition Result     :", calculate(add, 10, 5)) 
print("Multiplication Result:", calculate(multiply, 10))