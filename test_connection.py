from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

try:
    client = MongoClient(
        os.getenv("MONGO_URI"),
        serverSelectionTimeoutMS=5000
    )

    client.admin.command("ping")

    print("Conexão com MongoDB Atlas estabelecida!")

    database = client[os.getenv("MONGO_DATABASE")]

    print(f"Banco conectado: {database.name}")

except Exception as error:
    print(f"Erro na conexão: {error}")

finally:
    if "client" in locals():
        client.close()