import ProDemote

ProDeInstance = ProDemote

steamID = "STEAM_0:0:121430886"

#Eingabe von SteamID
print("bitte die SteamID")
usersteamID = input()       
#Ausgabe von Name& Rang
print(ProDeInstance.getNameAndRankFromSteamID(usersteamID)) 
#Welchen Rang soll er gesetzt werden?
selectedRank = input()
#Wer ändert den Rang?
changeingUser = input()
ProDeInstance.changeRankOfCard(selectedRank)   
