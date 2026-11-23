# Atividade 1 — Validador de Formulário e Extrator de E-mails

Implementação em Python utilizando expressões regulares com a biblioteca padrão `re`, localizada em [`validador_regex.py`](validador_regex.py).

---

## O que foi feito

O programa valida os quatro campos exigidos pela atividade e também varre textos livres para extrair apenas os e-mails válidos:

- **Nome:** aceita apenas letras (`a-z`, `A-Z`) e espaços, de 1 até 50 caracteres.
- **CPF:** aceita 11 dígitos numéricos contínuos (`00000000000`) ou o formato com máscara (`000.000.000-00`).
- **Telefone:** aceita 11 dígitos numéricos contínuos (`00000000000`) ou o formato `(00)00000-0000`.
- **E-mail:**
  - Usuário e domínio com no mínimo 2 caracteres (`a-z`, `A-Z`, `0-9`, `_`, `.`, `-`), sem permitir pontos consecutivos (`..`).
  - Tipo de registro obrigatório com 3 letras minúsculas (ex.: `.com`, `.org`, `.net`, `.edu`, `.gov`).
  - Código do país opcional para contemplar domínios dos EUA (sem sufixo) ou os códigos permitidos: `br`, `ao`, `pt`, `es`, `de` e `uk`.

---

## Como funciona

Ao executar o script, um menu interativo é exibido com as seguintes opções:

1. **Preencher formulário (`1`):** permite digitar Nome, CPF, Telefone e E-mail e informa quais campos são válidos/inválidos e se o formulário foi **APROVADO** ou **REJEITADO**, com opção de testar novos formulários em loop (`s`/`n`).
2. **Visualizar testes padrões (`2`):** executa casos prontos para demonstração:
   - Formulário válido com máscara;
   - Formulário válido sem máscara (incluindo e-mail dos EUA);
   - Formulário inválido com falhas propositais em cada campo;
   - Extração de e-mails válidos no texto da atividade (ignorando `erro.email@gmail..com`).
3. **Extrair e-mails de um texto (`3`):** permite digitar ou colar um texto com várias linhas (finalizando com `FIM` em uma nova linha) e lista todos os e-mails válidos encontrados, ignorando os inválidos e lidando corretamente com pontuação no fim das frases.
4. **Finalizar (`0`):** encerra o programa.

---

## Como executar

No terminal, dentro desta pasta (`atividade_01`):

```bash
python validador_regex.py
```
