from tkinter import Tk, Entry, Button, Label, StringVar,Toplevel

window = Tk()
window.geometry("600x250")
window.title("French Dictionary")

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

french_dict = {
    "good morning" : "Bonjour",
    "good evening" : "Bonsoir",
    "goodbye" : "Au revoir",
    "hi" : "Salut",
    "hello" : "Coucou",
    "see you later" : "a plus tard",
    "see you soon" : "a bientot",
    "goodnight" : "Bonne nuit",
    "thank you" : "Merci",
    "please" : "Sil vous plait",
    "0" : "Zero",
    "1" : "Un",
    "2" : "Deux",
    "3" : "Trios",
    "4" : "Quatre",
    "5" : "Cinq",
    "6" : "Seize",
    "7" : "Sept",
    "8" : "Huit",
    "9" : "Nuef",
    "10" : "Dix",
    "11" : "Onze",
    "12" : "Douze",
    "13" : "Trieze",
    "14" : "Quatorze",
    "15" : "Quinze",
    "16" : "Seize",
    "17" : "Dix-sept",
    "18" : "Dix-huit",
    "19" : "Dix-neuf",
    "20" : "Vingt",
    "red" : "Rouge",
    "gray" : "Gris",
    "pink" : "Rose",
    "black" : "Noir",
    "brown" :  "Marrow",
    "blue" :  "Bleu",
    "green" : "Vert",
    "white" : "Blanc",
    "yellow" : "Jaunce",
    "purple" : "Pourpre",
    "cat" : "Chat",
    "dog" : "Chien",
    "lion" : "Le lion",
    "goldfish" : "Un poisson rouge",
    "mouse" :"Une souris",
    "turtle" : "Une tujrtle",
    "rabbit" : "Un lapin",
    "wolf" : "Le loup",
    "monkey" : "Le singe",
    "hamster" : "Un hamster",
    "avec" : "With",
    "love" : "Amour",
    "happiness" : "Bonheur",
    "girl" : "La fille",
    "boy" : "La garcon",
    "beach" : "La plage",
    "subway" : "Metro",
    "car" : "Voiture",
    "wine" : "Vin",
    "bread" : "Pain",
    "ticket" : "Billet",
    "meat" : 'Viande'
}

def search(word):
    if word in french_dict:
        result.set(french_dict[word])
        print(french_dict[word])
    else:
        result.set("Word Not Found")

search_btn = Button(window, text="Search", command=lambda: search(entry_text.get()))
search_btn.pack()

window.mainloop()
