# Maildir Contact Extractor

Script em Python para extrair contatos únicos dos e-mails enviados de uma conta em estrutura **Maildir** e gerar um arquivo CSV para importação de contatos.

## Funcionalidades

* Permite informar a pasta da conta via terminal.
* Processa mensagens enviadas em pastas como `.Sent`, `.Sent Items` e `.Itens Enviados`.
* Extrai destinatários do campo `To`.
* Remove e-mails duplicados.
* Gera CSV com nome automático baseado na pasta da conta.
* Permite definir um arquivo de saída personalizado.

## Requisitos

* Python 3

Nenhuma biblioteca externa é necessária.

## Como usar

```bash
python3 extrair.py caminho/da/conta
```

Exemplo:

```bash
python3 extrair.py vendas
```

Isso irá gerar automaticamente:

```text
vendas.csv
```

Também é possível definir o arquivo de saída:

```bash
python3 extrair.py vendas -o contatos.csv
```

## Estrutura esperada

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

## Pastas de enviados suportadas

* `.Sent`
* `.Itens Enviados`
* `.Sent Items`
* `.Enviadas`
* `.enviadas`
* `.Sent Messages`

## Saída CSV

O arquivo gerado possui o seguinte formato:

```csv
First Name,Last Name,E-mail Address
João,Silva,joao@email.com
Maria,Souza,maria@email.com
```

## Exemplo de execução

```text
Processando: /caminho/da/conta/.Sent/cur
[     1] cliente@email.com

Concluído!
Total de contatos únicos: 1
Arquivo gerado: /caminho/do/projeto/vendas.csv
```

## Licença

Uso livre.
