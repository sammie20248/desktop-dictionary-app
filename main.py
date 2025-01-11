from japanese import japanese_dictionary_app
from german import german_dictionary_app
from italian import italian_dictionary_app

def main():
    combined_dictionary = {}

    while True:
        print("\nWelcome to this Multi-Lingual Dictionary!")
        print("Select a dictionary:")
        print("1. Japanese")
        print("2. German")
        print("3. Italian")
        print("4. Spanish (coming soon)")
        print("5. French (coming soon)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print("\nYou selected Japanese.")
            japanese_data = japanese_dictionary_app()  
            combined_dictionary.update(japanese_data)  

        elif choice == "2":
            print("\nYou selected German.")
            german_data = german_dictionary_app()  
            combined_dictionary.update(german_data)  

        elif choice == "3":
            print("\nYou selected Italian.")
            italian_data = italian_dictionary_app()  
            combined_dictionary.update(italian_data)  

        elif choice == "4":
            print("Sorry, the Spanish dictionary is not available yet. Coming soon!")

        elif choice == "5":
            print("Sorry, the French dictionary is not available yet. Coming soon!")

        elif choice == "6":
            print("You are exiting the program now!")
            print("\nFinal Combined Dictionary:")
            for key, value in combined_dictionary.items():
                print(f"{key}: {value}")
            break

        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
