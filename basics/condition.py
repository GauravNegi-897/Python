

score = 95

if score > 90:
    print("Grade A")
elif score > 80:
    print("Grade B")
elif score > 79:
    print("Grade C")
else :
    print("Need Improvement")   
    
has_license = True

if has_license:
    print("You can drive")
else:
    print("You cannot drive")
    
has_ticket = False
age = 14

if has_ticket:
    if age >= 18:
        print("You can watch movie")
    else:
        print("Need Supervision")
else :
    print("Need to buy ticket first")