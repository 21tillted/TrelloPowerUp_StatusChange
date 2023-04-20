from ProDemote import ProDemote
from CardOperations import *
import config

ProDeInstance = ProDemote()
operations = CardOperations()

steamID = "STEAM_0:0:507845320"


#ProDeInstance.remove_label_from_card('5rCdYDfG', 'SM')
card = ProDeInstance.getCardFromSteamID('STEAM_0:0:507845320')
operations.sortin_card(card=card, destinationRank='SSGT')
#ProDeInstance.add_label_to_card('5rCdYDfG', 'SM')
#Eingabe von SteamID
print("bitte die SteamID")
userSteamID = input()       
#Ausgabe von Name& Rang
print(ProDeInstance.getNameAndRankFromSteamID(userSteamID)) 
#Welchen Rang soll er gesetzt werden?
selectedRank = input()
#Wer ändert den Rang?
changeingUser = input()
ProDeInstance.changeRankOfCard(selectedRank)   

#makeLoggingMessage
