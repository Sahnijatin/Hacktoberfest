from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to Neo4j
uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USERNAME")
password = "inMorphis24"

try:
    driver = GraphDatabase.driver(uri, auth=(user, password))

    with driver.session() as session:
        result = session.run("RETURN 'Connection Successful!' AS message")
        print(result.single()['message'])

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.close()
