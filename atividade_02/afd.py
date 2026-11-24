# Função de Transição Estendida de um AFD

# --- Definição formal do AFD: M = (Sigma, Q, delta, q0, F) ---
ESTADOS = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'}
ALFABETO = {'a', 'b'}
ESTADO_INICIAL = 'q0'
ESTADOS_FINAIS = {'q4', 'q5', 'q6', 'q7'}

# delta: Q x Sigma -> Q
DELTA = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q2', 'b': 'q3'},
    'q2': {'a': 'q4', 'b': 'q5'},
    'q3': {'a': 'q6', 'b': 'q7'},
    'q4': {'a': 'q4', 'b': 'q5'},
    'q5': {'a': 'q6', 'b': 'q7'},
    'q6': {'a': 'q2', 'b': 'q3'},
    'q7': {'a': 'q1', 'b': 'q0'},
}


def delta_estendida(q: str, w: str) -> str:
    """
    delta_chapeu(q, w), definida por indução sobre |w|.
      Base:  delta_chapeu(q, "") = q
      Passo: delta_chapeu(q, xa) = delta(delta_chapeu(q, x), a)
    """
    if q not in ESTADOS:
        raise ValueError(f"Estado inválido '{q}'.")

    # Base da indução
    if w == "":
        return q

    # Passo indutivo: w = x a
    x, a = w[:-1], w[-1]
    if a not in ALFABETO:
        raise ValueError(f"Símbolo inválido '{a}'. Alfabeto: {sorted(ALFABETO)}.")
    return DELTA[delta_estendida(q, x)][a]


def rastro(q: str, w: str) -> list:
    """Sequência de estados percorrida ao ler w a partir de q."""
    caminho = [q]
    for i in range(1, len(w) + 1):
        caminho.append(delta_estendida(q, w[:i]))
    return caminho


def imprimir(w: str) -> None:
    est = delta_estendida(ESTADO_INICIAL, w)
    status = "ACEITA" if est in ESTADOS_FINAIS else "REJEITADA"
    print(f"{(w or '(vazia)'):<12} | {est:<6} | {status:<10} | "
          f"{' -> '.join(rastro(ESTADO_INICIAL, w))}")


def testes() -> None:
    esperado = {
        "": 'q0', "a": 'q1', "b": 'q0', "aa": 'q2', "ab": 'q3',
        "aaa": 'q4', "aab": 'q5', "aba": 'q6', "abb": 'q7',
        "baab": 'q5', "bbb": 'q0', "aaaa": 'q4',
    }
    print(f"{'Palavra':<12} | {'Estado':<6} | {'Resultado':<10} | Caminho")
    print("-" * 70)
    for w, est in esperado.items():
        assert delta_estendida(ESTADO_INICIAL, w) == est, w
        imprimir(w)
    print("\nTodos os testes passaram.\n")


def main() -> None:
    testes()
    print("Palavra para testar (Enter ou \"\" = palavra vazia; para encerrar, digite 'fim'):")
    while True:
        try:
            w = input("palavra: ").strip()
        except EOFError:
            break
        if w.lower() == "fim":
            break
        if w == '""':
            w = ""
        try:
            imprimir(w)
        except ValueError as e:
            print(e)
        print()


if __name__ == '__main__':
    main()
