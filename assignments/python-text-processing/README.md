# 📘 Atividade: Python Text Processing

## 🎯 Objetivo

Praticar processamento de texto em Python trabalhando com strings, leitura e escrita de arquivos, além de manipulações comuns como limpeza, normalização e contagem de palavras.

## 📝 Tarefas

### 🛠️	Limpeza e Normalização de Strings

#### Descrição
Implemente uma função para limpar e normalizar uma linha de texto. Isso inclui remover espaços extras, converter para minúsculas e retirar pontuação básica.

#### Requisitos
O programa concluído deve:

- Criar uma função `clean_text(text: str) -> str`.
- Remover pontuação comum (`.`, `,`, `!`, `?`, `;`, `:`) e espaços duplicados.
- Retornar o texto normalizado em minúsculas.


### 🛠️	Leitura de Arquivo e Contagem de Palavras

#### Descrição
Leia um arquivo de texto linha a linha, use a função de limpeza e conte quantas vezes cada palavra aparece.

#### Requisitos
O programa concluído deve:

- Criar uma função `count_words(file_path: str) -> dict`.
- Ler o arquivo com segurança usando `with open(...)`.
- Ignorar linhas vazias e retornar um dicionário no formato `{palavra: frequencia}`.


### 🛠️	Gerar Relatório de Frequência

#### Descrição
Com base no resultado da contagem de palavras, gere um relatório ordenado e salve em um novo arquivo.

#### Requisitos
O programa concluído deve:

- Criar uma função `save_report(word_counts: dict, output_path: str) -> None`.
- Ordenar por frequência (maior para menor) e, em empate, por ordem alfabética.
- Salvar no formato `palavra: frequencia`, uma entrada por linha, em `output_path`.
