<rdf:RDF
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:owl="http://www.w3.org/2002/07/owl#"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
  xmlns:ex="http://example.com/ontology#">
  <owl:Ontology rdf:about="http://example.com/ontology">
    <rdfs:comment>An example OWL ontology</rdfs:comment>
    <rdfs:label>Example Ontology</rdfs:label>
  </owl:Ontology>

  <!-- Classes -->
  <owl:Class rdf:about="http://example.com/ontology#Person">
    <rdfs:comment>A class representing a person</rdfs:comment>
    <rdfs:label>Person</rdfs:label>
  </owl:Class>
  <owl:Class rdf:about="http://example.com/ontology#Student">
    <rdfs:subClassOf rdf:resource="http://example.com/ontology#Person"/>
    <rdfs:comment>A class representing a student</rdfs:comment>
    <rdfs:label>Student</rdfs:label>
  </owl:Class>

  <!-- Properties -->
  <owl:ObjectProperty rdf:about="http://example.com/ontology#hasFriend">
    <rdfs:domain rdf:resource="http://example.com/ontology#Person"/>
    <rdfs:range rdf:resource="http://example.com/ontology#Person"/>
    <rdfs:comment>A property that relates a person to their friend</rdfs:comment>
    <rdfs:label>hasFriend</rdfs:label>
  </owl:ObjectProperty>
  <owl:DatatypeProperty rdf:about="http://example.com/ontology#hasAge">
    <rdfs:domain rdf:resource="http://example.com/ontology#Person"/>
    <rdfs:range rdf:resource="xsd:integer"/>
    <rdfs:comment>A property that relates a person to their age</rdfs:comment>
    <rdfs:label>hasAge</rdfs:label>
  </owl:DatatypeProperty>

  <!-- Individuals -->
  <ex:Person rdf:about="http://example.com/ontology#Alice">
    <ex:hasAge rdf:datatype="xsd:integer">25</ex:hasAge>
    <ex:hasFriend rdf:resource="http://example.com/ontology#Bob"/>
  </ex:Person>
  <ex:Person rdf:about="http://example.com/ontology#Bob">
    <ex:hasAge rdf:datatype="xsd:integer">30</ex:hasAge>
    <ex:hasFriend rdf:resource="http://example.com/ontology#Alice"/>
  </ex:Person>
</rdf:RDF>
