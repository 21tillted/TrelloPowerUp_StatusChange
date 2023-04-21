from ProDemote import ProDemote
from CardOperations import *
from datetime import date

ProDeInstance = ProDemote()
operations = CardOperations()

steamID = "STEAM_0:0:121430886"

Promote ={
    0: 'Isarc',
    1: 'Wangoch',
    2: 'SM',
    3: 'SGT',
    4: 'ist zu faul',
    5: f'{date.today().day}.{date.today().month}.{date.today().year}',
    6: steamID,
}


#ProDeInstance.remove_label_from_card('5rCdYDfG', 'SM')
#card = ProDeInstance.getCardFromSteamID('STEAM_0:0:507845320')
#operations.sortin_card(card=card, destinationRank='SGT')
#ProDeInstance.add_label_to_card('5rCdYDfG', 'SM')
#Eingabe von SteamID
print("bitte die SteamID")
userSteamID = input()       
#Ausgabe von Name& Rang
print(ProDeInstance.getNameAndRankFromSteamID(steamID=userSteamID.strip()))
print('Welchen Rang soll er gesetzt werden?')
selectedRank = input()
Promote[3] = selectedRank
print('Wer ändert den Rang?')
changeingUser = input()
Promote[1] = changeingUser
#makeLoggingMessage
Message = ProDeInstance.proDemoteUser(steamID=steamID.strip(),comment=Promote)
print(Message)
