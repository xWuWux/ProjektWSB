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

choice = menu()

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

elif choice == 5:
    plik = open('file.txt')
    try:
        tekst = plik.read()
    finally:
        plik.close()


        data = tekst.split(".")
        num_of_char = len(data)
        print('Count in text file :', num_of_char)


