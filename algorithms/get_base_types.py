import json
## Load the typedefs
file_path = 'get_typedefs.json'
base_types = []
with open(file_path) as adc_gen2_typdef_file:
    adc_gen2_typedefs = json.load(adc_gen2_typdef_file)
    entityDefs = adc_gen2_typedefs['entityDefs']
    for entityDef in entityDefs:
        ## Extract the list of entity categories (can modify it to others later)
        if entityDef['category'] == "ENTITY":
            base_type = {}
            base_type['name'] = entityDef['name']
            base_type['description'] = entityDef['description']
            base_type['attributes'] = entityDef['attributeDefs']
            ## Build the list to return
            base_types.append(base_type)
    


