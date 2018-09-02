from owlready2 import *

onto = get_ontology("http://test.org/onto.owl")

props = onto.properties()
for prop in props:
    print(prop)