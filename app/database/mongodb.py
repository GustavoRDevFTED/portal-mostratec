from flask import current_app
from pymongo import MongoClient
from pymongo.errors import PyMongoError

_client = None
_database = None


def init_database(app):
    global _client, _database

    uri = app.config.get("MONGO_URI")
    if not uri:
        app.logger.warning("MONGO_URI não configurada. Configure o arquivo .env.")
        return

    try:
        _client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        _client.admin.command("ping")
        _database = _client[app.config["MONGO_DATABASE"]]
        app.logger.info("Conexão com MongoDB Atlas estabelecida.")
    except PyMongoError:
        app.logger.exception("Não foi possível conectar ao MongoDB Atlas.")
        _client = None
        _database = None


def get_database():
    if _database is None:
        raise RuntimeError(
            "Banco de dados indisponível. Verifique MONGO_URI, usuário, senha "
            "e Network Access no MongoDB Atlas."
        )
    return _database