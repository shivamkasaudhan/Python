age = int(input("Age : "))
if age <0 or age >120:
    print("invalid")
elif age <18:
    print("minor")
elif age >=18 and age<=65:
    print("adult")
else :
    print("senior")