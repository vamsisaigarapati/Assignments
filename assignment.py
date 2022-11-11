import os
import csv
import re

path = "C://Users//vgara1//Downloads//Asn2CountRequests//RequestFiles"
subject_codes = ["RSC\d\d\d", "BWE\d\d\d", "RPD\d\d\d", "SMP\d\d\d"]
crs_req_cnt = {}
dir_list = os.listdir(path)
for file_name in os.listdir(path):
    with open(path+'/'+file_name, 'r', encoding = "utf-8") as f:
        dict_r = csv.DictReader(f)
        for request in dict_r:
            full_list=[]
            for key,value in request.items():
                full_list.append(value)
            i=0
            while(i<len(full_list)):
                course=full_list[i]
                try:
                    section=full_list[i+1]
                except IndexError:
                    if type(course) is list:
                        full_list=full_list+course
                        i=i+1
                        continue
                    else:
                        break
                if course == None or section == None:
                    i=i+2
                    continue
                course = course.replace(' ','')
                for j in subject_codes:
                    course_name=re.findall(f"{j}", course)
                    if course_name:
                        if section.isdigit() and len(str(section))<=3:
                            section=section.zfill(3)
                            name=f"{course_name[0]}-{section}"
                            if name in crs_req_cnt:
                                crs_req_cnt[name]=crs_req_cnt[name]+1
                            else:
                                crs_req_cnt[name]=1
                i=i+2
for course,count in crs_req_cnt.items():
    print(f"{course} {count}")
