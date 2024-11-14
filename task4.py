import random
def game():
    print("rules : rock beats scissor, scissor beats paper, paper beats rock")
    user_choice=input('rock/paper/scissor :')
    print("user's choice is : ",user_choice)
    options=["rock","paper","scissor"]
    comp_choice=random.choice(options)
    print("computer's choice is : "+str(comp_choice))
    if (comp_choice=='rock' and user_choice=='paper'):
        print("user won")
    if (comp_choice=='scissor' and user_choice=='rock'):
        print("user won")
    if (comp_choice=='paper' and user_choice=='scissor'):
        print("user won")
    if (comp_choice=='scissor' and user_choice=='paper'):
        print("computer won")
    if (comp_choice=='paper' and user_choice=='rock'):
        print("computer won")
    if (comp_choice=='rock' and user_choice=='scissor'):
        print("computer won")
    if (comp_choice=='paper' and user_choice=='paper'):
        print("game tied")
    if (comp_choice=='scissor' and user_choice=='scissor'):
        print("game tied")
    if (comp_choice=='rock' and user_choice=='rock'):
        print("game tied")
game()
print("do you want to play again this game")
play_again=input('y if yes or n if no : ')
if(play_again=='y'):
    game()
feedback=input('what is your feedback about this game ?\n')
print("user's feedback is:",feedback)





