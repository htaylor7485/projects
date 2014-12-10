userName = ""
while userName=="":
    userName = input ("What is your name?")

if userName == "Harry":
    print("Good morning {1}!!".format(userName,"God"))
elif userName =="David":
    print("Good morning {1}!!".format(userName,"Jesus"))
elif userName =="Nick":
    print("Good morning {1}!!".format(userName,"Poop"))
else:
    print("Good morning {0}!!".format(userName))

