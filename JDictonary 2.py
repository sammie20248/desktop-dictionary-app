from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("700x250")
window.title("Italian Dictionary")

entry_text= Entry(window)
entry_text.pack()
result=StringVar()
result_label= Label(window,textvariable=result)
result_label.pack()

Italian_dictionary={
'Car': 'Coche',
    'Sister': 'Hermana',
    'Father':'Padre',
    'Map':'Mapa',
    'Beer':'Cerveza',
    'Family':'Familia',
    'Hello':'Hola',
    'Taxi':'Taxi',
    'Goodbye':'Adios',
    'Four':'Cuatro',
    'Music':'Musica',
    'Tres':'Three',
    'Mother':'Madre',
    'Thank You':'Gracias',
    'Bus':'Autobus',
    'Party':'Fiesta',
    'One':'Uno',
    'Food':'Comida',
    'Brother':'Hermano'

                    }
def search(word):
    if word in Italian_dictionary:
        result.set(Italian_dictionary[word])
        print(Italian_dictionary)
    else:
        result.set("Not Found")
        print("Not Found")

search_btn = Button(window, text="search",command=lambda: search(entry_text.get()))
search_btn.pack()
window.mainloop()