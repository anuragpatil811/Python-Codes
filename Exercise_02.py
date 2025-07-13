#WAP to calculate Dog's age. Assume Dog first 2 years = 10 Human Years, then Dog's 2 years = Human 1 Year
#humanyear = input("Enter Human Years: ")

#if humanyear.isdigit():  # Check if input is a positive number
#    humanyear = int(humanyear)   
#    if humanyear <= 2:
#        dogyear = humanyear * 5
#    else:
#        dogyear = 10 + (humanyear - 2) * 2
#    print(f"For Human year {humanyear}, Dog is {dogyear} years old")
#else:
#    print("Invalid input! Please enter a positive number.")

#WAP: to calculate number of notes in amount
#amount = 1050
#print(amount//500)
#print(amount%200)
count = {}
notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
amount = int(input("Enter your amount:"))
#for note in notes:
#    if amount != 0:
#         if amount >= note:
#             temp = amount // note
#             count[note] = temp
#             amount = amount % note
#print(count)
def notecount(count, notes, amount):
    for note in notes:
        if amount != 0:
            if amount >= note:
                temp = amount // note
                count[note] = temp
                amount = amount % note
notecount(count, notes, amount)

print(f"For Transaction of {amount} you required {count}")

#    if amount >= note:
#       temp = amount // note
#       count[note] = temp
#print(count)

