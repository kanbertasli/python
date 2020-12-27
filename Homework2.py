"""
User Identification Program
The user will be defined. Get the data of this user by input method. 
Obtain information from user as follow.
- First Name
- Last Name
- Age
- Date of birth(just year)

Pass the users information to the list and displays the screen using the for loop. 
Print all user information on the screen.
If he is under 18, print "You can't go out because it's too dangerous" on screen.
If he is over 18, print "You can go out to the street." on screen.
"""
mylist = list(range(4))
mylist[0]=str(input("Please enter your first name: "))
mylist[1]=input("Please enter your last name: ")
mylist[2]=int(input("How old are you?: "))
mylist[3]=input("What is your year of birth?: ")

#Girilen değerlerin doğruluğu kontrol edilmeli! isim soy ismin de string olup olmadığı kontrole eklenebilir.

if(int(mylist[3])<1920 or int(mylist[3])>2020):
    print("Please check year of birth. Should be between 1920 and 2020")
elif(int(mylist[2])<0 or int(mylist[2])>100):
    print("Please check your age. Should be between 1 and 100")
elif((2020-int(mylist[3])) != int(mylist[2])):
    print("Please check your age and year of birth.If we look your year of birth you should:"+str(2020-int(mylist[3])))
else:
    for i in mylist:
        print(i)
        
    if mylist[2] < 18:
        print("You can't go out because it's too dangerous")
    else:
        print("You can go out to the street.")
