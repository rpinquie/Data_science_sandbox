from py2neo import Graph, Node, Relationship

graph = Graph()

graph.delete_all()

# CREATE NODES
nicole = Node("Person", name="Nicole", age=24)
drew = Node("Person", name="Drew", age=20)
mtdew = Node("Drink", name="Mountain Dew", calories=9000)
cokezero = Node("Drink", name="Coke Zero", calories=0)
coke = Node("Manufacturer", name="Coca Cola")
pepsi = Node("Manufacturer", name="Pepsi")
orangina = Node("Manufacturer", name="Orangina")

graph.create(nicole | drew | mtdew | cokezero | coke | pepsi)

# CREATE RELATIONSHIP
graph.create(Relationship(nicole, "LIKES", cokezero))
graph.create(Relationship(nicole, "LIKES", mtdew))
graph.create(Relationship(drew, "LIKES", mtdew))
graph.create(Relationship(coke, "MAKES", cokezero))
graph.create(Relationship(pepsi, "MAKES", mtdew))

# CYPHER QUERY
query1 = """
match (n:Person)-[:LIKES]->(m:Drink)
WHERE m.name="Coke Zero"
RETURN (n.name) 
"""

data = graph.run(query1)

for d in data:
    print(d)
    
# PARAMETRIZED CYPHER QUERY
query2 = """
MATCH (p:Person)-[:LIKES]->(drink:Drink)
WHERE p.name = {name}
RETURN p.name AS name, AVG(drink.calories) AS avg_calories
"""

data = graph.run(query2, name="Nicole")

for d in data:
    print(d)