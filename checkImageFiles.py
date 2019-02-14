from neo4j import GraphDatabase
import requests

uri = "bolt://kb.virtualflybrain.org:7688"
driver = GraphDatabase.driver(uri, auth=("neo4j", "vfb"))

files=['thumbnail.png','thumbnailT.png','volume.nrrd','volume.wlz','volume.obj','volume.swc']

def check_folders(tx):
    for record in tx.run("MATCH (ic:Individual)-[r:in_register_with]->(t:Template) RETURN r.folder, ic.short_form"):
      
      try:
        for file in files:
			    request = requests.get(record["r.folder"] + file)
			    if request.status_code != 200: 
				    print(record["r.folder"] + file + ' does not exist (' + str(request.status_code) + ')')
      except:
			  KeyError
			  print('no folder for ' +  record["ic.short_form"])

with driver.session() as session:
    session.read_transaction(check_folders)
