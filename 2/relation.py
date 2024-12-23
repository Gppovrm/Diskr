def is_reflexive(rel, set_a):
    reflexive = {(a, a) for a in set_a}
    if reflexive <= rel:
        return "Рефлексивное"
    elif not any((a, a) in rel for a in set_a):
        return "Антирефлексивное"
    else:
        return "Нерефлексивное"


def is_transitive(rel):
    is_transitive = True
    is_antitransitive = True
    for (i, j) in rel:
        for (j2, k) in rel:
            if j == j2:
                if (i, k) not in rel:
                    is_transitive = False
                if (i, k) in rel and i != j:
                    is_antitransitive = False
    if is_transitive:
        return "Транзитивное"
    elif is_antitransitive:
        return "Антитранзитивное"
    else:
        return "Нетранзитивное"


def is_symmetric(rel):
    is_symmetric = True
    is_antisymmetric = True
    for (i, j) in rel:
        if (j, i) not in rel:
            is_symmetric = False
        if (j, i) in rel and i != j:
            is_antisymmetric = False
    if is_symmetric:
        return "Симметричное"
    elif is_antisymmetric:
        return "Антисимметричное"
    else:
        return "Несимметричное"


if __name__ == "__main__":
    n, m = map(int, input().split())
    # Создаем множество рёбер
    edges = set()
    vertices = set()
    for _ in range(n):
        u, v = map(int, input().split())
        edges.add((u, v))
        vertices.add(u)
        vertices.add(v)
    # Проверяем и Выводим результаты проверок
    print(f"{is_reflexive(edges, vertices)}\n{is_transitive(edges)}\n{is_symmetric(edges)}")
