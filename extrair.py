#!/usr/bin/env python3

import os
import csv
import argparse
from email import policy
from email.parser import BytesParser
from email.utils import getaddresses


def main():
    parser = argparse.ArgumentParser(
        description="Extrai contatos únicos dos e-mails enviados em uma estrutura Maildir."
    )

    parser.add_argument(
        "conta",
        help="Caminho da pasta Maildir da conta. Ex.: vendas, suporte, comercial"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Arquivo CSV de saída. Ex.: contatos.csv"
    )

    args = parser.parse_args()

    pasta_mail = os.path.abspath(os.path.expanduser(args.conta))

    if not os.path.isdir(pasta_mail):
        print(f"Erro: pasta não encontrada: {pasta_mail}")
        return

    if args.output:
        arquivo_saida = os.path.abspath(os.path.expanduser(args.output))
    else:
        nome_conta = os.path.basename(pasta_mail.rstrip(os.sep))
        arquivo_saida = os.path.abspath(f"{nome_conta}.csv")

    contatos = {}

    nomes_enviadas = {
        ".Sent",
        ".Itens Enviados",
        ".Sent Items",
        ".Enviadas",
        ".enviadas",
        ".Sent Messages"
    }

    for raiz, dirs, arquivos in os.walk(pasta_mail):
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

                    if email in contatos:
                        continue

                    if not nome:
                        nome = email.split("@")[0]

                    contatos[email] = nome

                    print(f"[{len(contatos):6}] {email}", flush=True)

            except Exception as e:
                print(f"Erro ao ler {caminho}: {e}", flush=True)

    with open(arquivo_saida, "w", newline="", encoding="utf-8-sig") as csvfile:
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
    print(f"Arquivo gerado: {arquivo_saida}")


if __name__ == "__main__":
    main()