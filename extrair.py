#!/usr/bin/env python3

import os
import csv
from email import policy
from email.parser import BytesParser
from email.utils import getaddresses

PASTA_MAIL = os.path.expanduser("./vendas")
ARQUIVO_SAIDA = os.path.expanduser("./vendas.csv")

contatos = {}

nomes_enviadas = {
    ".Sent",
    ".Itens Enviados",
    ".Sent Items",
    ".Enviadas",
    ".enviadas",
    ".Sent Messages"
}

for raiz, dirs, arquivos in os.walk(PASTA_MAIL):

    # Processa apenas pastas cur dentro de pastas de enviados
    if os.path.basename(raiz) != "cur":
        continue

    pasta_pai = os.path.basename(os.path.dirname(raiz))

    if pasta_pai not in nomes_enviadas:
        continue

    print(f"\nProcessando: {raiz}", flush=True)

    for arquivo in arquivos:
        caminho = os.path.join(raiz, arquivo)

        try:
            with open(caminho, "rb") as f:
                msg = BytesParser(policy=policy.default).parse(f)

            destinatarios = getaddresses(msg.get_all("To", []))

            for nome, email in destinatarios:
                email = email.strip().lower()
                nome = nome.strip().replace('"', "")

                if not email or "@" not in email:
                    continue

                # Ignora e-mails repetidos
                if email in contatos:
                    continue

                # Se não tiver nome, usa a parte antes do @
                if not nome:
                    nome = email.split("@")[0]

                contatos[email] = nome

                print(f"[{len(contatos):6}] {email}", flush=True)

        except Exception as e:
            print(f"Erro ao ler {caminho}: {e}", flush=True)

with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([
        "First Name",
        "Last Name",
        "E-mail Address"
    ])

    for email, nome in sorted(contatos.items()):
        partes = nome.split(" ", 1)

        writer.writerow([
            partes[0],
            partes[1] if len(partes) > 1 else "",
            email
        ])

print("\nConcluído!")
print(f"Total de contatos únicos: {len(contatos)}")
print(f"Arquivo gerado: {ARQUIVO_SAIDA}")