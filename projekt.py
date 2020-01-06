import requests
import pathlib
import os
import string
import sys

def menu():
    print("1. Pobierz plik z internetu ")
    print("2. Zlicz liczbe liter w pobranym pliku ")
    print("3. Zlicz liczbe wyrazow w pliku ")
    print("4. Zlicz liczbe znakow interpunkcyjnych w pliku ")
    print("5. Zlicz liczbe zdan w pliku")
    print("6. Wygeneruj raport o uzyciu liter (A-Z) ")
    print("7. Zapisz statystyki z punktow 2-5 do pliku statystyki.txt ")
    print("8. Wyjscie z programu ")
    choice = int(input("Enter choice: "))
    return choice

plik = 'file.txt'
global letters, words, DottChars, sentences

while True:
    menu()
    while True:
        choice = int(input("Enter choice: "))
        try:
            if choice >=1 and choice <=8:
                break
        except ValueError:
            choice = -1

        print("Please select good value \n")

    if choice == 1:
        url = "http://s3.zylowski.net/public/input/5.txt"
        r = requests.get(url)
        with open('file.txt', 'w', encoding='utf8') as getFile:
            getFile.write(r.text)
        fileStats = pathlib.Path("file.txt")
        if fileStats.exists():
            print(" Download file. ")

    elif choice == 2:
        def count_letters():
            global letters
            letters = 0
            try:
                with open(filename, 'r') as myfile:
                    data = myfile.read()

                for x in data:
                    if x.isalpha():
                        letters += 1

                print(" Ilość liter w pliku ", filename, " to ", str(letters))
            except FileNotFoundError:
                print(" ** Brak pliku ", filename, " **")
            except Exception:
                print(" ** Nie mogę otworzyć pliku ", filename)

    elif choice == 3:
        try:
            with open(plik, 'r') as file:
                tekst = file.read()

            delWhiteSpace = tekst.strip()
            words = 0
            words = len(delWhiteSpace.split())
            print('Count words of text file:', words)

        except FileNotFoundError:
            print(" File not found ", plik)
        except Exception:
            print(" Could not open file ", plik)

    elif choice == 4:
        try:
            with open(plik, 'r') as file:
                tekst = file.read()

            DottChars = 0
            DottChars = tekst.count(".") + tekst.count("!") + tekst.count("?") + tekst.count(",") + tekst.count("'") + tekst.count(";") + tekst.count("-")
            print("Count special chars of text file: ", str(DottChars))

        except FileNotFoundError:
            print(" File not found ", plik)
        except Exception:
            print(" Could not open file ", plik)


    elif choice == 5:

        try:

            with open(plik, 'r') as file:

                tekst = file.read()

            sentences = 0
            sentences = tekst.count(".") + tekst.count("!") + tekst.count("?")
            print('Count sentences of text file:', sentences)

        except FileNotFoundError:

            print(" File not found ", plik)

        except Exception:

            print(" Could not open file ", plik)
    elif choice == 8:
        sys.exit()

