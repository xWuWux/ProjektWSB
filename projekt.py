import requests

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

    if choice==1:
        url = "http://s3.zylowski.net/public/input/5.txt"
        r = requests.get(url)
        with open('file.txt', 'w') as file:
            file.write(r.text.encode('UTF-8'))

    elif choice == 3:
        plik = open('file.txt')
        try:
            tekst = plik.read()
        finally:
            plik.close()

        data = tekst.split(" ")
        num_of_words = len(data)
        print('Count in text file :', num_of_words)
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
    elif choice == 4:
        plik = open('file.txt')
        try:
            tekst = plik.read()
        finally:
            plik.close()

        dataD = tekst.split(".")
        dataC = tekst.split(",")
        dataS = tekst.split(";")
        dataCo = tekst.split(":")
        dataQ = tekst.split("?")
        dataE = tekst.split("!")
        dataDa = tekst.split("-")

        num_of_d = len(dataD)
        num_of_c = len(dataC)
        num_of_s = len(dataS)
        num_of_co = len(dataCo)
        num_of_q = len(dataQ)
        num_of_e = len(dataE)
        num_of_Da = len(dataDa)


        print('. : ',num_of_d)
        print(', : ',num_of_c)
        print('; : ',num_of_s)
        print(': : ',num_of_co)
        print('? : ',num_of_q)
        print('! : ',num_of_e)
        print('- : ',num_of_Da)

        except FileNotFoundError:
            print(" ** Brak pliku ", filename, " **")
        except Exception:
            print(" ** Nie mogę otworzyć pliku ", filename)

        menu()
    elif choice == 5:
        plik = open('file.txt')
        try:
            tekst = plik.read()
        finally:
            plik.close()


            data = tekst.split(".")
            num_of_d = len(data)
            print('Count in text file :', num_of_d)


