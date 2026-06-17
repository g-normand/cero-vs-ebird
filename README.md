# cero-vs-ebird

CERO records (https://ceroecuador.wordpress.com/lista-oficial/) vs eBird records (https://ebird.org/region/EC/bird-list)

Inspired by <a href="https://github.com/Zoziologie">Zoziologie</a> web apps :)

# Installation

```
git clone git@github.com:g-normand/cero-vs-ebird.git
cd cero-vs-ebird
make pip
make diff_cero_and_ebird
npm install
npm run dev
```

EBIRD VS CERO:
```
1/ Get data
make diff_cero_and_ebird

2/ Change species_list.csv

3/ Run script
npm run processSpecies

4/ Deploy
make deploy
```
