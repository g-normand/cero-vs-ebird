# cero-vs-ebird

CERO records (https://ceroecuador.wordpress.com/lista-oficial/) vs eBird records (https://ebird.org/region/EC/bird-list)

Inspired by <a href="https://github.com/Zoziologie">Zoziologie</a> web apps :)

# Installation

```
git clone git@github.com:g-normand/cero-vs-ebird.git
cd cero-vs-ebird
npm install

FOR DEV:
npm run dev

FOR PROD:
make deploy
```

With new species:
```
Add species in data/species_list.csv
npm run processSpecies
```
