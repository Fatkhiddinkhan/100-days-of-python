#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
invited_name = []
with open("./input/Names/invited_names.txt") as names:
    for name in names:
        name = name.strip()
        invited_name.append(name)

print(invited_name)

with open("./input/Letters/starting_letter.txt", mode="r") as invitation:
    temp_invitation = invitation.read()
    for name in invited_name:
        personalized = temp_invitation.replace('[name]', name.strip())

        with open(f"./Output/ReadyToSend/invitation_for_{name.strip()}.txt", mode="w") as output:
            output.write(personalized)
