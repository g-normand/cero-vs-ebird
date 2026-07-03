from openpyxl import load_workbook
from bs4 import BeautifulSoup
import requests
from datetime import datetime

CERO = {'x': 'confirmed', 'nb': 'non breeding', 'in': 'introduced', 'ex':'extinct', 'e': 'endemic', 
'x/nb': 'confirmed + non breeding', 'v': 'vagrant', 'un': 'unconfirmed', 'un(i)' : 'introduced not breeding'}
simple = False


def extract_cero_data():
    wb = load_workbook("data/ecuador_lista-master-final_2025_v4.xlsx")
    ws = wb.active  # or wb["Sheet1"]
    cero_data = {}
    cero_unconfirmed = {}
    cero_introduced = {}
    for row in ws.iter_rows(min_row=2):
        english_name = row[18].value   # Column S (Clem Common Name)
        value = row[4].value # Column E
    
        if english_name is not None:
            if simple:
                cero_data[english_name] = CERO[value]
            else:
                cero_data[english_name] = f"cero,,{english_name},,{CERO[value]},"
            if value == 'un':
                if simple:
                     cero_unconfirmed[english_name] = CERO[value]
                else:
                     cero_unconfirmed[english_name] = f"cero_unconfirmed,,{english_name},,{CERO[value]},"
            if value == 'in':
               cero_introduced[english_name] = CERO[value]
    return cero_data, cero_unconfirmed, cero_introduced

def extract_observation_dates(url):
    ebird_data = {}
    ebird_checklists = {}
    website = requests.get(url)
    soup = BeautifulSoup(website.text, 'html.parser')

    for li in soup.find_all('li', class_='BirdList-list-list-item'):
        time_tag = li.find('time')
        is_sensitive = li.find('button', class_='Sensitive-badge') is not None
        if (time_tag and time_tag.has_attr('datetime')) or is_sensitive:
            ebird_id = li.get('id')
            english_name = li.find('span', class_='Species-common').get_text(strip=True)
            checklist = ''
            if 'sp.' in english_name or '/' in english_name or '(hybrid)' in english_name or 'undescribed' in english_name:
                continue
            is_exotic = li.find('svg', class_='Icon--exoticEscapee') is not None
            if is_exotic:
                continue
            is_provisional = li.find('svg', class_='Icon--exoticProvisional') is not None
            if is_provisional:
                continue

            is_naturalized = li.find('svg', class_='Icon--exoticNaturalized') is not None
            if is_naturalized:
                value = f'dato ebird (NATURALIZED)'
            elif time_tag:
                checklist = li.find('div', class_='Obs-date').find('a').get('href')
                ebird_checklists[english_name] = checklist
                value = f'dato en ebird ({datetime.strptime(time_tag["datetime"], "%Y-%m-%d %H:%M")})'
            else:
                value = 'dato en ebird'
             
            if simple:
                ebird_data[english_name] = value
            else:
                ebird_data[english_name] = f'ebird,,{english_name},https://ebird.org/species/{ebird_id},{value},{checklist}'
    return ebird_data, ebird_checklists

ebird_data, ebird_checklists = extract_observation_dates('https://ebird.org/region/EC/bird-list')
cero_data, cero_unconfirmed, cero_introduced = extract_cero_data()

only_in_ebird = {k: ebird_data[k] for k in ebird_data.keys() - cero_data.keys()}
only_in_cero = {k: cero_data[k] for k in cero_data.keys() - ebird_data.keys()}

print(f'ONLY IN EBIRD ({len(only_in_ebird)})')
for english_name in only_in_ebird:
    if simple:
        print(english_name, ' : ', ebird_data[english_name])
    else:
        print(ebird_data[english_name])
print('')
print(f'ONLY IN CERO ({len(only_in_cero)})')
for english_name in only_in_cero:
    if simple:
        print(english_name, ' : ', cero_data[english_name])
    else:
        print(cero_data[english_name])
print('')
print('___ INTRODUCED IN THE CERO LIST__')
for english_name in cero_introduced:
    if simple:
        print(english_name, ' : ', ebird_data[english_name])
    else:
        print(ebird_data[english_name].replace('ebird,', 'introduced,'))
print('')
print('___UNCONFIRMED IN THE CERO LIST__')
for english_name in cero_unconfirmed:
    if simple:
        print(english_name, ' ; ', ebird_data[english_name] if english_name in ebird_data else 'NO DATA',' ; ', ebird_checklists[english_name] if english_name in ebird_checklists else 'NO DATA')
    else:
        print(ebird_data[english_name].replace('ebird,', 'unconfirmed,') if english_name in ebird_data else f'unconfirmed,,{english_name},,,')
