# This program lets the user create flashcards and quiz themselves

# Create an empty list to store flashcards
# Each flashcard will be a dictionary with a 'question' and an 'answer'
flashcards = []

# This function allows the user to create a new flashcard
def add_flashcard():
    print("\n--- Add a New Flashcard ---")

    # Asks the user to enter a question
    question = input("Enter the question: ")

    # Asks the user to enter the answer to the question
    answer = input("Enter the answer: ")

    # Creates a dictionary to store the flashcard
    flashcard = {
        "question": question,
        "answer": answer
    }

    # Adds the new flashcard to the flashcards list
    flashcards.append(flashcard)

    # Lets the user know it was saved
    print("Flashcard added successfully!")

# This function runs the quiz, asking all flashcards and checking answers
def take_quiz():
    print("\n--- Quiz Time! ---")

    # Check if there are flashcards to quiz
    if len(flashcards) == 0:
        print("No flashcards found. Please add some first.")
        return  # Exit quiz if no cards

    score = 0  # Track number of correct answers

    # Loop through each flashcard in the list
    for card in flashcards:
        print("\nQuestion: " + card["question"])
        print("Type 'skip' to move to the next question.")  # Tell user how to skip

        user_answer = input("Your answer: ").strip()

        # Allow user to skip question
        if user_answer.lower() == "skip":
            print("Question skipped.")
            continue  # Move on to next flashcard

        # Check if the answer matches (case-insensitive, ignoring spaces)
        if user_answer.lower() == card["answer"].strip().lower():
            print("✅ Correct!")
            score += 1  # Increase score for correct answer
        else:
            print(f"❌ Incorrect. The correct answer was: {card['answer']}")

    # After all questions, show the final score
    print(f"\nYou got {score} out of {len(flashcards)} correct.")

# Define a function that shows a menu and handles user input
def show_menu():
    # This loop will keep showing the menu until the user chooses to exit
    while True:
        print("\nFlashcard Quiz Menu")
        print("1. Add flashcard")   # Option to make a new flashcard
        print("2. Take quiz")       # Option to test yourself
        print("3. Exit")            # Option to quit the program

        # Ask the user to pick one of the options
        choice = input("Choose an option (1-3): ")

        # If the user picks option 1, the program will let them add a flashcard
        if choice.strip() == "1":
            add_flashcard()

        # If the user picks option 2, the program will start a quiz
        elif choice.strip() == "2":
            take_quiz()  # Run the quiz function

        # If the user picks option 3, the program should end
        elif choice.strip() == "3":
            print("Goodbye!")  # Say goodbye
            break              # This stops the loop and exits the program

        # If the user types something invalid (not 1, 2, or 3)
        else:
            print("Invalid choice. Try again.")  # Show an error message

# Start the program by calling the menu function
show_menu()
