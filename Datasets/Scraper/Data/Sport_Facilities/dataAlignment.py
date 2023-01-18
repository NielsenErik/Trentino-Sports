import json
import pandas as pd
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
trentoCaps = [str(38121), str(38122),str(38123)]

def toCSV(name, f):
    path = "CSV/"+name + ".csv"
    f.to_csv(path, index=False)

def pagineGialle():
    pg = open('PagineGialle_facilities_web_infos.json')
    pagineGialle = json.load(pg)
    names = [] 
    openings = []
    tel = []
    typeFac = []
    address = []
    city = []
    cap = []
    i = 0
    for k in range(len(pagineGialle)):
        names.append(pagineGialle[k]['title'])
        tel.append(pagineGialle[k]['Telephone']['Telephone'])
        typeFac.append(pagineGialle[k]['Type_of_facility']['Type'])
    for k in range(len(pagineGialle)):
        address.append(pagineGialle[k]['Address']['Address'][0].upper())
        city.append(pagineGialle[k]['Address']['Address'][1])
    for k in range(len(pagineGialle)):
        openings.append(pagineGialle[k]['Openings'])

    for i in range(len(city)):
        city[i] = city[i].replace("(TN)", "")
        tmp = city[i].split()
        cap.append(tmp[0])
        city[i] = tmp[1].upper()

    pgColoums = ['Name', 'Address', 'Municipality', 'CAP','OpeningHours', 'Telephone', 'Type']
    d = {pgColoums[0] : names, 
        pgColoums[1] : address, 
        pgColoums[2] : city, 
        pgColoums[3] : cap,
        pgColoums[4] : openings, 
        pgColoums[5] : tel, 
        pgColoums[6] : typeFac
        }
    pgDataset = pd.DataFrame(d)
    print(pgDataset)
    datasetName = "PagineGialleScraped"
    toCSV(datasetName, pgDataset)
def trentoFac():
    pg = open('trento_facilities_web_infos.json')
    tn = json.load(pg)
    names = [] 
    email= []
    web = []
    tel = []
    gest = []
    typeFac = []
    address = []
    city = []

    for k in range(len(tn)):
        names.append(tn[k]['title'])
        if "Telefono" in tn[k]['infos']:
            tel.append(tn[k]['infos']['Telefono'])
        else:
            tel.append("")
        typeFac.append(tn[k]['infos']['Tipologia di luogo'])
        address.append(tn[k]['infos']['Indirizzo'].upper().replace(trentoCaps[0], "").replace(trentoCaps[1], "").replace(trentoCaps[2], ""))
        address
        city.append("TRENTO")
        if "E-mail" in tn[k]['infos']:
            email.append(tn[k]['infos']['E-mail'])
        else:
            email.append("")
        if "Indirizzo web" in tn[k]['infos']:
            web.append(tn[k]["infos"]["Indirizzo web"])
        else:
            web.append("")
        if "Impianto gestito da" in tn[k]['infos']:
            gest.append(tn[k]['infos']['Impianto gestito da'])
        else:
            gest.append("")
    print(len(names), " ", len(email), " ", len(web), " ", len(tel), " ", len(gest), " ", len(typeFac), " ",len(address), " ", len(city), " ")
    pgColoums = ['Name', 'Address', 'Municipality','Gestione', 'Telephone', 'Email', 'Web', 'Type']
    d = {pgColoums[0] : names, 
        pgColoums[1] : address, 
        pgColoums[2] : city, 
        pgColoums[3] : gest, 
        pgColoums[4] : tel, 
        pgColoums[5] : email,
        pgColoums[6] : web,
        pgColoums[7] : typeFac
        }
    pgDataset = pd.DataFrame(d)
    print(pgDataset)
    datasetName = "TrentoComuneScraped"
    toCSV(datasetName, pgDataset)

def arcooFac():
    pg = open('arco_facilities_web_infos.json')
    tn = json.load(pg)
    names = [] 
    email= []
    web = []
    tel = []
    typeFac = []
    address = []
    city = []

    for k in range(len(tn)):
        names.append(tn[k]['title'])
        if "Telefono" in tn[k]['infos']:
            tel.append(tn[k]['infos']['Telefono'])
        else:
            tel.append("")
        if "Tipologia" in tn[k]['infos']:
            typeFac.append(tn[k]['infos']['Tipologia'])
        else:
            typeFac.append("")
        address.append(tn[k]['infos']['Indirizzo'].upper())
        city.append("ARCO")
        if "Email" in tn[k]['infos']:
            email.append(tn[k]['infos']['Email'])
        else:
            email.append("")
        if "Sito WEB" in tn[k]['infos']:
            web.append(tn[k]["infos"]["Sito WEB"])
        else:
            web.append("")
    print(len(names), " ", len(email), " ", len(web), " ", len(tel), " ", " ", len(typeFac), " ",len(address), " ", len(city), " ")
    pgColoums = ['Name', 'Address', 'Municipality', 'Telephone', 'Email', 'Web', 'Type']
    d = {pgColoums[0] : names, 
        pgColoums[1] : address, 
        pgColoums[2] : city,
        pgColoums[3] : tel, 
        pgColoums[4] : email,
        pgColoums[5] : web,
        pgColoums[6] : typeFac
        }
    pgDataset = pd.DataFrame(d)
    print(pgDataset)
    datasetName = "ArcoComuneScraped"
    toCSV(datasetName, pgDataset)


pagineGialle()
trentoFac()
arcooFac()

