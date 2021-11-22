# encoding of enigma 

import tkinter as tk

# start values for enigma wheel
SchrittzahlE1 = 0 
SchrittzahlE2 = 0 
SchrittzahlE3 = 0



def process():
    #vales for encoding of symbols and special characters 
    # ' ' = xaybzc ; '1' =  xdyezf; '2' =  xhyizj; '3' =  xkylzm; '4' =  xnyozp; '5' =  xqyrzs;
    #  '6' =  xtyuzv; '7' =  xwyxzy; '8' =  xzyaazbb; '9' =  xccyddzee; '0' =  xffyhhzii; '.' = xjjykkzll; '?' = xmmynnzoo; '!' = xppyqqzrr; ':' = xssyttzuu
    # ',' = xvvywwzxx; 

    symbol1 = "1"
    symbol2 = "2"
    symbol3 = "3"
    symbol4 = "4"
    symbol5 = "5"
    symbol6 = "6"
    symbol7 = "7"
    symbol8 = "8"
    symbol9 = "9"
    symbol10 = "0"
    symbol11 = " "
    symbol12 = "."
    symbol13 = "?"
    symbol14 = "!"
    symbol15 = ":"
    symbol16 = ","

    # get user input
    tk.Label(mask, text="Encoded text:").grid(row=10)
    output = tk.Entry(mask, width = 80)
    output.grid(row=10, column=1)
    E = (entry.get())

    # encoding of special characters

    def INSERT(symbol, symbolindex):
        if symbol == "1":
            I.insert(symbolindex, 'f')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'e')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, "d")
            I.insert(symbolindex, 'x')
        elif symbol == "2":
            I.insert(symbolindex, 'j')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'i')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'h')
            I.insert(symbolindex, 'x')   
        elif symbol == "3":
            I.insert(symbolindex, 'm')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'l')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'k')
            I.insert(symbolindex, 'x')   
        elif symbol == "4":
            I.insert(symbolindex, 'p')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'o')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'n')
            I.insert(symbolindex, 'x')   
        elif symbol == "5":
            I.insert(symbolindex, 's')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'r')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'q')
            I.insert(symbolindex, 'x')
        elif symbol == "6":
            I.insert(symbolindex, 'v')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'u')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 't')
            I.insert(symbolindex, 'x')     
        elif symbol == "7":
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'x')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'w')
            I.insert(symbolindex, 'x')    
        elif symbol == "8":
            I.insert(symbolindex, 'b')
            I.insert(symbolindex, 'b')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'a')
            I.insert(symbolindex, 'a')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'x')   
        elif symbol == "9":
            I.insert(symbolindex, 'e')
            I.insert(symbolindex, 'e')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'd')
            I.insert(symbolindex, 'd')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'c')
            I.insert(symbolindex, 'c')
            I.insert(symbolindex, 'x')    
        elif symbol == "0":
            I.insert(symbolindex, 'i')
            I.insert(symbolindex, 'i')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'h')
            I.insert(symbolindex, 'h')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'f')
            I.insert(symbolindex, 'f')
            I.insert(symbolindex, 'x') 
        elif symbol == ".":
            I.insert(symbolindex, 'l')
            I.insert(symbolindex, 'l')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'k')
            I.insert(symbolindex, 'k')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'j')
            I.insert(symbolindex, 'j')
            I.insert(symbolindex, 'x') 
        elif symbol == " ":
            I.insert(symbolindex, 'c')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'b')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'a')
            I.insert(symbolindex, 'x')     
        elif symbol == "?":
            I.insert(symbolindex, 'o')
            I.insert(symbolindex, 'o')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'n')
            I.insert(symbolindex, 'n')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'm')
            I.insert(symbolindex, 'm')
            I.insert(symbolindex, 'x')
        elif symbol == "!":
            I.insert(symbolindex, 'r')
            I.insert(symbolindex, 'r')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'q')
            I.insert(symbolindex, 'q')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'p')
            I.insert(symbolindex, 'p')
            I.insert(symbolindex, 'x')  
        elif symbol == ":":
            I.insert(symbolindex, 'u')
            I.insert(symbolindex, 'u')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 't')
            I.insert(symbolindex, 't')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 's')
            I.insert(symbolindex, 's')
            I.insert(symbolindex, 'x')  
        elif symbol == ",":
            I.insert(symbolindex, 'x')
            I.insert(symbolindex, 'x')
            I.insert(symbolindex, 'z')
            I.insert(symbolindex, 'w')
            I.insert(symbolindex, 'w')
            I.insert(symbolindex, 'y')
            I.insert(symbolindex, 'v')
            I.insert(symbolindex, 'v')
            I.insert(symbolindex, 'x')  

    # searches for special characters and numbers

    def linearsearch(arr, symbol):
        symbolindex = []
        
        for i in range(len(I)):
            if arr[i] == symbol:
                symbolindex.append(int(i))
        ListLen = len(symbolindex)
        while ListLen > 0:
            ListLen = ListLen-1
            arr.pop(symbolindex[ListLen])
            if symbol == "1":
                INSERT("1", symbolindex[ListLen])  
            elif symbol == "2":
                INSERT("2", symbolindex[ListLen])
            elif symbol == "3":
                INSERT("3", symbolindex[ListLen])
            elif symbol == "4":
                INSERT("4", symbolindex[ListLen])
            elif symbol == "5":
                INSERT("5", symbolindex[ListLen])
            elif symbol == "6":
                INSERT("6", symbolindex[ListLen])
            elif symbol == "7":
                INSERT("7", symbolindex[ListLen])
            elif symbol == "8":
                INSERT("8", symbolindex[ListLen])
            elif symbol == "9":
                INSERT("9", symbolindex[ListLen])
            elif symbol == "0":
                INSERT("0", symbolindex[ListLen])
            elif symbol == ".":
                INSERT(".", symbolindex[ListLen])
            elif symbol == " ":
                INSERT(" ", symbolindex[ListLen])
            elif symbol == "?":
                INSERT("?", symbolindex[ListLen])
            elif symbol == "!":
                INSERT("!", symbolindex[ListLen])
            elif symbol == ":":
                INSERT(":", symbolindex[ListLen])
            elif symbol == ",":
                INSERT(",", symbolindex[ListLen])    



    def Kodierung():
        global SchrittzahlE1
        global SchrittzahlE2
        global SchrittzahlE3
        AusgabeBA = Enigma1.index(I[i])
        AusgabeBB = Enigma2.index(AusgabeBA)
        AusgabeBC = Enigma3.index(AusgabeBB)
        I[i] = AusgabeBC
        Drehung1 = Enigma1.pop()
        Enigma1.insert(1,Drehung1)
        SchrittzahlE1 = SchrittzahlE1 + 1
        if SchrittzahlE1 == 26:
            SchrittzahlE1 = 0
            Drehung2 = Enigma2.pop()
            Enigma2.insert(1,Drehung2)
            SchrittzahlE2 = SchrittzahlE2 + 1
        if SchrittzahlE2 == 26:
            SchrittzahlE2 = 0
            Drehung3 = Enigma3.pop()
            Enigma3.insert(1,Drehung3)
            SchrittzahlE3 = SchrittzahlE3 + 1  
        if SchrittzahlE3 == 26:
            print("Eingabe zu Lang") 

    N = len(E)
    E = E.lower()
    I = []
    AN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Erstellung einer Liste
    while N > 0:
        G = E[N-1]
        I.insert(0,G)
        N = N-1

    # REplacing of every number & special character
    linearsearch(I, symbol1)
    linearsearch(I, symbol2)
    linearsearch(I, symbol3)
    linearsearch(I, symbol4)
    linearsearch(I, symbol5)
    linearsearch(I, symbol6)
    linearsearch(I, symbol7)
    linearsearch(I, symbol8)
    linearsearch(I, symbol9)
    linearsearch(I, symbol10)
    linearsearch(I, symbol11)
    linearsearch(I, symbol12)
    linearsearch(I, symbol13)
    linearsearch(I, symbol14)
    linearsearch(I, symbol15)
    linearsearch(I, symbol16)

    # Einsetzen der Zahlen    
    for i in range(len(I)):
        if I[i] == Alphabet[0]:
            I[i] = 1
        elif I[i] == Alphabet[1]:
            I[i] = 2
        elif I[i] == Alphabet[2]:
            I[i] = 3
        elif I[i] == Alphabet[3]:
            I[i] = 4
        elif I[i] == Alphabet[4]:
            I[i] = 5
        elif I[i] == Alphabet[5]:
            I[i] = 6
        elif I[i] == Alphabet[6]:
            I[i] = 7
        elif I[i] == Alphabet[7]:
            I[i] = 8
        elif I[i] == Alphabet[8]:
            I[i] = 9
        elif I[i] == Alphabet[9]:
            I[i] = 10
        elif I[i] == Alphabet[10]:
            I[i] = 11
        elif I[i] == Alphabet[11]:
            I[i] = 12
        elif I[i] == Alphabet[12]:
            I[i] = 13
        elif I[i] == Alphabet[13]:
            I[i] = 14
        elif I[i] == Alphabet[14]:
            I[i] = 15
        elif I[i] == Alphabet[15]:
            I[i] = 16
        elif I[i] == Alphabet[16]:
            I[i] = 17
        elif I[i] == Alphabet[17]:
            I[i] = 18
        elif I[i] == Alphabet[18]:
            I[i] = 19
        elif I[i] == Alphabet[19]:
            I[i] = 20
        elif I[i] == Alphabet[20]:
            I[i] = 21
        elif I[i] == Alphabet[21]:
            I[i] = 22
        elif I[i] == Alphabet[22]:
            I[i] = 23
        elif I[i] == Alphabet[23]:
            I[i] = 24
        elif I[i] == Alphabet[24]:
            I[i] = 25
        elif I[i] == Alphabet[25]:
            I[i] = 26

    # Enigma - Räder
    Enigma1 = ['_', 6, 11, 4, 10, 8, 12, 2, 9, 5, 23, 1, 13, 7, 24, 21, 18, 19, 16, 26, 20, 14, 25, 15, 17, 22, 3]
    Enigma2 = ['_', 17, 5, 9, 26, 16, 8, 22, 13, 14, 1, 19, 2, 10, 18, 3, 25, 4, 12, 24, 21, 6, 20, 7, 23, 15, 11]
    Enigma3 = ['_', 26, 15, 9, 5, 3, 12, 23, 17, 19, 14, 7, 10, 1, 24, 11, 25, 4, 20, 22, 6, 18, 13, 2, 21, 16, 8]

    # Enigma Kodierung (siehe Kodierung())    
    for i in range(len(I)):
        if I[i] == AN[0]:
            Kodierung()
        elif I[i] == AN[1]:
            Kodierung()
        elif I[i] == AN[2]:
            Kodierung()
        elif I[i] == AN[3]:
            Kodierung()
        elif I[i] == AN[4]:
            Kodierung()
        elif I[i] == AN[5]:
            Kodierung()
        elif I[i] == AN[6]:
            Kodierung()
        elif I[i] == AN[7]:
            Kodierung()
        elif I[i] == AN[8]:
            Kodierung()
        elif I[i] == AN[9]:
            Kodierung()
        elif I[i] == AN[10]:
            Kodierung()
        elif I[i] == AN[11]:
            Kodierung()
        elif I[i] == AN[12]:
            Kodierung()
        elif I[i] == AN[13]:
            Kodierung()
        elif I[i] == AN[14]:
            Kodierung()
        elif I[i] == AN[15]:
            Kodierung()
        elif I[i] == AN[16]:
            Kodierung()
        elif I[i] == AN[17]:
            Kodierung()
        elif I[i] == AN[18]:
            Kodierung()
        elif I[i] == AN[19]:
            Kodierung()
        elif I[i] == AN[20]:
            Kodierung()
        elif I[i] == AN[21]:
            Kodierung()
        elif I[i] == AN[22]:
            Kodierung()
        elif I[i] == AN[23]:
            Kodierung()
        elif I[i] == AN[24]:
            Kodierung()
        elif I[i] == AN[25]:
            Kodierung()

    # converting numbers into letters   
    
    for i in range(len(I)):
        if I[i] == AN[0]:
            I[i] = "a"
        elif I[i] == AN[1]:
            I[i] = "b"
        elif I[i] == AN[2]:
            I[i] = "c"
        elif I[i] == AN[3]:
            I[i] = "d"
        elif I[i] == AN[4]:
            I[i] = "e"
        elif I[i] == AN[5]:
            I[i] = "f"
        elif I[i] == AN[6]:
            I[i] = "g"
        elif I[i] == AN[7]:
            I[i] = "h"
        elif I[i] == AN[8]:
            I[i] = "i"
        elif I[i] == AN[9]:
            I[i] = "j"
        elif I[i] == AN[10]:
            I[i] = "k"
        elif I[i] == AN[11]:
            I[i] = "l"
        elif I[i] == AN[12]:
            I[i] = "m"
        elif I[i] == AN[13]:
            I[i] = "n"
        elif I[i] == AN[14]:
            I[i] = "o"
        elif I[i] == AN[15]:
            I[i] = "p"
        elif I[i] == AN[16]:
            I[i] = "q"
        elif I[i] == AN[17]:
            I[i] = "r"
        elif I[i] == AN[18]:
            I[i] = "s"
        elif I[i] == AN[19]:
            I[i] = "t"
        elif I[i] == AN[20]:
            I[i] = "u"
        elif I[i] == AN[21]:
            I[i] = "v"
        elif I[i] == AN[22]:
            I[i] = "w"
        elif I[i] == AN[23]:
            I[i] = "x"
        elif I[i] == AN[24]:
            I[i] = "y"
        elif I[i] == AN[25]:
            I[i] = "z"
    M = "".join(I)
        
    # output

    output.insert(0, M)

# graphical interface
mask = tk.Tk()
mask.geometry("650x250")
mask.title("Encoding of Engima")
tk.Label(mask, text="Enter text:").grid(row=0)
entry = tk.Entry(mask, width = 80)
entry.grid(row=0, column=1)


tk.Button(mask, text="End", command=mask.quit).grid(row=250, column=0, sticky=tk.W, pady=20)
tk.Button(mask, text="Encode", command=process).grid(row=8, column=0, sticky=tk.W, pady=20)

mask.mainloop()