import random, shelve, tkinter

def CharacterCreation():
    Name = input("Imie: ")
    print("Statystyki (1-5):")
    HealthBaseValue = int(input("Zycie: "))
    ENBaseValue = int(input("Energia: "))
    WitBaseValue = int(input("WIT: "))
    BaseValue= HealthBaseValue+ENBaseValue+WitBaseValue
    HealthValue = HealthBaseValue/BaseValue
    Health=int(ValueCalc(HealthValue,10,1,2,3,35))
    ENValue = ENBaseValue/BaseValue
    EN=int(ValueCalc(ENValue,2,1,1,1,1))
    WitValue = WitBaseValue/BaseValue
    Wit=int(ValueCalc(WitValue,0,1,2,4,6))
    Res=10
    return Name,Health,EN,Wit,Res

def ValueCalc(Value,Base,Step1,Step2,Step3,Step4):
    
    if Value >= 0:
        Current = Base
    if Value >= 0.1:
        Current = Base+Step1
    if Value >= 0.2:
        Current = Current+Step1
    if Value >= 0.3:
        Current = Current+Step1
    if Value >= 0.4:
        Current = Current+Step2
    if Value >= 0.5:
        Current = Current+Step2
    if Value >= 0.6:
        Current = Current+Step3
    if Value >= 0.7:
        Current = Current+Step4
    return Current

def SavePlayerData(SEED,Name,Health,EN,Wit,Res):
    SEED = str(SEED)
    shelfFile = shelve.open(SEED)
    shelfFile['Name'] = Name
    shelfFile['Health'] = Health
    shelfFile['EN'] = EN
    shelfFile['Wit'] = Wit
    shelfFile['Res'] = Res
    shelfFile.close()
            
def LoadPlayerData(LoadSEED):
    LoadSEED = str(LoadSEED)
    shelfFile = shelve.open(LoadSEED)
    Name = shelfFile['Name']
    Health = shelfFile['Health']
    EN = shelfFile['EN']
    Wit = shelfFile['Wit']
    Res = shelfFile['Res']
    shelfFile.close()
    return Name,Health,EN,Wit,Res

def WitOrder(Name,Wit,Enemy,EnemyWit):
    Name.append(Enemy)
    Wit.append(EnemyWit)
    WOrder=[]
    NOPlayers=len(Name)
    rval = 0
    for rval in NOPlayers:
        WOrder.append((Name[rval],Wit[rval]))
    return WOrder

def AbNaDeck():
    AbNames=["Punch","Dodge","Force blast","Cheap shot","Quick breath","Improvised aid","Misdirection","Kinetic vision","Betrayal","Infect"]
    AbCardAmount = len(AbNames)
    AbDeckAmount = [0]*AbCardAmount
    AbDeckAmount[0] = 4
    AbDeckAmount[1] = 4
    return AbNames

def EnRoDeck():
    RoNames=["Out of time","He, who sees","She, who hears","It, that knows"]
    RoAmount = len(RoNames)
    RoHealth=[20,30,30,30]
    RoWit=[3,2,2,2]
    return RoNames,RoAmount,RoHealth,RoWit

def EnAlDeck():
    AlNames=["Out of time","He, who sees","She, who hears","It, that knows"]
    AlAmount = len(AlNames)
    AlHealth=[20,30,30,30]
    AlWit=[3,2,2,2]
    return AlNames,AlAmount,AlHealth,AlWit

print("Witam w GMFamiliar!")
print("autor Oskar Mlynarczuk")
playerName=[]
playerHealth=[]
playerEN=[]
playerWit=[]
playerRes=[]
REMainSaveLoad = 1
REMainAfter = 1
REGame = 1
while REGame == 1:
    while REMainSaveLoad == 1:
        print("\n1. Nowa gra")
        print("2. Wczytaj gre")
        print("0. Stop")
        OptionMain=input("\nCo chcialbys wykonac: ")

        if OptionMain in ["1"]:
            print("\nWygenerowany SEED: ")
            LoadSEED = random.randrange(1000000,9999999)
            print(LoadSEED)
            NOPlayers=int(input("\nIlosc graczy: "))
            print("\n")
            while NOPlayers >> 0:
                Name,Health,EN,Wit,Res=CharacterCreation()
                playerName.append(Name)
                playerHealth.append(Health)
                playerEN.append(EN)
                playerWit.append(Wit)
                playerRes.append(Res)
                NOPlayers=NOPlayers-1
                print("\n")
            
            SavePlayerData(LoadSEED,playerName,playerHealth,playerEN,playerWit,playerRes)
            REMainSaveLoad = 0


        elif OptionMain in ["2"]:
            LoadSEED=input("Wprowadz SEED: ")
            playerName,playerHealth,playerEN,playerWit,playerRes=LoadPlayerData(LoadSEED)
            REMainSaveLoad = 0
            

        elif OptionMain in ["0"]:
            print("Dziekuje")
            REMainSaveLoad = 0
            REMainAfter = 0
            REGame = 0
            break
        else:
            print("Wybierz z opcji podanych powyzej")

    while REMainAfter == 1:
        print("\nImiona: ",playerName)
        print("Zycie:   ",playerHealth)
        print("EN:      ",playerEN)
        print("Wit:     ",playerWit)
        print("Res:     ",playerRes)

        print("\n1. Edytuj statystyki")
        print("2. Walka")
        print("0. Stop")
        OptionMainAfter=input("\nCo chcialbys wykonac: ")
        if OptionMainAfter in ["1"]:
            print("\n1. Zycie")
            print("2. EN")
            print("3. Wit")
            print("4. Res")
            print("9. Imie")
            print("0. Stop")
            OptionEditStats=input("\nCo chialbys zmienic: ")

            if OptionEditStats in ["0"]:
                print("\n")

            elif OptionEditStats in ["1","2","3","4","9"]:
                print("\n")
                for rval in range(len(playerName)):
                    print(rval+1,". ",playerName[rval])
                OptionPEditStats=int(input("\nKomu chialbys zmienic: "))

                if OptionEditStats in ["1"]:
                    print("\nAktualne Zycie: ",playerHealth[OptionPEditStats-1])
                    playerHealth[OptionPEditStats-1]=int(input("\nPodaj nowa wartosc: "))
                elif OptionEditStats in ["2"]:
                    print("\nAktualne EN: ",playerEN[OptionPEditStats-1])
                    playerEN[OptionPEditStats-1]=int(input("\nPodaj nowa wartosc: "))
                elif OptionEditStats in ["3"]:
                    print("\nAktualne Wit: ",playerWit[OptionPEditStats-1])
                    playerWit[OptionPEditStats-1]=int(input("\nPodaj nowa wartosc: "))
                elif OptionEditStats in ["4"]:
                    print("\nAktualne Res: ",playerRes[OptionPEditStats-1])
                    playerRes[OptionPEditStats-1]=int(input("\nPodaj nowa wartosc: "))
                elif OptionEditStats in ["9"]:
                    print("\nAktualne Imie: ",playerName[OptionPEditStats-1])
                    playerName[OptionPEditStats-1]=input("\nPodaj nowa wartosc: ")

                SavePlayerData(LoadSEED,playerName,playerHealth,playerEN,playerWit,playerRes)

            else:
                print("Wybierz z opcji podanych powyzej")
            
        elif OptionMainAfter in ["2"]:
            EnemyNames,EnemyAmounts,EnemyHealths,EnemyWits=EnRoDeck()
            print("\n")
            for rval in range(len(EnemyNames)):
                print(rval+1,". ",EnemyNames[rval])
            print("0 .  Stop")
            OptionEnemyID=input("\nWprowadz ID: ")

            if OptionEnemyID in ["0"]:
                print("\n")

            else:
                OptionEnemyID=int(OptionEnemyID)-1
                EnemyName=EnemyNames[OptionEnemyID]
                EnemyHealth=EnemyHealths[OptionEnemyID]*len(playerName)
                EnemyWit=EnemyWits[OptionEnemyID]
                print("\nImie: ",EnemyName)
                print("Zycie: ",EnemyHealth)
                print("Wit:   ",EnemyWit)

                EncounterList=WitOrder(playerName,playerWit,EnemyName,EnemyWit)
                WOrder=sorted(EncounterList,key=lambda EncounterList: EncounterList[1], reverse=True)
                
                print("\n")
                for rval2 in range(len(WOrder)):
                    print("Akcja",rval2+1,": ",WOrder[rval2])
                    
                del playerName[-1]
                del playerWit[-1]
                EncounterList.clear()
                WOrder.clear()

        elif OptionMainAfter in ["0"]:
            print("Dziekuje")
            REMainAfter = 0
            REGame = 0
            break
        else:
            print("Wybierz z opcji podanych powyzej")