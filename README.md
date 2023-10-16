# Guia de Execução da Aplicação

Este guia fornece instruções passo a passo para executar a aplicação utilizando Docker e Python. Certifique-se de que o Docker esteja instalado em sua máquina antes de prosseguir.

## Passo 1: Clonar o Repositório

```bash
git clone https://github.com/parisivitor/linked_list
cd linked_list
```

## Passo 2: Executar a Aplicação
Construa e inicie os contêineres Docker.
```bash
docker-compose up --build -d
```
Acesse o contêiner da aplicação.
```bash
docker exec -it qipu-linked-list-app /bin/bash
```
Uma vez dentro do contêiner, execute o aplicativo Python.
```bash
python linked_list.py
```

Se prefirir pode executar os test unitarios feitos com pytest
```bash
python test_linked_list.py
```

## Author
Vitor Risso Parisi
