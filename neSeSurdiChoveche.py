import random

lengh_feild=50
count_players=4
pozitions_players=[0,0,0,0]
players=['i','I','T','V']
while True:
    next=int(input("Next pozition.Press 0."))
    for nom_players in range(count_players):
        dice=random.randint(1,6)
        if pozitions_players[nom_players]+dice<=lengh_feild:
            pozitions_players[nom_players]=pozitions_players[nom_players]+dice
        for index_players in range(count_players):
            if index_players!=nom_players and pozitions_players[nom_players]==pozitions_players[index_players]:
                pozitions_players[index_players]=0
                print("players N "+str(nom_players+1)+"pushed"+str(index_players+1))
		print("players N"+str(nom_players+1)+"is on pozition"+str(pozitions_players))


    for tekushta_pozition in range(1,lengh_feild+1):
        simvol_for_outage='-'
        for index_players in range(count_players):
            if tekushta_pozition == pozitions_players[index_players]:
                simvol_for_outage=players[index_players]
        print(simvol_for_outage)
    count=0
    for index_players in range(count_players):
        if pozitions_players[index_players]>=lengh_feild:
                print("Player N "+str(index_players+1)+"has left the field! ")
                pozitions_players[index_players]=-1
                count=count+1
    if count==count_players:
        break