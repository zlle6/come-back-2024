import tkinter as tk
import webbrowser

import yes

#root = tk.Tk()
#root.geometry("250x250")
#root.title("first")

#entery = tk.Entry(root, width=15, font= ("Arial", 14))
#entery.pack(pady=120)


print('welcome to quiz game')

userinput= input("press 1 to continue: ")


quest = 'how many ppl are there in world?'

if userinput == '1':
    print(quest)

else:
    print("Exiting the game. Goodbye!")
    exit()
pass




options=[    8    ,    6    ,    7    ,    4    ]
print(options)
answer = input ("type down: ")
1
if answer =='8':
    print("correct")
elif answer =='6':
     print("wrong")
elif answer =='4':
     print("wrong")
elif answer == '7':
     print("wrong")


else:
    print("Shame on you, Exiting the game. Goodbye!")
    exit()

pass



quest1= 'will israel attack iraq?'


user= input("if you want to contniue press 2: ")
if user == '2':
    print(quest1)

else:
    print("Exiting the game. Goodbye!")
    exit()
pass


quest1 = ('will israel attack iraq?')

optionss=[    'Yes'    ,    'No'   ,    'Maybe'   ,    'Never'   ]
print(optionss)


answer1 = input ("type down: ")
if answer1 =='yes':
    print("correct")

elif answer1 =='no':
     print("wrong")
elif answer1 =='maybe':
     print("correct")
elif answer1 == 'never':
     print("wrong")
else: print("shame on you")

pass

quest2= 'does kurdistan will earse?'
user2= input("if you want to contniue press 3: ")
if user2 == '3':
    print(quest2)



options2=[    'Yes'    ,    'No'   ,    'Maybe'   ,    'Never'   ]
print(options2)

answer3 = input ("type down: ")
if answer3 =='yes':
    print("correct")

elif answer3 =='no':
     print("wrong")
elif answer3 =='maybe':
     print("correct")
elif answer3 == 'never':
     print("wrong")
else: print("shame on you")

pass


math= "2*4?"
quest3= 'how many legs do human have?'
user3= input("if you want math quiz press 1, if you want only quiz game press 4: ")
if user2 == '4':
    print(quest3)
elif user3== "1":
    print(math)

#root.mainloop()
