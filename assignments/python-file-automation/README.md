# 📘 Atividade: Automação de Arquivos em Python

## 🎯 Objetivo

Os alunos vão praticar leitura e escrita de arquivos CSV em Python, transformando dados brutos em informações organizadas e fáceis de consultar. Ao final, eles terão uma pequena ferramenta para carregar registros, analisar conteúdo e gerar um relatório resumido.

## 📝 Tarefas

### 🛠️ Carregar Registros de um CSV

#### Descrição
Implemente uma função para ler um arquivo CSV com registros de arquivos da escola. Cada linha representa um item com colunas como nome, tipo e tamanho.

#### Requisitos
O programa concluído deve:

- Criar uma função `load_files(file_path: str) -> list[dict]`.
- Ler o CSV usando `with open(...)` e `csv.DictReader`.
- Ignorar linhas vazias e retornar uma lista de dicionários.


### 🛠️ Calcular um Resumo dos Arquivos

#### Descrição
Use os dados carregados para contar quantos arquivos existem por tipo e identificar o maior arquivo da lista.

#### Requisitos
O programa concluído deve:

- Criar uma função `build_summary(files: list[dict]) -> dict`.
- Contar quantos registros existem para cada tipo de arquivo.
- Encontrar o arquivo com maior tamanho e incluir essa informação no resumo.


### 🛠️ Gerar um Relatório em Texto

#### Descrição
Com base no resumo calculado, salve um relatório simples em um novo arquivo de texto.

#### Requisitos
O programa concluído deve:

- Criar uma função `save_report(summary: dict, output_path: str) -> None`.
- Escrever o relatório em um formato legível, com uma linha por informação.
- Salvar o arquivo de saída usando `with open(...)`.
