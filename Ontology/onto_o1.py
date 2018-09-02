from owlready2 import *

onto_path.append("/home/modak/Data/ontologies/onto")
# onto = get_ontology("/home/modak/Data/ontologies/po.owl").load()
onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl").load()

print(onto.Pizza)

print(onto.classes())

print(list(onto.classes()))

print(onto.base_iri)

properties = onto.properties()
for prop in properties:
    print(prop)

annotation_properties = onto.annotation_properties()

for ann_prop in annotation_properties:
    print(ann_prop)

onto.save()



