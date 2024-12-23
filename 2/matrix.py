def check_symmetry(matrix, vertices):
    is_symmetric = True
    is_antisymmetric = True

    for i in range(vertices):
        for j in range(vertices):
            if matrix[i][j] != matrix[j][i]:
                is_symmetric = False
            if i != j and matrix[i][j] == 1 and matrix[j][i] == 1:
                is_antisymmetric = False
            if matrix[i][i] != 0:
                is_antisymmetric = False

    if is_symmetric:
        return "Симметричное"
    elif is_antisymmetric:
        return "Антисимметричное"
    else:
        return "Несимметричное"


def check_reflexivity(matrix, vertices):
    has_one = False
    has_zero = False

    for i in range(vertices):
        if matrix[i][i] == 1:
            has_one = True
        elif matrix[i][i] == 0:
            has_zero = True

    if has_one and not has_zero:
        return "Рефлексивное"
    elif has_zero and not has_one:
        return "Антирефлексивное"
    else:
        return "Нерефлексивное"


def check_transitivity(matrix, vertices):
    is_transitive = True
    is_antitransitive = True

    for i in range(vertices):
        for j in range(vertices):
            if matrix[i][j] == 1:
                for k in range(vertices):
                    if matrix[j][k] == 1:
                        if matrix[i][k] != 1:
                            is_transitive = False
                        if matrix[i][k] == 1:
                            is_antitransitive = False
    if is_transitive:
        return "Транзитивное"
    elif is_antitransitive:
        return "Антитранзитивное"
    else:
        return "Нетранзитивное"


def create_adjacency_matrix(edges, vertices):
    matrix = [[0] * vertices for _ in range(vertices)]
    for edge in edges:
        matrix[edge[0]][edge[1]] = 1
    return matrix


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(n)]
    # USING create_adjacency_matrix НУМЕРАЦИЯ С 0 (ОТКУДА,КУДА )
    adj_matrix = create_adjacency_matrix(edges, m)
    print(f"{check_reflexivity(adj_matrix, m)}\n{check_transitivity(adj_matrix, m)}\n{check_symmetry(adj_matrix, m)}")


    # USING build_adjacency_matrix НУМЕРАЦИЯ С 1 (КУДА, ОТКУДА)
    # adjacency_matrix = build_adjacency_matrix(m, edges)
    # print("Матрица смежности:")
    # print_matrix(adjacency_matrix)
    # if is_symmetric(adjacency_matrix, m):
    #     symmetry_type = "Cимметричное"
    # elif is_antisymmetric(adjacency_matrix, m):
    #     symmetry_type = "Антисимметричное"
    # else:
    #     symmetry_type = "Несимметричное"
    # reflexivity_type = check_reflexivity(adjacency_matrix, m)
    # transitivity_type = check_transitivity(adjacency_matrix, m)
    # print(f"{reflexivity_type}")
    # print(f"{transitivity_type}")
    # print(f"{symmetry_type}")