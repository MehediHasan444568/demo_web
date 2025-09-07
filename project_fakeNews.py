import random
subjects= [
    "Shakib Al Hasan",
    "Sheik Hasina",
    "Narandra Modi",
    "Obaidul Kader",
    "Pori Moni",
    "A group of dogs",
    "Student leader"

]
actions=[
    "fall into",
    "got married again",
    "mocked",
    "hited",
    "ignored",
    "enjoyed"
]
objects=[
    "a supporter",
    "another person",
    "at Chattogram",
    "at Bali",
    "a politician"
]
while True:
    subject= random.choice(subjects)
    action= random.choice(actions)
    object= random.choice(objects)
    headline= f"BREAKING NEWS: {subject} {action} {object} !"
    print ("\n"+headline)
    user_input=input("Do you want to generate more fake news headline? (YES/NO)").strip().lower()
    if user_input=="no":
        break
print ("Thanks for using the fake news headline generator. Have a good day...")