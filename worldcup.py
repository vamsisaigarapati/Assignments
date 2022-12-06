import csv
list_of_recs = []
with open('BrazilWCstats.csv', 'r', encoding="latin1") as f:
    dr = csv.DictReader(f)
    for rec in dr:
        temp_dict={}
        for key,value in rec.items():
            temp_dict[key.encode('ascii', 'ignore').decode('ascii')]= value.encode('ascii', 'ignore').decode('ascii')
        list_of_recs.append(temp_dict)
player_years={}
for rec in list_of_recs:
    for goals in rec['Goals by World Cup'].split(','):
        temp=goals.strip().split(' ')
        if int(temp[0])!=0:
            if int(temp[2]) in player_years:
                player_years[int(temp[2])].update({rec['Player']:int(temp[0])})
            else:
                player_years[int(temp[2])]={}
                player_years[int(temp[2])].update({rec['Player']: int(temp[0])})
list_of_years=list(player_years.keys())
list_of_years.sort()
for year in list_of_years:
    tmp = ', '.join(f"{i[0]} ({i[1]})" for i in sorted(player_years[year].items(), key=lambda x: (-x[1], x[0])))
    print(f"{year}: {tmp}")
