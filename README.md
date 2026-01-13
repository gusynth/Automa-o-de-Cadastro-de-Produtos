# Automação de Cadastro de Produtos

Este projeto é um script em Python que automatiza o cadastro de produtos em um sistema web, utilizando um arquivo CSV como base de dados. Ele abre o navegador, acessa o sistema, faz login automaticamente e preenche o formulário de produtos linha a linha.

## Tecnologias utilizadas

- Python 3
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [pandas](https://pandas.pydata.org/)
- Arquivo CSV para base de dados

## Funcionalidades

- Abre o navegador automaticamente.
- Acessa a URL do sistema de cadastro.
- Realiza login com e-mail e senha configurados no código.
- Lê os dados de produtos a partir de um arquivo `produtos.csv`.
- Preenche automaticamente os campos do formulário (código, marca, tipo, categoria, preço unitário, custo e observações).
- Cadastra todos os produtos da base de dados de forma sequencial.

## Pré-requisitos

- Python 3 instalado.
- Bibliotecas instaladas:
  ```bash
  pip install pyautogui pandas
****
