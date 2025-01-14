from tkinter import *
from spanish import SPANISH_DICT
from german import german_dictionary_app
from french import french_dict
from italian import italian_dictionary_app
from japanese import japanese_dictionary_app



def main():

    window = Tk()
    window.title("Multilingual Dictionary")
    window.geometry("560x550")
    window.config(bg="white")


    window.eval('tk::PlaceWindow . center')


    title_label = Label(window, text="Multilingual Dictionary", font=("Arial", 23, "bold"), bg="#f5f5f5", fg= "black")
    title_label.pack(pady=20)


    feedback_label = Label(window, text="", font=("Arial", 12), bg="black", fg="red")
    feedback_label.pack(pady=10)

    
    def open_dictionary(dictionary_app, name):
        try:
            feedback_label.config(text=f"Opening {name} Dictionary...")
            window.withdraw()
            dictionary_app()
            window.deiconify()
        except Exception as e:
            feedback_label.config(text=f"Error: {e}")


    Button(window, text="Spanish Dictionary", font=("Arial", 14), bg="orange", fg="white", width=25,
           command=lambda: open_dictionary(SPANISH_DICT, "Spanish")).pack(pady=10)

    Button(window, text="german Dictionary", font=("Arial", 14), bg="orange", fg="white", width=25,
           command=lambda: open_dictionary(german_dictionary_app, "german")).pack(pady=10)

    Button(window, text="french Dictionary", font=("Arial", 14), bg="orange", fg="white", width=25,
           command=lambda: open_dictionary(french_dict, "french")).pack(pady=10)

    Button(window, text="italian Dictionary", font=("Arial", 14), bg="orange", fg="white", width=25,
           command=lambda: open_dictionary(italian_dictionary_app, "italian")).pack(pady=10)

    Button(window, text="Japanese Dictionary", font=("Arial", 14), bg="orange", fg="white", width=25,
           command=lambda: open_dictionary(japanese_dictionary_app(), "Japanese")).pack(pady=10)


    Button(window, text="Exit", font=("Arial", 14), bg="green", fg="white", width=25, command=window.destroy).pack(pady=20)


    window.mainloop()


if __name__ == "__main__":
    main()
