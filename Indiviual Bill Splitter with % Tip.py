amount = (int(input('OH HI THERE PLEASE ENTER YOUR TOTAL BILLING AMOUNT:- $')))

split_between = (int(input("ENTER THE NUMBER OF FRIENDS WITH WHO YOU HAD DINNER:- ")))

tip_input = (int(input("PLEASE ENTER HOW MUCH PERCENTE WOULD YOU LIKE TO TIP 5,10,15,20,25:- ")))

total_amout = (amount*tip_input)/100

individual_split = total_amout/split_between

print ('PER PERSON SPLIT = $', individual_split )
