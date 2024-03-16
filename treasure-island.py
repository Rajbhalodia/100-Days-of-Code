print("Welcome to the treasure Island")
print("Your Mission is to Find the treasure")

choice01 = (input('You are at a Crossroad. Where do you want to go ? Type "Left" or "Right". \n')).lower()
if choice01 == "left":
    choice02 = (input('You can see an island accross the Lake. Type "Wait" to wait for a boat,"Swim" to swim accross the lake \n')).lower()
    if choice02 == "wait":
        choice03 = input('You have arrieved at the Island Unharmed Please Enter the Door you choose "RED","YELLOW","GREEN" \n').lower()
        if choice03 == "yellow":
            print('7 crore aapke hua mahashai')
        else:
            print('YOU HAVE SELECTED THE WRONG DOOR. TRY AGAIN')
    else:
        print('THE LAKE WAS FILLED WITH SNAKES AND CROCODILES')
else:
    print ('You Fell into a Hole. Your Game has ended.')