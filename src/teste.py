import os
from dotenv import load_dotenv

print("Diretório atual:", os.getcwd())
print("Caminho do .env sendo usado:", os.path.abspath('.env'))

# Carrega o arquivo .env
load_dotenv(override=True)

# Lê e imprime as variáveis
env_vars = {
    "POSTGRES_USER": os.getenv("POSTGRES_USER"),
    "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD"),
    "POSTGRES_HOST": os.getenv("POSTGRES_HOST"),
    "POSTGRES_PORT": os.getenv("POSTGRES_PORT"),
    "POSTGRES_DB": os.getenv("POSTGRES_DB")
}

print("\nVariáveis carregadas:")
for key, value in env_vars.items():
    # Oculta a senha ao imprimir
    if key == "POSTGRES_PASSWORD":
        print(f"{key}: {'*' * len(value) if value else 'None'}")
    else:
        print(f"{key}: {value}")

# Construir e imprimir a URL de conexão (com senha oculta)
if all(env_vars.values()):  # Verifica se todas as variáveis têm valor
    db_url = (
        f"postgresql://{env_vars['POSTGRES_USER']}:****"
        f"@{env_vars['POSTGRES_HOST']}:{env_vars['POSTGRES_PORT']}/{env_vars['POSTGRES_DB']}"
    )
    print("\nURL de conexão (senha oculta):", db_url)
else:
    print("\nALERTA: Algumas variáveis de ambiente estão faltando!")