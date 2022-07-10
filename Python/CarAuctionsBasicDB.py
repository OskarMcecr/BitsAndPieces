import json
from pathlib import Path

#Element sprawdzajacy wartosci float oraz int
class ValueErrorCheck():
    
    empty_ = 0
    
    def __init__(self, value=None):
        self.value=value
 
    def get_empty(self):
        return self.empty_
    
    #wywolany przy przywolaniu int(ValueErrorCheck) sprawdza input. Jezeli jest bledny, wyrzuca wartosc 0
    def __int__(self):
        try:
            self.value = int(self.value)
        except ValueError:
            print("Wrong input, correcting to 0")
            self.value = int(0)
        return self.value

    #podobnie do int tylko dla float i wyrzuca 0.0
    def __float__(self):
        try:
            self.value = float(self.value)
        except ValueError:
            print("Wrong input, correcting to 0.0")
            self.value = float(0.0)
        return self.value

#rozpis opcji w glownym menu
MMoptions = {
    0: 'EXIT',
    1: 'Start an auciton',
    2: 'Add a car',
    3: 'Show database',
    4: 'Create new empty database',
}

#rozpis opcji w menu aukcji
AMoptions = {
    0: 'BACK',
    1: 'Bid',
    2: 'Sell',
    3: 'Reset price & status'
}

#rysuje w terminalu glowne menu
def StartMenu():
    print("\n")
    for key in MMoptions.keys():
        print (key, '--', MMoptions[key] )
    print("\n")

#rysuje w terminalu menu aukcji
def AuctionMenu():
    print("\n")
    for key in AMoptions.keys():
        print (key, '--', AMoptions[key] )
    print("\n")

#rysuje w terminalu liste dostepnych samochodow z bazy
def CarMenu(list):
    print("0","--","BACK")
    for key in range(len(list)):
        print(key+1,"--",list[key])
    print("\n")

#opcja 1 w glownym menu uruchamia menu aukcyjne
def MMoption1():

    #przypisanie wartosci z bazy
    print('\nChoose a car')
    nameBase = CarDataBase["name"]
    valueBase = CarDataBase["value"]
    priceBase = CarDataBase["price"]
    statusBase = CarDataBase["status"]
    CarMenu(nameBase)

    #prosi uzytkownika o wybor ktory jest sprawdzany.
    optionO = ''
    optionO = input('Enter your choice: ')
    optionO = int(ValueErrorCheck(optionO))
    
    #sprawdza czy zostal wybrany samochod z listy
    if optionO in range(1,len(nameBase)+1,1):
        lp = 1
        iO = optionO-1

        #petla pozwalajaca na wybor kilku elementow bez potrzeby powrotu do glownego menu
        while lp == 1:
            print("\nName - Starting price - Current price - Status")
            print(nameBase[iO]," - ",valueBase[iO]," - ",priceBase[iO]," - ",statusBase[iO])
            AuctionMenu()  
            
            optionOO = ''
            optionOO = input('Enter your choice: ')
            optionOO = int(ValueErrorCheck(optionOO))

            #warunek sprawdzajacy status samochodu
            if statusBase[iO] == "Sold":
                print("Car already sold")
            else:

                #opcja 1 w menu aukcji powieksza aktualna cene samochodu    
                if optionOO == 1:
                    print("\nCurrent price: ",priceBase[iO])
                    bid = input('Enter bid amount: ')
                    bid=float(ValueErrorCheck(bid))
                    priceBase[iO] = priceBase[iO] + bid
                    CarDataBase["price"] = priceBase
                    print("\n")
                
                #opcja 2 w menu aukcji zmienia status na sprzedany
                elif optionOO == 2:
                    print(nameBase[iO],"sold")
                    statusBase[iO] = "Sold"
                    CarDataBase["status"] = statusBase
                    lp = 0
                    print("\n")
                else:
                    print('Option not found')

            #resetuje cene aktualna oraz status samochodu
            if optionOO == 3:
                priceBase[iO] = valueBase[iO]
                statusBase[iO] = "New"
                CarDataBase["price"] = priceBase
                CarDataBase["status"] = statusBase
                print("\n")

            #wyjscie z petli    
            elif optionOO == 0:
                lp = 0
                print("\n")
            else:
                print('\n')

    #powrot do glownego menu
    elif optionO == 0:
        print("\n")
    else:
        print('Car not found')
        print("\n")

#opcja 2 pozwala na dodanie samochodu do bazy
def MMoption2():
    nameBase = CarDataBase["name"]
    valueBase = CarDataBase["value"]
    priceBase = CarDataBase["price"]
    statusBase = CarDataBase["status"]

    #prosba o dane samochodu od uzytkownika ktora jednoczesnie sprawdza poprawnosc danych
    name = input("Name: ")
    nameBase.append(name)
    value = input("Value: ")
    value = float(ValueErrorCheck(value))
    valueBase.append(value)
    priceBase.append(value)
    statusBase.append("New")

    CarDataBase["name"] = nameBase
    CarDataBase["value"] = valueBase
    CarDataBase["price"] = priceBase
    CarDataBase["status"] = statusBase

    #zapis nowego samochodu w bazie
    file = open('AuctionDB', 'w') 
    json.dump(CarDataBase, file)                      
    file.close()

#opcja 3 w glownym menu drukuje aktualna baze
def MMoption3():
    nameBase = CarDataBase["name"]
    valueBase = CarDataBase["value"]
    priceBase = CarDataBase["price"]
    statusBase = CarDataBase["status"]
    print("\nName - Starting price - Current price - Status")
    for i in range(len(nameBase)):
        print(nameBase[i]," - ",valueBase[i]," - ",priceBase[i]," - ",statusBase[i])

#opcja 4 w glownym menu tworzy nowa, pusta baze danych
def MMoption4():
    CardDataBase={}
    nameBase = []
    valueBase = []
    priceBase = []
    statusBase = []
    CarDataBase["name"] = nameBase
    CarDataBase["value"] = valueBase
    CarDataBase["price"] = priceBase
    CarDataBase["status"] = statusBase

    file = open('AuctionDB', 'w') 
    json.dump(CarDataBase, file)                      
    file.close()

    print("New data base created")

#opcja 0 w glownym menu zapisuje baze oraz zamyka program
def MMclose():
    file = open('AuctionDB', 'w') 
    json.dump(CarDataBase, file)                      
    file.close()
    exit()

#glowny program
if __name__=='__main__':

    #warunek sprawdzajacy istnienie bazy
    if Path("AuctionDB").exists():

        #jezeli plik istnieje, baza zostaje tylko wczytana
        file = open('AuctionDB', 'r')
        CarDataBase = json.load(file)
        file.close()
    else:

        #jezeli plik nie istnieje, baza zostaje stworzona z przykladowymi wartosciami
        file = open('AuctionDB', 'w')
        CarDataBase = {}
        CarDataBase["name"] = ["Test"]
        CarDataBase["value"] = [float(0.0)]
        CarDataBase["price"] = [float(0.0)]
        CarDataBase["status"] =["New"]
        json.dump(CarDataBase,file)
        file.close()

    #petla glownego menu
    while(True):
        StartMenu()
        option = ''
        option = input('Enter your choice: ')
        option = int(ValueErrorCheck(option))
        if option == 0:
            MMclose()
        elif option == 1:
           MMoption1()
        elif option == 2:
            MMoption2()
        elif option == 3:
            MMoption3()
        elif option == 4:
            MMoption4()
        else:
            print('Option not found')


#LISTA

#Aukcje samochodowe
#Dodanie samochodu oraz jego ceny startowej
#Wybor samochodu z aukcji
#Podbicie kwoty
#Zakonczenie aukcji przez dopisanie ceny sprzedanej
#Zapis do bazy danych zakonczenia aukcji
#blokada/pytanie przy aukcji sprzedanego juz samochodu