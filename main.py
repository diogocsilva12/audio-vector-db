import weaviate
import json

client = weaviate.Client("http://localhost:8080")

schema = json.load(open("weaviate_config.json"))
client.schema.create(schema)

print("Schema criado com sucesso!")
