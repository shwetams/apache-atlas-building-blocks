import json
from enum import Enum

# Inputs into the algorithm

inp_relationships = []

#ASSOCIATION, AGGREGATION, COMPOSITION 
#NONE - not at all
#ONE_TO_TWO - from end 1 to 2
#TWO_TO_ONE - from end 2 to 1
#BOTH - both ways
class relationship_category(Enum):
    ASSOCIATION = 1
    AGGREGATION = 2
    COMPOSITION = 3

class relationship_propagation(Enum):
    NONE = 1
    ONE_TO_TWO = 2
    TWO_TO_ONE = 3
    BOTH = 4
class cardinality(Enum):
    SINGLE = 1
    LIST = 2
    SET = 3

relationship_attributes = []
relationships = []
relationship = {}
relationship["category"] = "RELATIONSHIP"
relationship["created_by"] = "sg"
relationship["name"] = "adlsgen2_azure_col_map_20191013"
relationship["description"] = "linking adlsgen2 to azure sql column _20191013"
relationship["relationship_category"]= relationship_category.ASSOCIATION.name
adlsgen2_attribute = {}
adlsgen2_attribute["cardinality"] = cardinality.SINGLE.name
adlsgen2_attribute["type"] = "azure_datalake_gen2_resource_set_20191013"
adlsgen2_attribute["attributes"] = []
adlsgen2_attribute["attributes"].append({"name":"headerName"})
adlsgen2_attribute["attributes"].append({"type":"string"})
relationship_attributes.append(adlsgen2_attribute)
relationship["propagation_flow"] = relationship_propagation.BOTH.name
relationship['entity1'] = {}
relationship['entity1']['type'] = "azure_datalake_gen2_resource_set_20191013"
relationship['entity1']['name'] = "adlsgen2_file_header_20191013"
relationship['entity1']['cardinality'] = cardinality.SINGLE.name
relationship['entity1']['isLegacyAttribute'] = False

relationship['entity2'] = {}
relationship['entity2']['type'] = "azure_sql_column_sg_20191013"
relationship['entity2']['name'] = "azure_col_name_20191013"
relationship['entity2']['cardinality'] = cardinality.SINGLE.name
relationship['entity2']['isLegacyAttribute'] = False

relationship['label'] = "r:adlsgen2_Resource_Set to azure_sql_column _20191013 "

relationships.append(relationship)

print(relationships)


## Relationship


inp_base_types_param = []

## Testing new type

base_type2 = {}
base_type2['name']='DQ_Rule_20191013'
base_type2['description'] = 'a DQ Rule _20191013'
base_type2['new_attributes_defs']=[]
base_type2['new_attributes_defs'].append({"name": "rule_type","typeName": "string","isOptional": False,"cardinality": "SINGLE","valuesMinCount": 1,"valuesMaxCount": 1,"isUnique": False,"isIndexable": False,"includeInNotification": False})
base_type2['new_attributes_defs'].append({"name": "name","typeName": "string","isOptional": True,"cardinality": "SINGLE","valuesMinCount": 0,"valuesMaxCount": 1,"isUnique": False,"isIndexable": False,"includeInNotification": False})
base_type2['new_attributes_defs'].append({"name": "rule_id","typeName": "string","isOptional": True,"cardinality": "SINGLE","valuesMinCount": 0,"valuesMaxCount": 1,"isUnique": False,"isIndexable": False,"includeInNotification": False})
base_type2['created_by'] = 'sg'
base_type2['super_types'] = []
base_type2['sub_types']=[]
base_type2['category'] = 'ENTITY'
base_type2['typeVersion'] ='1.0'
inp_base_types_param.append(base_type2)

base_type = {}
base_type['name']='azure_sql_column_20191013'
base_type['description'] = 'A Column in Azure SQL Database'
base_type['new_attributes_defs']=[]
base_type['new_attributes_defs'].append({"name": "TotalCount","typeName": "long","isOptional": True,"cardinality": "SINGLE","valuesMinCount": 0,"valuesMaxCount": 1,"isUnique": False,"isIndexable": False,"includeInNotification": False})
base_type['new_attributes_defs'].append({"name": "FailedCount","typeName": "long","isOptional": True,"cardinality": "SINGLE","valuesMinCount": 0,"valuesMaxCount": 1,"isUnique": False,"isIndexable": False,"includeInNotification": False})
base_type['new_attributes_defs'].append({"name": "DataUpdateTimeStamp","typeName": "date","isOptional": True,"cardinality": "SINGLE","valuesMinCount": 0,"valuesMaxCount": 1,"isUnique": False,"isIndexable": False,"includeInNotification": False})
base_type['created_by'] = 'sg'

base_type['super_types'] = []
base_type['sub_types']=[]
base_type['category'] = 'ENTITY'
base_type['typeVersion'] ='1.0'

inp_base_types_param.append(base_type)

base_type1 = {}
base_type1['name']='azure_datalake_gen2_resource_set_20191013'
base_type1['description'] = 'A Column in Azure SQL Database _20191013'
base_type1['new_attributes_defs']=[]
base_type1['new_attributes_defs'].append({"name": "TotalCount","typeName": "long","isOptional": True,"cardinality": "SINGLE","valuesMinCount": 0,"valuesMaxCount": 1,"isUnique": False,"isIndexable": False,"includeInNotification": False})
base_type1['new_attributes_defs'].append({"name": "FailedCount","typeName": "long","isOptional": True,"cardinality": "SINGLE","valuesMinCount": 0,"valuesMaxCount": 1,"isUnique": False,"isIndexable": False,"includeInNotification": False})
base_type1['new_attributes_defs'].append({"name": "DataUpdateTimeStamp","typeName": "date","isOptional": True,"cardinality": "SINGLE","valuesMinCount": 0,"valuesMaxCount": 1,"isUnique": False,"isIndexable": False,"includeInNotification": False})

base_type1['created_by'] = 'sg'

base_type1['super_types'] = ['']
base_type1['sub_types']=[]
base_type1['category'] = 'ENTITY'
base_type1['typeVersion'] ='1.0'

inp_base_types_param.append(base_type1)

def create_relationsDefs(inp_relationships):
    relationship_defs_json = {}
    relationship_defs = []
    for inp_relationship in inp_relationships:
        relationship_def = {}
        if inp_relationship.get("name") is not None and inp_relationship.get("category") is not None and inp_relationship.get("entity1") is not None and inp_relationship.get("entity2") is not None:
            relationship_def["name"] = inp_relationship["name"]
            if inp_relationship.get("description") is not None:
                relationship_def["description"] = inp_relationship["description"]
            else:
                relationship_def["description"] = inp_relationship["name"]
            if inp_relationship.get("relationship_category") is not None:
                relationship_def["relationshipCategory"] = inp_relationship.get("relationship_category")
            else: #default relashionship category kept to Association
                relationship_def["relationshipCategory"] = relationship_category.ASSOCIATION.name
            relationship_def["end1"] = inp_relationship["entity1"]
            relationship_def["end2"] = inp_relationship["entity2"]
            if inp_relationship.get("attributes") is not None:
                relationship_def["attributeDefs"] = inp_relationship["attributes"]
            else:
                relationship_def["attributeDefs"] = []
            if inp_relationship.get("propagation_flow") is not None:
                relationship_def["propagateTags"] = inp_relationship["propagation_flow"]
            else: # default is set to both
                relationship_def["propagateTags"] = relationship_propagation.BOTH.name
            if inp_relationship.get("label") is not None:
                relationship_def["relationshipLabel"] = inp_relationship["label"]
            else:
                relationship_def["relationshipLabel"] = inp_relationship["name"]
        else:
            return relationship_defs_json 
        relationship_defs.append(relationship_def)
    relationship_defs_json = relationship_defs
    return relationship_defs_json


## Create EntityDef
def create_entityDefs(inp_base_types):
    base_file_path = 'get_typedefs.json'
#    entity_defs_json={}
    entity_defs = []
    base_type_found = False
    with open(base_file_path) as adc_gen2_typdef_file:
        adc_gen2_typedefs = json.load(adc_gen2_typdef_file)
        entityDefs = adc_gen2_typedefs['entityDefs']
        for inp_base_type in inp_base_types:
            new_entity_def={}
            new_entity_attr_defs = []
            for entityDef in entityDefs:
                if entityDef['name']==inp_base_type['name']:
                    base_type_found = True
                    new_entity_def['name'] = inp_base_type['name']
                    if entityDef.get('superTypes') is not None: 
                        new_entity_def['superTypes']=entityDef.get('superTypes')
                    else:
                        new_entity_def['superTypes'] = []
                    if entityDef.get('subTypes') is not None:
                        new_entity_def['subTypes']=entityDef.get('subTypes')
                    else:
                        new_entity_def['subTypes']= []
                    if entityDef.get('category') is not None:
                        new_entity_def['category'] = entityDef['category']
                    else:
                        new_entity_def['category'] = 'ENTITY'
                    if entityDef.get('description') is not None:
                        new_entity_def['description'] = entityDef['description']
                    else:
                        new_entity_def['description'] = inp_base_type['description']
                    if entityDef.get('attributeDefs') is not None:
                        entity_def_base_attrs = entityDef.get('attributeDefs') 
                        for entity_attr in entity_def_base_attrs:
                            new_entity_attr_defs.append(entity_attr)
                    if inp_base_type['new_attributes_defs'] is not None:
                        new_attr_to_be_added = inp_base_type['new_attributes_defs']
                        for new_attributes_def in new_attr_to_be_added:
                            new_entity_attr_defs.append(new_attributes_def)
                        
                    new_entity_def['attributeDefs'] = new_entity_attr_defs

                    if entityDef.get('typeVersion') is not None:
                        new_entity_def['typeVersion'] = entityDef.get('typeVersion')
                    else:
                        new_entity_def['typeVersion'] = '1.0'            
                    new_entity_def['createdBy'] = inp_base_type['created_by']
                    entity_defs.append(new_entity_def)
                    
            if base_type_found == False:
                if inp_base_type['super_types'] is not None:
                    new_entity_def['superTypes'] = inp_base_type['super_types']
                else:
                    new_entity_def['superTypes']= 'Asset'
                if inp_base_type['sub_types'] is not None:
                    new_entity_def['subTypes'] = inp_base_type['sub_types']
                else:
                    new_entity_def['subTypes']= []
                
                new_entity_def['name']=inp_base_type['name']
                new_entity_def['attributeDefs'] = inp_base_type['new_attributes_defs']
                new_entity_def['typeVersion'] = inp_base_type['typeVersion']
                entity_defs.append(new_entity_def)
    #entity_defs_json['entityDefs'] = entity_defs
    return entity_defs

typeDefs = {}
typeDefs["entityDefs"] = []
typeDefs["entityDefs"] = create_entityDefs(inp_base_types_param)
typeDefs["relationshipDefs"] = []
typeDefs["relationshipDefs"]=create_relationsDefs(relationships)

print(json.dumps(typeDefs))
