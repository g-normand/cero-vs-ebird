print('USAGE : python3 get_ebird_status.py')

import requests

with open("scientific_names.txt") as fp:
    lines = fp.readlines()
    for species_name in lines:
        name = species_name.strip()
        url = f"https://species.birds.cornell.edu/bow/api/v1/auxspecies/{name}?category=conservation_status"
        resp = requests.get(url)
        if resp.status_code == 200:
            if len(resp.json()) > 0:
                is_ok = False
                for cat_info in resp.json():
                    if cat_info['fieldName'] == 'IUCN_status':
                        is_ok = True
                        print(f'{name}, {cat_info["value"]}, {cat_info["comment"]}')
                if not is_ok:
                    print(name, ', NO IUCN')
            else:
                print(name, ', NO RESULT')
        else:
            print('ERROR', resp.status_code, resp.__dict__)
