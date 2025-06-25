import random   # Import random module to shuffle the flashcards order

# Create an empty list to store flashcards
# Each flashcard is a dictionary containing a 'question' and its corresponding 'answer'
flashcards = []

def add_flashcard():
    """Function to add a new flashcard with a question and answer."""
    print("\n--- Add a New Flashcard ---")

    # Prompt the user to enter a question, remove extra spaces from input
    question = input("Enter the question: ").strip()
    # Validate that the question is not empty
    if question == "":
        print("Question cannot be empty.")
        return  # Exit the function early if invalid

    # Prompt the user to enter the answer, remove extra spaces
    answer = input("Enter the answer: ").strip()
    # Validate that the answer is not empty
    if answer == "":
        print("Answer cannot be empty.")
        return  # Exit the function early if invalid

    # Create a new flashcard as a dictionary and add it to the flashcards list
    flashcards.append({"question": question, "answer": answer})
    print("✅ Flashcard added successfully!")  # Confirm addition to user

def take_quiz():
    """Function to conduct the quiz, ask questions, accept answers, and track score."""
    print("\n--- Quiz Time! ---")

    # Check if there are any flashcards to quiz on
    if not flashcards:
        print("No flashcards found. Please add some first.")
        return  # Exit if no flashcards are available

    # Make a copy of flashcards to shuffle without changing the original list order
    quiz_cards = flashcards.copy()
    random.shuffle(quiz_cards)  # Shuffle questions to randomize quiz order

    score = 0  # Variable to keep track of correct answers
    skipped_cards = []  # List to store flashcards that the user chooses to skip

    # First pass: ask each question in shuffled order
    for card in quiz_cards:
        print("\nQuestion:", card["question"])  # Display the question
        print("Type 'skip' to move to the next question.")  # Inform user about skip option

        user_answer = input("Your answer: ").strip()  # Get user's answer

        if user_answer.lower() == "skip":  # If user chooses to skip
            print("Question skipped.")  # Notify that question is skipped
            skipped_cards.append(card)  # Add skipped card to review later
            continue  # Move to next flashcard without scoring

        # Check if the user's answer matches the correct answer (case-insensitive)
        if user_answer.lower() == card["answer"].strip().lower():
            print("✅ Correct!")  # Correct answer feedback
            score += 1  # Increase score
        else:
            # Show correct answer if user's answer was incorrect
            print(f"❌ Incorrect. The correct answer was: {card['answer']}")

    # Second pass: review skipped questions to give user another chance
    if skipped_cards:
        print("\n--- Review Skipped Questions ---")
        for card in skipped_cards:
            print("\nQuestion:", card["question"])  # Display skipped question again
            user_answer = input("Your answer: ").strip()  # Get user's second attempt answer

            # Check answer correctness on second attempt
            if user_answer.lower() == card["answer"].strip().lower():
                print("✅ Correct!")  # Positive feedback
                score += 1  # Add to score
            else:
                print(f"❌ Incorrect. The correct answer was: {card['answer']}")  # Show correct answer

    total_cards = len(flashcards)  # Total number of flashcards the user has
    percentage = (score / total_cards) * 100  # Calculate percentage score
    # Display final score summary to user
    print(f"\nFinal score: {score} / {total_cards} correct ({percentage:.1f}%).")

def show_menu():
    """Main menu that lets the user add flashcards, take a quiz, or exit."""
    while True:  # Loop until the user decides to exit
        print("[PRIVACY - No user data will be saved]") #
        print("\nFlashcard Quiz Menu")
        print("1. Add flashcard")  # Option to add a new flashcard
        print("2. Take quiz")      # Option to start the quiz
        print("3. Exit")           # Option to exit the program

        choice = input("Choose an option (1-3): ").strip()  # Get user's menu choice

        if choice == "1":
            add_flashcard()  # Call function to add a flashcard
        elif choice == "2":
            take_quiz()  # Call function to start the quiz
        elif choice == "3":
            print("Goodbye!")  # Exit message
            break  # Exit the menu loop and end the program
        else:
            print("Invalid choice. Try again.")  # Handle invalid inputs gracefully

# Start the program by running the menu function
show_menu()