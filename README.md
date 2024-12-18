# Projeto ETL Python

## 📝 Descrição
Um projeto ETL (Extract, Transform, Load) em Python que extrai dados de APIs, processa as informações e as carrega em um destino específico.

## 🚀 Funcionalidades
- Extração automatizada de dados via API
- Transformação de dados em tempo real
- Carregamento de dados processados
- Tratamento de erros e logs

## 🛠️ Tecnologias
- Python 3.x
- pandas
- requests
- python-dotenv

## 🔧 Configuração
1. Clone o repositório:
```

git clone https://github.com/seu-usuario/projeto-etl-python.git
cd projeto-etl-python
```

2. Instale as dependências:
```

pip install -r requirements.txt
```

3. Configure as variáveis de ambiente no arquivo `.env`:
```

API_KEY=sua_chave_api
API_URL=url_da_api
OUTPUT_PATH=data/output
```

## 📊 Estrutura do Projeto
```

projeto-etl-python/
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── config/
│   └── config.py
├── data/
│   ├── raw/
│   └── processed/
├── logs/
├── tests/
├── .env
├── requirements.txt
└── README.md
```

## 🚀 Como Executar
```

python src/main.py
```

## 📈 Fluxo de Dados
1. **Extração**: Coleta de dados da API
2. **Transformação**: Processamento e limpeza dos dados
3. **Carregamento**: Armazenamento no destino

## 🤝 Como Contribuir
1. Faça um Fork do projeto
2. Crie sua Branch de recurso (`git checkout -b feature/NovoRecurso`)
3. Faça commit das alterações (`git commit -m 'Adiciona NovoRecurso'`)
4. Faça Push para a Branch (`git push origin feature/NovoRecurso`)
5. Abra um Pull Request

## 📝 Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## ✒️ Autor
* Seu Nome - [Perfil GitHub](https://github.com/seu-usuario)
```

Principais alterações feitas:
1. Tradução completa para português
2. Simplificação das seções de descrição e funcionalidades
3. Especificação das tecnologias principais
4. Instruções de configuração mais diretas
5. Estrutura de projeto mais clara
6. Remoção de seções redundantes
7. Adição de estrutura adequada para o diretório de dados
8. Simplificação da seção de contribuição

