from random import randint

def convert_user_input_to_dice_indices(user_choice):
    ans=[]
    choice = user_choice.split(" ")
    for dice in range(len(choice)):
        ans.append(int(choice[dice].replace("D",""))-1)
    return ans

def roll_dice(current_dice_rolls, dice_to_roll):
    ans = current_dice_rolls
    try:
        ans[4]
    except IndexError:
        ans = [1,1,1,1,1]
    for rolls in dice_to_roll:
        ans[rolls] = randint(1,6)
    return ans

def calculate_score(current_dice_rolls):
    cdr = []
    cdr = sorted(current_dice_rolls)
    if cdr[0] == cdr[1] == cdr[2] == cdr[3] == cdr[4]:
        ans = 50
    elif cdr[0] == cdr[1]-1 == cdr[2]-2 == cdr[3]-3 == cdr[4]-4:
        ans = 40
    elif cdr[0] == cdr[1]-1 == cdr[2]-2 == cdr[3]-3 or cdr[1] == cdr[2]-1 == cdr[3]-2 == cdr[4]-3:
        ans = 30
    elif cdr[0] == cdr[1] == cdr[2] and cdr[3] == cdr[4] or cdr[0] == cdr[1] and cdr[2] == cdr[3] == cdr[4]:
        ans = 25
    elif cdr[1] == cdr[2] == cdr[3] == cdr[4]:
        ans = cdr[1]*4
    elif cdr[0] == cdr[1] == cdr[2] == cdr[3]:
        ans = cdr[0]*4
    elif cdr[2] == cdr[3] == cdr[4]:
        ans = cdr[2]*3
    elif cdr[0] == cdr[1] == cdr[2]:
        ans = cdr[0]*3
    else:
        ans = 0
    return ans


print("The game of Yahtzee begins!")

user_choice_info = 'When prompted to choose which dice to roll, please write the' \
' letter "D" followed by the number of the dice you want to roll.' \
' If you want to roll multiple dice, separate your choices with white space.' \
' For example, write "D1 D2 D5" if you want to roll dice 1, 2 and 5' \
' Alternatively, press enter without writing anything to skip the turn.'

print("")
print(user_choice_info)

run_game = True
while run_game:
    
    # Podczas pierwszej tury użytkownik musi rzucić wszystkimi pięcioma kośćmi
    current_dice_rolls = roll_dice([], [0, 1, 2, 3, 4])
    print("")
    print("Your current dice rolls: " + str(current_dice_rolls))
    
    # Gdy kości zostały rzucone choć raz, użytkownik będzie mógł wybrać, którymi
    # kośćmi chce rzucić na dwoch następnych turach.
    for i in range(2):
        
        # Tutaj zdobędziemy decyzję od użytkownika
        user_choice = input('Please choose which dice you want to roll again: ')
        dice_to_roll = convert_user_input_to_dice_indices(user_choice)
        current_dice_rolls = roll_dice(current_dice_rolls, dice_to_roll)
        print("Your current dice rolls: " + str(current_dice_rolls))
    
    # Jeżeli wszystki 3 tury zostały wykonane, należy obliczyć ostateczny wynik
    current_score = calculate_score(current_dice_rolls)
    print("Your score for this round is: " + str(current_score))
    
    # Gdy runda się skończyła, pytamy użytkownika czy chce zagrać ponownie
    continue_game = input("Do you want to play again? (yes/no)")
    while continue_game not in ["yes", "no"]:
        print('Invalid option. Please write "yes" or "no"')
        continue_game = input("Do you want to play again? (yes/no)")
    
    # Jeżeli użytkownik nie chce już grać, zmienna run_game będzie równa `False`
    # co sprawi, że na przed następną iteracją pętli, Python wyjdzie z pętli i zakończy program
    if continue_game == "no":
        run_game = False