from rdflib import Graph
g = Graph()
g.parse('intelligence-rdf.owl', format='application/rdf+xml')
g.serialize('intelligence-json.owl', format="json-ld")