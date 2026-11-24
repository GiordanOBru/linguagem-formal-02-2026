# Atividade 2 — Função de Transição Estendida em AFD

Implementação em Python da função de transição estendida de um Autômato Finito Determinístico (AFD), baseada no grafo [`afd.png`](afd.png) e localizada em [`afd.py`](afd.py).

---

## O que foi feito

O programa define formalmente o AFD $M = (\Sigma, Q, \delta, q_0, F)$ com alfabeto `{a, b}`, estados `{q0, q1, q2, q3, q4, q5, q6, q7}`, estado inicial `q0` e estados finais `{q4, q5, q6, q7}`:

| Estado | `a` | `b` |
| :---: | :---: | :---: |
| `-> q0` | `q1` | `q0` |
| `q1` | `q2` | `q3` |
| `q2` | `q4` | `q5` |
| `q3` | `q6` | `q7` |
| `*q4` | `q4` | `q5` |
| `*q5` | `q6` | `q7` |
| `*q6` | `q2` | `q3` |
| `*q7` | `q1` | `q0` |

A partir dessa definição, foram implementadas as seguintes funções:

- **`delta_estendida(q, w)`:** implementa a função de transição estendida por indução sobre o tamanho da palavra `w`:
  - **Base:** para a palavra vazia `""`, retorna o próprio estado `q`.
  - **Passo indutivo:** separa `w = x + a`, resolve `delta_estendida(q, x)` recursivamente e aplica a transição `DELTA[estado][a]`.
  - Valida se o estado inicial e todos os símbolos da palavra pertencem ao alfabeto `{a, b}`.
- **`rastro(q, w)`:** registra a sequência completa de estados percorrida ao ler `w` a partir de `q`.
- **`imprimir(w)`:** exibe a palavra (ou `(vazia)`), o estado final, se foi `ACEITA` ou `REJEITADA` e o caminho percorrido.

---

## Como funciona

Ao executar o script:

1. **Testes automáticos (`testes()`):** executa 12 palavras de exemplo (`""`, `a`, `b`, `aa`, `ab`, `aaa`, `aab`, `aba`, `abb`, `baab`, `bbb`, `aaaa`), validando os estados esperados com `assert` e exibindo a tabela de resultados.
2. **Modo interativo:** após os testes, solicita palavras no prompt `palavra:`:
   - Pressionar `Enter` vazio ou digitar `""` testa a palavra vazia.
   - Qualquer palavra válida exibe o estado final, `ACEITA` ou `REJEITADA` e o caminho.
   - Digitar `sair` encerra o programa.

---

## Como executar

No terminal, dentro desta pasta (`atividade_02`):

```bash
python afd.py
```
