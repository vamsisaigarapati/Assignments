import csv
gender = {}
all_superheros=0
eye_colour = {}
all_eye_colours=0
with open('hero_info.csv', 'r', encoding="utf-8") as f:
    dr = csv.DictReader(f)
    for rec in dr:
        all_superheros+=1
        if rec['Gender'] in gender:
            gender[rec['Gender']]+=1
        else:
            gender[rec['Gender']] =1
        if rec['Race']=='Human':
            all_eye_colours+=1
            if rec['Eyes'] in eye_colour:
                eye_colour[rec['Eyes']] += 1
            else:
                eye_colour[rec['Eyes']] = 1
print("Distribution of Gender:")
#Yellow: 3 (1.4%)
for key,value in gender.items():
    print(f"{key}: {value} ({round((value/all_superheros)*100,1)}%)")
print("\n")
print("Distribution of Eye colours for Humans:")
#Yellow: 3 (1.4%)
for key,value in eye_colour.items():
    print(f"{key}: {value} ({round((value/all_eye_colours)*100,1)}%)")
