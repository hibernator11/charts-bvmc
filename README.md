# charts-bvmc
Data for data.cervantesvirtual.com data


## query1 example


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

## query2 example

    PREFIX rdaw: <http://rdaregistry.info/Elements/w/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaa: <http://rdaregistry.info/Elements/a/>
    PREFIX rda: <http://www.rdaregistry.info/>
    PREFIX rdac: <http://rdaregistry.info/Elements/c/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    select distinct ?subject ?subjectLabel ?researcher ?researcherLabel
    where{
        ?w dc:subject ?subject .
        ?w rdaw:author ?researcher .
        ?researcher rdfs:label ?researcherLabel .
        ?subject rdfs:label ?subjectLabel .
        FILTER (?subject != ?researcher)
        {select distinct ?subject (count(distinct ?researcher) as ?total)
        where {
           ?work dc:subject ?subject .
           ?subject rdf:type rdac:Person .
           ?work rdaw:author ?researcher .
        }
        group by ?subject
        having (?total > 10)
        order by desc(?total)
        }
    }
    limit 5000
    
    
## query 3 example

    PREFIX rdaw: <http://rdaregistry.info/Elements/w/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX rdaa: <http://rdaregistry.info/Elements/a/>
    PREFIX rda: <http://www.rdaregistry.info/>
    PREFIX rdac: <http://rdaregistry.info/Elements/c/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    select distinct ?subject ?subjectLabel ?researcher ?researcherLabel
    where{
        ?w dc:subject ?subject .
        ?subject rdf:type rdac:Person .
        ?w rdaw:author ?researcher .
        ?researcher rdf:type rdac:Person .
        ?researcher rdfs:label ?researcherLabel .
        ?subject rdfs:label ?subjectLabel .
        FILTER (?subject != ?researcher)
        {select distinct ?subject (count(distinct ?researcher) as ?total)
        where {
           ?work dc:subject ?subject .
           ?subject rdf:type rdac:Person .
           ?work rdaw:author ?researcher .
        }
        group by ?subject
        having (?total > 10)
        order by desc(?total)
        }
       {select distinct ?researcher (count(distinct ?subject) as ?total)
        where {
           ?work dc:subject ?subject .
           ?subject rdf:type rdac:Person .
           ?work rdaw:author ?researcher .
        }
        group by ?researcher
        having (?total > 1)
        order by desc(?total)
        }
    }
    limit 5000
