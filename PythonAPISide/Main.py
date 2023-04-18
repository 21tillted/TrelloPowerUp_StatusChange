from ProDemote import ProDemote
import config

ProDeInstance = ProDemote()

steamID = "STEAM_0:0:507845320"

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
