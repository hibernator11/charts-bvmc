# charts-bvmc
Data for data.cervantesvirtual.com data


## query1 example

'''
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX rdaa: <http://rdaregistry.info/Elements/a/>
PREFIX rda: <http://www.rdaregistry.info/>
PREFIX rdac: <http://rdaregistry.info/Elements/c/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?s ?label (count(distinct ?w) as ?count)
where { 
  ?s ?p ?o . 
  ?s rdf:type rdac:Person .
  ?s rdfs:label ?label .
  ?w dc:subject ?s
}
group by ?s ?label
having (?count > 50)
order by desc(?count)
limit 50
'''
