#Validador de formulário e extrator de e-mails com expressões regulares.

import re

# 1. PADRÕES 
PADROES = {
    # Letras e espaços, de 1 a 50 caracteres
    "Nome": r"[a-zA-Z ]{1,50}",

    # 11 dígitos OU 000.000.000-00
    "CPF": r"[0-9]{11}|[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}",

    # 11 dígitos OU (00)00000-0000
    "Telefone": r"[0-9]{11}|\([0-9]{2}\)[0-9]{5}-[0-9]{4}",

    # usuário (mín. 2 caracteres) @ domínio (mín. 2 caracteres, sem '..') . 3 letras [.país opcional]
    "E-mail": (
        r"[\w.-]{2,}"                                           # usuário
        r"@(?=[a-zA-Z0-9_.-]{2,}\.[a-z]{3})"                    # garante domínio >= 2 chars
        r"[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)*"                  # domínio sem pontos consecutivos
        r"\.[a-z]{3}"                                           # registro (.com, .org, .net ...)
        r"(?:\.(?:br|ao|pt|es|de|uk))?"                         # país (opcional para EUA)
    ),
}

# 2. FUNÇÕES
def validar_campo(nome_campo, valor):
    """Retorna True se o valor casa por inteiro com o padrão do campo."""
    ok = re.fullmatch(PADROES[nome_campo], valor.strip(), re.ASCII) is not None
    print(f"  [{'VÁLIDO' if ok else 'INVÁLIDO':8}] {nome_campo}: '{valor}'")
    return ok


def validar_formulario(dados):
    """Valida todos os campos do dicionário e informa o resultado final."""
    print("-" * 50)
    resultados = [validar_campo(campo, valor) for campo, valor in dados.items()]
    print("  >> APROVADO" if all(resultados) else "  >> REJEITADO")


def extrair_emails(texto):
    """Encontra todos os e-mails válidos dentro de um texto livre."""
    padrao = r"(?<![\w.-])" + PADROES["E-mail"] + r"(?![\w-]|\.[a-zA-Z0-9_-])"
    emails = re.findall(padrao, texto, re.ASCII)
    print("-" * 50)
    print(f"E-mails encontrados: {len(emails)}")
    for i, email in enumerate(emails, start=1):
        print(f"  {i}. {email}")


def perguntar_sim_nao(mensagem):
    """Solicita 's' ou 'n' ao usuário, repetindo enquanto a entrada for inválida."""
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ("s", "n"):
            return resposta == "s"
        print("Valor inválido! Digite 's' para sim ou 'n' para não.")


def modo_interativo():
    """Permite ao usuário preencher e validar formulários em loop."""
    print("\n MODO INTERATIVO ")
    while True:
        dados = {
            "Nome": input("Nome (até 50 letras e espaços): "),
            "CPF": input("CPF (11 dígitos ou 000.000.000-00): "),
            "Telefone": input("Telefone (11 dígitos ou (00)00000-0000): "),
            "E-mail": input("E-mail: "),
        }
        validar_formulario(dados)

        if not perguntar_sim_nao("\nDeseja testar outro formulário? (s/n): "):
            print("Saindo do modo interativo...")
            return
        print()


def modo_extracao_interativa():
    """Permite ao usuário colar/digitar um texto para extrair e-mails válidos."""
    print("\n EXTRAÇÃO DE E-MAILS ")
    while True:
        print("Digite ou cole o texto abaixo. Para finalizar, digite 'FIM' em uma nova linha:")
        linhas = []
        while True:
            linha = input()
            if linha.strip().upper() == "FIM":
                break
            linhas.append(linha)

        extrair_emails("\n".join(linhas))

        if not perguntar_sim_nao("\nDeseja extrair e-mails de outro texto? (s/n): "):
            print("Voltando ao menu principal...")
            return
        print()


def executar_testes_padroes():
    """Executa a bateria de testes padrões (casos válidos, inválidos e extração)."""
    print("\n TESTE 1: formulário válido (com máscara)")
    validar_formulario({
        "Nome": "Mariana Ribeiro da Costa",
        "CPF": "123.456.789-00",
        "Telefone": "(11)98765-4321",
        "E-mail": "mariana_costa@instituto-pesquisa.org.br",
    })

    print("\n TESTE 2: formulário válido (sem máscara) ")
    validar_formulario({
        "Nome": "Lucas Silva",
        "CPF": "12345678900",
        "Telefone": "21998877665",
        "E-mail": "lucas.dev@platform.com",
    })

    print("\n TESTE 3: formulário inválido ")
    validar_formulario({
        "Nome": "Nome com número 123!",
        "CPF": "123.456.789-0",
        "Telefone": "(11)9876-4321",
        "E-mail": "x@site.com",
    })

    print("\n TESTE 4: extração de e-mails de um texto ")
    texto = """
    Prezado usuário,

    Aqui estão os contatos do nosso time de suporte:

    - alice.souza@gmail.com

    - suporte_23@empresa-tech.com

    - joao99@dominio123.org

    - erro.email@gmail..com

    Por favor, envie suas dúvidas para qualquer um dos e-mails válidos acima.

    Atenciosamente,

    Equipe de Atendimento
    """
    extrair_emails(texto)


# 3. EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    try:
        while True:
            escolha = input(
                "\nEscolha uma opção:\n"
                "  1 - Preencher formulário\n"
                "  2 - Visualizar testes padrões\n"
                "  3 - Extrair e-mails de um texto\n"
                "  0 - Finalizar\n"
                "Escolha: "
            ).strip()

            if escolha == "1":
                modo_interativo()
            elif escolha == "2":
                executar_testes_padroes()
            elif escolha == "3":
                modo_extracao_interativa()
            elif escolha == "0":
                print("Programa finalizado.")
                break
            else:
                print("Valor inválido! Digite 1, 2, 3 ou 0.")
    except (EOFError, KeyboardInterrupt):
        print("\nPrograma finalizado.")
