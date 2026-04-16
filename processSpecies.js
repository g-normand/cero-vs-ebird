import csvtojson from "csvtojson";
import fs from "fs";

const sp = await csvtojson.csv().fromFile("data/species_list.csv")


const sp_category = sp.map(s => {
    return {
        english_name: s.english_name,
        species_code: s.species_code,
        scientific_name: s.scientific_name,
        category: s.category,
        notes:s.notes,
        ebird_checklist:s.ebird_checklist,
    }
})


await fs.writeFileSync('src/assets/species_list.json', JSON.stringify(sp_category));