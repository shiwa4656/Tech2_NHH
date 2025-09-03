user = int(input("enter your age"))
if user >=21:
    print("you can drive, vote and drink")
elif user >=18 and user <21:
    print("you can drive and vote")
elif user <18 and user >=16:
    print("you can drive")
else :
    print("you can't drive, vote or drink")
