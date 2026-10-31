import socket
import ssl

host = "ac-bsbwyv1-shard-00-00.wl6jipi.mongodb.net"
port = 27017

context = ssl.create_default_context()

try:
    with socket.create_connection((host, port), timeout=10) as connection:
        with context.wrap_socket(connection, server_hostname=host) as tls:
            print("Conexão TLS estabelecida!")
            print("Versão TLS:", tls.version())
            print("Cipher:", tls.cipher())

except Exception as error:
    print("Falha no teste TLS:")
    print(type(error).__name__, error)