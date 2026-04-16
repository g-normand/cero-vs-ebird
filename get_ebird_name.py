print('USAGE : python3 get_ebird_name.py --key EBIRD_API_KEY')

import requests
import argparse

parser = argparse.ArgumentParser("get_ebird_name")
parser.add_argument("--key", help="Ebird API Key.", type=str)
args = parser.parse_args()
ebird_api_key = args.key

locale = 'en'

with open("scientific_names.txt") as fp:
    lines = fp.readlines()
    for species_name in lines:
        parts = species_name.strip().split(',')
        name = parts[2].strip()
        resp = requests.get(f'https://api.ebird.org/v2/ref/taxon/find?locale={locale}&cat=species&limit=150&key={ebird_api_key}&q={name}')
        if resp.status_code == 200:
            if len(resp.json()) > 0:
                parts[3] = f"https://ebird.org/species/{resp.json()[0]['code']}"
                new_line = ','.join(parts)
                print(new_line)
            else:
                print(name, ', NO RESULT')
        else:
            print('ERROR', resp.status_code, resp.__dict__)
