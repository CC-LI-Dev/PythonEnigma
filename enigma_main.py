import tkinter as tk
from enigma_decoding import *
from enigma_encoding import *

def encoding_button():
    # retrieval of encoding user input and creation of ouput field
    tk.Label(mask, text="Kodierter Text:", font=("Arial", 11)).grid(row=14)
    output_encoding = tk.Entry(mask, width = 160)
    output_encoding.grid(row=14, column=1)
    input_string = (entry_encoding.get())
    output_string = process_of_encoding(input_string)
    output_encoding.insert(0, output_string)


def decoding_button():
    # retrieval of decoding user input and creation of ouput field
    tk.Label(mask, text="Dekodierter Text:", font=("Arial", 11)).grid(row=20)
    output_decoding = tk.Entry(mask, width = 160)
    output_decoding.grid(row=20, column=1)
    input_string = (entry_decoding.get())
    output_string = process_of_decoding(input_string)
    output_decoding.insert(0, output_string)


# main window
mask = tk.Tk()
mask.geometry("1450x600")
mask.title("Enigma")
tk.Label(mask).grid(row=0)
tk.Label(mask, text="Die Enigma", font=("Arial", 13, tk.UNDERLINE)).grid(row=1, column=1)
tk.Label(mask, text="Sie können unten einen beliebigen Text mit einem Verfahren, welches an die Enigma angelehnt ist, kodieren und wieder dekodieren.", font=("Arial", 11)).grid(row=2, column=1)
tk.Label(mask).grid(row=3)
tk.Label(mask, text="Regeln:", font=("Arial", 11)).grid(row=4, column=1)
tk.Label(mask, text="1. Jeder Buchstabe außer 'ß' und jede Zahl kann verwendet werden.", font=("Arial", 11)).grid(row=5, column=1)
tk.Label(mask, text="2. Die Sonderzeichen '.?!:,' sowie Leerzeichen sind verfügbar.", font=("Arial", 11)).grid(row=6, column=1)
tk.Label(mask, text="3. Die Buchstaben 'ä', 'ö' und 'ü' sind durch jeweils 'ae', 'oe' und 'ue' zu ersetzen.", font=("Arial", 11)).grid(row=7, column=1)
tk.Label(mask).grid(row=8)


# encoding section
tk.Label(mask).grid(row=9)
tk.Label(mask, text="Kodierung:", font=("Arial", 11, tk.UNDERLINE)).grid(row=10, column=1)
tk.Label(mask).grid(row=11)
tk.Label(mask, text="Geben Sie ihren Text ein:", font=("Arial", 11)).grid(row=12)
entry_encoding = tk.Entry(mask, width = 160)
entry_encoding.grid(row=12, column=1)

tk.Button(mask, text="Kodieren", command=encoding_button, font=("Arial", 11)).grid(row=13, column=0, sticky=tk.W, pady=20)

# decoding section
tk.Label(mask).grid(row=15)
tk.Label(mask, text="Dekodierung:", font=("Arial", 11, tk.UNDERLINE)).grid(row=16, column=1)
tk.Label(mask).grid(row=17)
tk.Label(mask, text="Geben Sie den kodierten Text ein:", font=("Arial", 11)).grid(row=18)
entry_decoding = tk.Entry(mask, width = 160)
entry_decoding.grid(row=18, column=1)

tk.Button(mask, text="Dekodieren", command=decoding_button, font=("Arial", 11)).grid(row=19, column=0, sticky=tk.W, pady=20)




tk.Button(mask, text="Beenden", command=mask.quit, font=("Arial", 11)).grid(row=5000, column=2, sticky=tk.W, pady=20)

mask.mainloop()










