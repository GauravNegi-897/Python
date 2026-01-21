

def greet():
    print("hello, good morning")
    
greet()


def check_weather():
    temperature = 32
    
    if temperature > 25:
        print("Its Very hot")
    else:
        print("Its nice weather")
        
check_weather()


def greet(first_name , last_name):
    print(f"Hello {first_name} {last_name}")

greet("Gaurav" , "Negi")

def add_numbers(num1 , num2):
    return num1 + num2

sum = add_numbers(2,3)

print("sum : " , sum)


def calculate_area(width , height):
    return width * height

area = calculate_area(12,23)

print(f"The total area is {area} sq. ft.")