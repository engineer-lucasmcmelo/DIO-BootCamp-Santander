# Projeto: Simulação de Ataque de Força Bruta com Medusa

Projeto desenvolvido durante o **Bootcamp Santander Cibersegurança (DIO)**. O objetivo é simular, em ambiente controlado e autorizado, um ataque de força bruta contra uma máquina virtual local (Metasploitable) utilizando a ferramenta **Medusa** e wordlists próprias.

> **Uso educacional e autorizado.** Execute apenas em laboratório/local (VMs suas). Ataques a sistemas de terceiros sem autorização são ilegais.

## Estrutura do projeto

```
.
├── README.md
├── images/             # Capturas de tela do laboratório
├── scripts/
│   └── bruteforce.py   # Automação do ataque com Medusa
└── wordlist/
    ├── username        # Lista de usuários
    └── password        # Lista de senhas
```

## Pré-requisitos

- Kali Linux (ou similar) como máquina atacante
- Metasploitable (ou outra VM vulnerável) como alvo
- Medusa instalado: `sudo apt install medusa`
- Python 3

## Configuração do laboratório

1. Suba a VM alvo (Metasploitable) e a VM atacante (Kali) na mesma rede (host-only/NAT).
2. Descubra o IP do alvo: `ifconfig` ou `ip a` na VM alvo.
3. Teste conectividade: `ping <IP_DO_ALVO>`.

## Execução manual (Medusa)

```bash
medusa -h <IP_DO_ALVO> -U wordlist/username -P wordlist/password -M ssh
```

## Execução automatizada (Python)

```bash
python3 scripts/bruteforce.py -H 192.168.56.101
```

## Wordlists

As wordlists estão em `wordlist/`:

- `username` — lista de usuários candidatos
- `password` — lista de senhas candidatas

## Mitigações recomendadas

- Políticas de senha forte e rotação
- Bloqueio de conta após tentativas falhas
- Autenticação multifator (MFA)
- Monitoramento e alertas de tentativas de login

## Referências

- Medusa: https://github.com/jmk-foofus/medusa
- Metasploitable: https://sourceforge.net/projects/metasploitable/
- DIO — Santander Cibersegurança

