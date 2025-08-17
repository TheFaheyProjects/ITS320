#Kyle Fahey
#Critical Thinking: Module 5
#ITS320-1

#Library Management System

#Library Inventory
libraryInventory = []

#User Input Validation
def getUserInput(prompt):
    while True:
        userInput = input(prompt)
        if userInput:
            return userInput
        print("You have not entered anything. Please try again.")

#Book Copies
def bookNumberOfCopies(prompt):
    while True:
        try:
            numberOfCopies = int(input(prompt))
            if numberOfCopies > 0:
                return numberOfCopies
            else:
                print("The number of books must be positive. It can't be negative.")
        except ValueError:
            print("Please enter a valid number.")
            
#Functions for Displaying "Add a Book", "Borrow a Book", "Return a Book", and "Display Inventory"

#Adding a Book
def addNewBook():
    print("\n---- Add New Book ----")
    title = getUserInput("Enter the Books Title: ")
    author = getUserInput("Enter the Books Author: ")
    copies = bookNumberOfCopies("Enter the Number of Copies for the Book: ")
    
    #Does this Book Already Exist?
    for book in libraryInventory:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            book["copies"] += copies
            print(f"\nBook '{title}' updated. Total Current Copies: {book['copies']}")
            return
    
    #Adding a New Book
    newBook = {"title": title, "author": author, "copies": copies}
    libraryInventory.append(newBook)
    print(f"Book '{title}' by {author}, has been added with {copies} copies.")
    
#Borrowing a Book
def borrowingABook():
    print("\n---- Borrow A Book ----")
    title = getUserInput("Please enter the title of the book you wish to borrow: ")
    
    for book in libraryInventory:
        if book["title"].lower() == title.lower():
            if book["copies"] > 0:
                book["copies"] -= 1
                print(f"You have successfully borrowed '{book['title']}'.")
                return
            else:
                print("Sorry that book is not currently in stock.")
    print("This book does not exist in our inventory.")
    
#Returning a Book
def returningABook():
    print("\n---- Return A Book ----")
    title = getUserInput("Please enter the title of the book you wish to return: ")
        
    for book in libraryInventory:
        if book["title"].lower() == title.lower():
            book["copies"] += 1
            print("You have returned the book successfully.")
            return
    print("We don't seem to have this book in our inventory. Please add it as a new book.")
    
#Displaying the Current Inventory
def displayCurrentBookInventory():
    print("\n---- Current Inventory ----")
    if not libraryInventory:
        print("The Library is Currently Empty. You can check back later.")
    else:
        for idx, book in enumerate(libraryInventory, 1):
            print(f"{idx}. Title: {book['title']}, Author: {book['author']}, Copies: {book['copies']}")

#Program Main Menu
def mainMenu():
    while True:
        print("\n---- Library Management System ----")
        print("1. Add New Book")
        print("2. Borrow A Book")
        print("3. Return A Book")
        print("4. Display Inventory")
        print("5. Exit The Program")
        
        #User Input for The Menu
        userChoice = int(input("\nPlease make a select from the Menu. Enter a number between 1 and 5: "))
        
        #Menu Logic
        if userChoice == 1:
            addNewBook()
        elif userChoice == 2:
            borrowingABook()
        elif userChoice == 3:
            returningABook()
        elif userChoice == 4:
            displayCurrentBookInventory()
        elif userChoice == 5:
            print("Thanks for using the Library Management System! See you next time!")
            break
        else:
            print("That is an invalid choice. Please select a number between 1 and 5.")
            
#Runnig the Program
if __name__ == "__main__":
    mainMenu()