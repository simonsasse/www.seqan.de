import bibtexparser
import json
import yaml

json_file = "_data/publications.json"
yml_file = "_data/publications.yml"
bib_file = "_data/publications.bib"

# parse the bibtex file
with open(bib_file) as bibtex_file:
    bib = bibtexparser.load(bibtex_file)

# parse the json file
with open(json_file) as js_file:
    js = json.load(js_file)

for entry in js:
    # replace the keys
    entry["key"] = "fu_mi_publications" + str(entry["eprintid"])
    # extract the corresponding bibtex entry
    temp_entry = bib.entries_dict[entry["key"]]
    # create new temporary database
    temp_db = bibtexparser.bibdatabase.BibDatabase()
    # Insert temporary entry into temporary Database
    temp_db.entries = [temp_entry]
    # insert bibtex string into the json entry
    entry["bibtex"] = bibtexparser.dumps(temp_db)
    del temp_db, temp_entry
# write sorted entries to yml
with open( yml_file, 'w') as out_file:
    documents = yaml.dump(sorted(js, key=lambda x: x['key']), out_file, explicit_start=True)
