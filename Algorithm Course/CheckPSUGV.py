import requests

def returnClasses(url):
    retval = list()
    webpage = requests.get(url)
    startDelimeter = "<td>"
    contents = webpage.content.split(startDelimeter)
    qualifiers = ["DAAN","IST", "IN SC", "SWENG", "STAT", "IE", "SYSEN", "CMPSC", "CSE", "EA", "INFSY"]
    for line in contents:
        sublines = line.splitlines()
        for subline in sublines:
            for qualifier in qualifiers:
                if qualifier in subline:
                    retval.append(subline)
    desiredList = list()
    for item in retval:
        splitList = item.split(" ")
        if "IE 575" in item or "Data Communications Systems" in item:
            desired = splitList[0:2]
        elif "Prereq" in item or 'jQuery' in item or 'previously' in item:
            continue
        elif "SC" in item and "CMPSC" not in item:
            desired = splitList[0:3]
        else:
            desired = splitList[0:2]
        desiredList.append(desired)
    return desiredList[1:]

daan = returnClasses("https://greatvalley.psu.edu/academics/masters-degrees/data-analytics/curriculum-and-schedule-master-of-professional-studies")
daan = daan[0:2] + daan[3:]
sweng = returnClasses("https://greatvalley.psu.edu/academics/masters-degrees/software-engineering/curriculum-and-schedule")
endListDaan = list()
endListSweng = list()
count = 0
for item in daan:
    ''.join(item)
    if count >= 0 and count <=2:
        endItem = {"ID" : item, "type": "coreDA"}
    elif count >= 3 and count <=5:
        endItem = {"ID": item, "type": "reqDA"}
    elif count >= 6 and count <=15:
        endItem = {"ID": item, "type": "electiveDA"}
    elif count == 16:
        endItem = {"ID": item, "type": "capstoneDA"}
    count +=1
    endListDaan.append(endItem)
count = 0
for item in sweng:
    ''.join(item)
    if count >= 0 and count <=1:
        endItem = {"ID" : item, "type": "foundationSW"}
    elif count >= 2 and count <=6:
        endItem = {"ID": item, "type": "coreSW"}
    elif count >= 7 and count <=8:
        endItem = {"ID": item, "type": "capstoneSW"}
    elif count > 8:
        endItem = {"ID": item, "type": "electiveSW"}
    count +=1
    endListSweng.append(endItem)
matchingList = list()
for itemS in endListSweng:
    for itemD in endListDaan:
        if itemS.get("ID")[0] == itemD.get("ID")[0]:
            if itemS.get("ID")[1] == itemD.get("ID")[1]:
                if itemS.get("ID")[0] == "IN" and itemS.get("ID")[1] == "SC":
                    if itemS.get("ID")[2] == itemD.get("ID")[2]:
                        matchingList.append(itemD)
                else:
                    matchingList.append(itemD)
for item in matchingList:
    print item