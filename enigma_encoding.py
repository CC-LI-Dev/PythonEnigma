# encoding of enigma 

import tkinter as tk

# count of turns for enigma wheels
turn_count_EW1 = 0 
turn_count_EW2 = 0 
turn_count_EW3 = 0



def process_of_encoding(input_string):
    #vales for encoding of symbols and special characters 
    # " " = xaybzc ; "1" =  xdyezf; "2" =  xhyizj; "3" =  xkylzm; "4" =  xnyozp; "5" =  xqyrzs;
    #  "6" =  xtyuzv; "7" =  xwyxzy; "8" =  xzyaazbb; "9" =  xccyddzee; "0" =  xffyhhzii; "." = xjjykkzll; 
    # "?" = xmmynnzoo; "!" = xppyqqzrr; ":" = xssyttzuu; "," = xvvywwzxx; 

    symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ", ".", "?", "!", ":", ","]

    # encoding of special characters

    def replace_symbols(symbol, symbolindex):
        if symbol == "1":
            processing_list[symbolindex:symbolindex] = ["x", "d", "y", "e", "z", "f"]
        elif symbol == "2":
            processing_list[symbolindex:symbolindex] = ["x", "h", "y", "i", "z", "j"] 
        elif symbol == "3":
            processing_list[symbolindex:symbolindex] = ["x", "k", "y", "l", "z", "m"]  
        elif symbol == "4":
            processing_list[symbolindex:symbolindex] = ["x", "n", "y", "o", "z", "p"]  
        elif symbol == "5":
            processing_list[symbolindex:symbolindex] = ["x", "q", "y", "r", "z", "s"]    
        elif symbol == "6":
            processing_list[symbolindex:symbolindex] = ["x", "t", "y", "u", "z", "v"]    
        elif symbol == "7":
            processing_list[symbolindex:symbolindex] = ["x", "w", "y", "x", "z", "y"]   
        elif symbol == "8":
            processing_list[symbolindex:symbolindex] = ["x", "z", "y", "a", "a", "z", "b", "b"]  
        elif symbol == "9":
            processing_list[symbolindex:symbolindex] = ["x", "c", "c", "y", "d", "d", "z", "e", "e"]   
        elif symbol == "0":
            processing_list[symbolindex:symbolindex] = ["x", "f", "f", "y", "h", "h", "z", "i", "i"] 
        elif symbol == ".":
            processing_list[symbolindex:symbolindex] = ["x", "j", "j",  "y", "k", "k", "z", "l", "l"]
        elif symbol == " ":
            processing_list[symbolindex:symbolindex] = ["x", "a", "y", "b", "z", "c"]    
        elif symbol == "?":
            processing_list[symbolindex:symbolindex] = ["x", "m", "m", "y", "n", "n", "z", "o", "o"]
        elif symbol == "!":
            processing_list[symbolindex:symbolindex] = ["x", "p", "p", "y", "q", "q", "z", "r", "r"]
        elif symbol == ":":
            processing_list[symbolindex:symbolindex] = ["x", "s", "s", "y", "t", "t", "z", "u", "u"] 
        elif symbol == ",":
            processing_list[symbolindex:symbolindex] = ["x", "v", "v", "y", "w", "w", "z", "x", "x"] 

    # searches for special characters and numbers

    def replacer_of_special_characters(arr, symbol):
        symbolindex = []
        
        for i in range(len(processing_list)):
            if arr[i] == symbol:
                symbolindex.append(int(i))
        ListLen = len(symbolindex)
        while ListLen > 0:
            ListLen = ListLen-1
            arr.pop(symbolindex[ListLen])
            replace_symbols(symbol, symbolindex[ListLen])
            
    # process of encoding
    def encoding_process():
        global turn_count_EW1
        global turn_count_EW2
        global turn_count_EW3
        return_val_a = enigma_wh_1.index(processing_list[i])
        return_val_b = enigma_wh_2.index(return_val_a)
        return_val_c = enigma_wh_3.index(return_val_b)
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

    input_string = input_string.lower()
    processing_list = []
    
    Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # Erstellung einer Liste
    processing_list[:0] = input_string
    
    # replacement of special characters/number 
    for i in range(16):
        replacer_of_special_characters(processing_list, symbols[i])

    # replacing letters with numbers    

    def replace_letters_numbers_in_list(list, replace_element, new_element):
        return [new_element if item == replace_element else item for item in list]

    for i in range(26):
        processing_list = replace_letters_numbers_in_list(processing_list, Alphabet[i], i+1)

    # enigma wheels

    enigma_wh_1 = ["_", 6, 11, 4, 10, 8, 12, 2, 9, 5, 23, 1, 13, 7, 24, 21, 18, 19, 16, 26, 20, 14, 25, 15, 17, 22, 3]
    enigma_wh_2 = ["_", 17, 5, 9, 26, 16, 8, 22, 13, 14, 1, 19, 2, 10, 18, 3, 25, 4, 12, 24, 21, 6, 20, 7, 23, 15, 11]
    enigma_wh_3 = ["_", 26, 15, 9, 5, 3, 12, 23, 17, 19, 14, 7, 10, 1, 24, 11, 25, 4, 20, 22, 6, 18, 13, 2, 21, 16, 8]

    # Enigma encoding (siehe encoding_process())    
    for i in range(len(processing_list)):
        encoding_process()

    # replacing numbers with letters   
    
    for i in range(26):
        processing_list = replace_letters_numbers_in_list(processing_list, i+1, Alphabet[i])
    output_string = "".join(processing_list)
        
    # output
    return output_string
    


