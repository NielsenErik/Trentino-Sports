import json
import pandas as pd
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
trentoCaps = [str(38121), str(38122),str(38123)]

def toCSV(name, f):
    print("Ma che oh")
    path = "CSV/"+name + ".csv"
    f.to_csv(path, index=False)


def trentoFac():
    pg = open('sport_web_infos.json')
    tn = json.load(pg)
    names = [] 
    email= []
    web = []
    tel = []
    gest = []
    sport = []
    address = []
    city = []

    for k in range(len(tn)):
        names.append(tn[k]['title'])
        if "Telefono: " in tn[k]['infos']:
            tel.append(tn[k]['infos']['Telefono: '])
        else:
            tel.append("")
        if "Indirizzo: " in tn[k]['infos']:
            address.append(tn[k]['infos']['Indirizzo: '].upper().replace(trentoCaps[0], "").replace(trentoCaps[1], "").replace(trentoCaps[2], ""))
        
        else:
            address.append("")
        city.append("TRENTO")
        if "E-mail: " in tn[k]['infos']:
            email.append(tn[k]['infos']['E-mail: '])
        else:
            email.append("")
        if "Sito web: " in tn[k]['infos']:
            web.append(tn[k]["infos"]["Indirizzo web: "])
        else:
            web.append("")
        if "Materia" in tn[k]['infos']:
            sport.append(tn[k]['infos']['Materia'].replace("Sport", "").replace("(", "").replace(")", "").strip())
        else:
            sport.append("")
 
    pgColoums = ['Name', 'Address', 'Municipality','Sport', 'Telephone', 'Email', 'Web']
    d = {pgColoums[0] : names, 
        pgColoums[1] : address, 
        pgColoums[2] : city, 
        pgColoums[3] : sport,
        pgColoums[4] : tel, 
        pgColoums[5] : email,
        pgColoums[6] : web,
  
        }
    pgDataset = pd.DataFrame(d)
    print(pgDataset)
    datasetName = "SportClubScraped"
    toCSV(datasetName, pgDataset)

trentoFac()