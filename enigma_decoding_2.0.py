# decoding of enigma

import tkinter as tk

# start values for enigma wheels 
turn_count_EW1 = 0 
turn_count_EW2 = 0 
turn_count_EW3 = 0



def process_of_decoding():
    # values for replacement of numbers & special characters
    symbolcodes = [["x","d","y","e","z","f"], ["x","h","y","i","z","j"], ["x","k","y","l","z","m"], ["x","n","y","o","z","p"], ["x","q","y","r","z","s"], ["x","t","y","u","z","v"], ["x","w","y","x","z","y"], ["x","z","y","a","a","z","b","b"], ["x","c","c","y","d","d","z","e","e"], ["x","f","f","y","h","h","z","i","i"], ["x","a","y","b","z","c"], ["x","j","j","y","k","k","z","l","l"], ["x","m","m","y","n","n","z","o","o"], ["x","p","p","y","q","q","z","r","r"], ["x","s","s","y","t","t","z","u","u"], ["x","v","v","y","w","w","z","x","x"]]
    symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ", ".", "?", "!", ":", ","]
    
    # creation of main list, alphabet
    processing_list = []
    Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # enigma wheels
    enigma_wh_1 = ['_', 6, 11, 4, 10, 8, 12, 2, 9, 5, 23, 1, 13, 7, 24, 21, 18, 19, 16, 26, 20, 14, 25, 15, 17, 22, 3]
    enigma_wh_2 = ['_', 17, 5, 9, 26, 16, 8, 22, 13, 14, 1, 19, 2, 10, 18, 3, 25, 4, 12, 24, 21, 6, 20, 7, 23, 15, 11]
    enigma_wh_3 = ['_', 26, 15, 9, 5, 3, 12, 23, 17, 19, 14, 7, 10, 1, 24, 11, 25, 4, 20, 22, 6, 18, 13, 2, 21, 16, 8]

    # function to exchange numbers and letters
    def replace_letters_numbers_in_list(list, replace_element, new_element):
        return [new_element if item == replace_element else item for item in list]

    # function for decoding
    def decoding_process():
        global turn_count_EW1
        global turn_count_EW2
        global turn_count_EW3
        return_val_a = enigma_wh_3[processing_list[i]]
        return_val_b = enigma_wh_2[return_val_a]
        return_val_c = enigma_wh_1[return_val_b]
        processing_list[i] = return_val_c
        switch_variables_1 = enigma_wh_1.pop()
        enigma_wh_1.insert(1,switch_variables_1)
        turn_count_EW1 = turn_count_EW1 + 1
        if turn_count_EW1 == 26:
            turn_count_EW1 = 0
            switch_variables_2 = enigma_wh_2.pop()
            enigma_wh_2.insert(1,switch_variables_2)
            turn_count_EW2 = turn_count_EW2 + 1
        if turn_count_EW2 == 26:
            turn_count_EW2 = 0
            switch_variables_3 = enigma_wh_3.pop()
            enigma_wh_3.insert(1,switch_variables_3)
            turn_count_EW3 = turn_count_EW3 + 1  
        if turn_count_EW3 == 26:
            print("Eingabe zu Lang") 

    # function to replace symbolcodes with respective special characters
    def rereplacer_of_special_characters(symbol ,symbolcode):   
        indexes = []
        for i in range(len(processing_list)):
            if processing_list[i:i+len(symbolcode)] == symbolcode:
                indexes.append((i, i+len(symbolcode)))
        a = len(indexes)
        while a >= 0:
            a = a-1
            if a == -1:
                break
            BeginSymbolInd = indexes[a][0]
            EndSymbolInd = indexes[a][-1]
            while EndSymbolInd > BeginSymbolInd:
                EndSymbolInd = EndSymbolInd-1
                processing_list.pop(EndSymbolInd)
            processing_list.insert(BeginSymbolInd,symbol)  	

        
    # main process


    # retrieval of user input
    tk.Label(mask, text="Decoded text:").grid(row=10)
    output = tk.Entry(mask, width = 80)
    output.grid(row=10, column=1)
    input_string = (entry.get())

    # creation of list from input string
    processing_list[:0] = input_string

    # replacement of letters with numbers  
    for i in range(26):
        processing_list = replace_letters_numbers_in_list(processing_list, Alphabet[i], i+1)

    # Enigma decoding_process (see decoding_process())    
    for i in range(len(processing_list)):
        decoding_process()
       

    # replacement of numbers with letters   
    for i in range(26):
        processing_list = replace_letters_numbers_in_list(processing_list, i+1, Alphabet[i])

    # replacement of special characters/number
    for i in range(16):
        rereplacer_of_special_characters(symbols[i],symbolcodes[i])
   


    # merging list and output
    output_string = "".join(processing_list)
    output.insert(0, output_string)
        
mask = tk.Tk()
mask.geometry("650x250")
mask.title("Decoding of Engima")
tk.Label(mask, text="Enter encoded text:").grid(row=0)
entry = tk.Entry(mask, width = 80)
entry.grid(row=0, column=1)

tk.Button(mask, text="End", command=mask.quit).grid(row=250, column=0, sticky=tk.W, pady=20)
tk.Button(mask, text="Decode", command=process_of_decoding).grid(row=8, column=0, sticky=tk.W, pady=20)

mask.mainloop()