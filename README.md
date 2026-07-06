# Maildir Contact Extractor

Script em Python para extrair contatos únicos dos e-mails enviados armazenados em uma estrutura **Maildir** e gerar um arquivo CSV compatível com importação de contatos.

## Funcionalidades

* Percorre uma estrutura Maildir.
* Processa apenas mensagens da pasta **Enviados** (`Sent`, `Itens Enviados`, etc.).
* Extrai os destinatários do campo **To**.
* Remove endereços de e-mail duplicados.
* Gera um arquivo CSV no formato:

| First Name | Last Name | E-mail Address |
| ---------- | --------- | -------------- |

## Requisitos

* Python 3.8 ou superior

Nenhuma biblioteca externa é necessária.

## Estrutura esperada

O script procura uma pasta chamada `vendas` no mesmo diretório onde é executado.

Exemplo:

```text
projeto/
├── extrair.py
└── vendas/
    ├── .Sent/
    │   └── cur/
    ├── .Itens Enviados/
    │   └── cur/
    └── ...
```

## Como executar

```bash
python3 extrair.py
```

Ao final será criado o arquivo:

```text
vendas.csv
```

## Formato do CSV

Exemplo:

```csv
First Name,Last Name,E-mail Address
João,Silva,joao@email.com
Maria,Souza,maria@email.com
```

## Pastas de enviados suportadas

O script reconhece automaticamente as seguintes pastas:

* `.Sent`
* `.Sent Items`
* `.Sent Messages`
* `.Itens Enviados`
* `.Enviadas`
* `.enviadas`

Caso utilize outro nome, basta adicioná-lo ao conjunto `nomes_enviadas`.

## Funcionamento

Durante a execução o script:

1. Percorre todas as pastas da estrutura Maildir.
2. Localiza apenas os diretórios `cur` pertencentes às pastas de enviados.
3. Lê cada mensagem utilizando o módulo `email` da biblioteca padrão.
4. Extrai todos os destinatários do cabeçalho `To`.
5. Remove endereços duplicados.
6. Divide o nome em **First Name** e **Last Name**.
7. Gera um arquivo `vendas.csv` codificado em UTF-8 com BOM, compatível com Microsoft Excel.

## Exemplo de saída

```text
Processando: ./vendas/.Sent/cur
[     1] contato1@email.com
[     2] contato2@email.com
...

Concluído!
Total de contatos únicos: 2547
Arquivo gerado: ./vendas.csv
```

## Licença

Este projeto pode ser utilizado e modificado livremente conforme sua necessidade.
