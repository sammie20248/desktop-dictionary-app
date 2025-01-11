
from tkinter import *
from spanish import spanish_dictionary_app  
from Italian import  Italian_dictionary_app  
from french import french_dictionary_app  
from german import german_dictionary_app  
from japanese import japanese_dictionary_app  


def main():
    
    window = Tk()
    window.title("Multilingual Dictionary")
    window.geometry("600x550")
    window.config(bg="#f5f5f5")  

    
    window.eval('tk::PlaceWindow . center')

    
    title_label = Label(window, text="Multilingual Dictionary", font=("Arial", 25, "bold"), bg="#f5f5f5", fg= "black")
    title_label.pack(pady=20)

    
    subtitle_label = Label(window, text="Select a dictionary to Explore!", font=("Arial", 14), bg="#f5f5f5", fg="black")
    subtitle_label.pack(pady=10)

    
    feedback_label = Label(window, text="", font=("Arial", 12), bg="#f5f5f5", fg="red")
    feedback_label.pack(pady=10)

    
    def open_dictionary(dictionary_app, name):
        try:
            feedback_label.config(text=f"Opening {name} Dictionary...")
            window.withdraw()  
            dictionary_app()  
            window.deiconify()  
        except Exception as e:
            feedback_label.config(text=f"Error: {e}")

    
    Button(window, text="Spanish Dictionary", font=("Arial", 14), bg="#4b0082", fg="white", width=25,
           command=lambda: open_dictionary(spanish_dictionary_app, "Spanish")).pack(pady=10)

    Button(window, text="german Dictionary", font=("Arial", 14), bg="#4b0082", fg="white", width=25,
           command=lambda: open_dictionary(german_dictionary_app, "german")).pack(pady=10)

    Button(window, text=" Italian Dictionary", font=("Arial", 14), bg="#4b0082", fg="white", width=25,
           command=lambda: open_dictionary(  Italian_dictionary," Italian")).pack(pady=10)

    Button(window, text="french Dictionary", font=("Arial", 14), bg="#4b0082", fg="white", width=25,
           command=lambda: open_dictionary(french_dictionary_app, "french")).pack(pady=10)

    Button(window, text="Japanese Dictionary", font=("Arial", 14), bg="#4b0082", fg="white", width=25,
           command=lambda: open_dictionary(japanese_app, "Japanese")).pack(pady=10)

    
    Button(window, text="Exit", font=("Arial", 14), bg="#dc143c", fg="white", width=25, command=window.destroy).pack(pady=20)

    
    window.mainloop()


if __name__ == "__main__":
    main()
