# # Książka adresowa:
#
# # Program przechowujący danę kontaktowe znajomych/klientów.
# # Program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie. Zadania to:
# # Wyświetlenie wszystkich wpisów
# # Stworzenie nowego wpisu (dane wczytywane z klawiatury)
# # Usunięcie wpisu
# # Zakończenie pracy programu
# # Program powinien na starcie mieć już wprowadzone kilka wpisów.
import sys

def show_addressbook():
    for k, v in address_book.items():
        for a, b in v.items():
            print(a , ":",  b)


def is_correct(number):
    if (len(number) == 9) and number.isdigit():
        return True
    else:
        return False


def add_person():
    people_num = int(input("Ile osob chcesz dodać do książki adresowej?"))
    for i in range(people_num):
        print("------------------------------------------")
        name = input("Podaj imię: ")
        surname = input("Podaj nazwisko: ")
        number = input("Podaj numet telefonu: ")
        name = name.title()
        surname = surname.title()
        address_book[name + " " + surname] = {}
        address_book[name + " " + surname]["imię"] = name
        address_book[name + " " + surname]["nazwisko"] = surname
        set_number = False
        while set_number != True:
            if is_correct(number):
                address_book[name + " " + surname]["numer"] = number
                set_number = True
            else:
                print("Podaj nowy numer")
                number = input("Podaj numer telefonu: ")
    show_addressbook()

def remove_person():
    name = input("Podaj imię: ")
    surname = input("Podaj nazwisko: ")
    name = name.title()
    surname = surname.title()
    del address_book[name + " " + surname]



def search_person():
    name = input("Podaj imię: ")
    name = name.title()
    found = False
    for key_name in address_book.keys():
        if name in key_name:
            print(address_book[key_name])
            found = True

    if found == False:
        print("nie znaleziono")


def users_choice():
    if a == 1:
        show_addressbook()
    elif a == 2:
        add_person()
    elif a == 3:
        remove_person()
    elif a == 4:
        search_person()
    elif a == 5:
        sys.exit(0)


address_book = {
    "Jan Kowalski": {"imię": "Jan", "nazwisko": "Kowalski", "numer": 756259321},
    "Anna Nowak" : {"imię" : "Anna", "nazwisko" : "Nowak", "numer": 789456123}
}


running_program = True
while running_program != False:
    print("***Menu***")
    print("1 - wyświetl książkę adresową. \n2 - dodaj nowy kontakt \n3 - usuń kontakt \n4 - wyszukaj kontakt \n5 - wyjdź")
    a = int(input("Co chcesz zrobić:"))
    users_choice()


