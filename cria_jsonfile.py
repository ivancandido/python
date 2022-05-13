import json
dicionario = {
  "CHAVES": ["CHAVES DO 8", "14/04/2017", "RECEP_01"],
  "QUICO": ["QUICO FLORES", "04/05/2018", "RAIOX_01"],
  "FLORINDA": ["DONA FLORINDA", "30/08/2020", "RECEP_03"]
}
with open("novobd.json", "w") as json_file:
    json.dump(dicionario, json_file)