import random
computer_choice={
    0:"Rock",
    1:"Paper",
    2:"Scissor"
}
c_choice=random.randint(0,2)
# print(f"Computer choice: {computer_choice[c_choice]}")
human_choice={
    1:"Rock",
    2:"Paper",
    3:"Scissor"
}
print("""Your choices are:
      1.Rock
      2.Paper
      3.Scissor""")
user_choice=int(input("Enter your choice: "))
print(f"User choice: {human_choice[user_choice]}")
if(human_choice[user_choice]==computer_choice[c_choice]):
    print(f"The computer choose: {computer_choice[c_choice]}")
    print(f"You choose: {human_choice[user_choice]}")
    print("Result: Draw!")
elif((human_choice[user_choice]== "Rock" and computer_choice[c_choice]=="Scissor")
     or(human_choice[user_choice]=="Paper" and computer_choice[c_choice]=="Rock")
     or(human_choice[user_choice]=="Scissor" and computer_choice[c_choice]=="Paper")):
    print(f"The computer choose: {computer_choice[c_choice]}")
    print(f"You choose: {human_choice[user_choice]}")
    print("Result: You won!")
else:
    print(f"The computer choose: {computer_choice[c_choice]}")
    print(f"You choose: {human_choice[user_choice]}")
    print("Result: Computer won!")
    