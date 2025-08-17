#Kyle Fahey
#ITS320-1
#Critical Thinking: Module 4

#Voting Registration System

#List of Candidates
officialCandidates = ["Alice", "Bob", "Charlie"]

#Registered Voters
officialVoters = []

#Loop for the Main Menu
while True:
    print("\n---Voting Registration System Menu---")
    print("1. Register a New Voter")
    print("2. Display All Registered Voters")
    print("3. Search for a Voter by Voter ID")
    print("4. Exit the Program")

    #Main Menu Selection
    try:
        menuSelection = int(input("\nSelect a Number between 1 and 4: "))
    except ValueError:
        print("That is not a valid selection. Please enter a Number between 1 and 4.")
        continue

    #Registering a New Voter | Menu Option 1
    if menuSelection == 1:
        while True:
            #Voter Information
            nameOfVoter = ""
            ageOfVoter = 0
            candidateOfVoter = ""
            idOfVoter = ""

            #Name of Voter
            while True:
                nameOfVoter = input("\nEnter the Voters Full Name: ")
                if nameOfVoter != "":
                    break
                else:
                    print("The Name is currently empty. Please enter in the Voters full name.")

            #Age of Voter
            while True:
                voterAgeInput = input("Enter the Voters Age: ")
                if voterAgeInput.isdigit():
                    ageOfVoter = int(voterAgeInput)
                    if ageOfVoter >= 18 and ageOfVoter <= 120:
                        break
                    else:
                        print("The Voters Age must be between 18 and 120.")
                else:
                    print("Please enter a valid number for the Age of the Voter.")

            #The Candidate of the Voter
            while True:
                candidateOfVoter = input("Please select a candidate from the following list. Alice, Bob, or Charlie: ")
                if candidateOfVoter in officialCandidates:
                    break
                else:
                    print("That is not a valid candidate. Please choose between Alice, Bob, or Charlie.")

            #ID of Voter
            while True:
                idOfVoter = input("Please enter a unique Voter ID that is alphanumeric: ")
                if idOfVoter != "" and idOfVoter.isalnum():
                    #Does the VoterID already exist?
                    registeredVoterID = False
                    for voter in officialVoters:
                        if voter["VoterID"] == idOfVoter:
                            registeredVoterID = True
                            break
                    if registeredVoterID:
                        print("This VoterID is already in use and has been registered. Please enter a new ID.")
                    else:
                        break
                else:
                    print("Please enter a VoterID and ensure that it is alphanumeric.")
        
            #Storing the Voters Data
            votersData = {
                "Name": nameOfVoter,
                "Age": ageOfVoter,
                "Candidate": candidateOfVoter,
                "VoterID": idOfVoter
            }

            #Add Voter Data to Offical Voters
            officialVoters.append(votersData)
            print("\nVoter was Registered Successfully!")

            #Do you want to Register another Voter?
            registerAnotherVoter = input("\nWould you like to Register another Voter? Please enter Yes or No: ").lower()
            if registerAnotherVoter != "yes":
                break
    
    #Displaying all Registered Voters | Menu Option 2
    elif menuSelection == 2:
        if len(officialVoters) == 0:
            print("\nNo Voters have been Registered yet. Please check back later.")
        else:
            print("\n---Registered Voters---")
            for registeredVoter in officialVoters:
                print("Name:", registeredVoter["Name"])
                print("Age:", registeredVoter["Age"])
                print("Candidate:", registeredVoter["Candidate"])
                print("Voter ID:", registeredVoter["VoterID"])
                print("\n")
    
    #Searching for a Voter by their VoterID | Menu Option 3
    elif menuSelection == 3:
        while True:
            idSearch = input("\nPlease enter the Voter ID that you want to search for: ")
            voterIDFound = False
            for registeredVoter in officialVoters:
                if registeredVoter["VoterID"] == idSearch:
                    print("\n---Voter Found---")
                    print("Name:", registeredVoter["Name"])
                    print("Age:", registeredVoter["Age"])
                    print("Candidate:", registeredVoter["Candidate"])
                    print("Voter ID:", registeredVoter["VoterID"])
                    print("\n")
                    voterIDFound = True
                    break
            if not voterIDFound:
                print("\nThere is no Voter with this Voter ID Registered.")
        
            #Do you want to Search another Voter ID?
            searchAnotherVoterID = input("Would you like to Search for another Voter ID? Please enter Yes or No: ").lower()
            if searchAnotherVoterID != "yes":
                break
    
    #Exiting the Progam | Menu Option 4
    elif menuSelection == 4:
        print("\nThank you for using the Voter Registration System. See you next time!")
        break
    
    #Handling an Invalid Menu Option
    else:
        print("Your selection is invalid. Please enter a number between 1 and 4.")