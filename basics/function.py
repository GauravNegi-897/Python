

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