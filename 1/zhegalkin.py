def zhegalkin_reduce(tbl):
    n = len(tbl[0]) - 1
    tbl = [row[:] for row in tbl]
    for j in range(len(tbl)):
        for i in range(j):
            if (i & j) == i:
                tbl[j][-1] = (tbl[j][-1] + tbl[i][-1]) % 2
    return [row for row in tbl if row[-1] == 1]


def generate_vars(n): return [chr(ord('a') + i) for i in range(n)]


def print_polynom(zhegalkin_tbl):
    # vars = ['a', 'b', 'c', 'd']
    vars = generate_vars(n)
    poly = []
    for row in zhegalkin_tbl:
        mono = [vars[j] for j in range(len(row) - 1) if row[j]]
        if mono:
            poly.append("".join(mono))
        else:
            poly.append("1")

    print(" ⊕ ".join(poly))


if __name__ == "__main__":
    n = int(input())
    tbl = [list(map(int, input().split())) for _ in range(1 << n)]
    zhegalkin_tbl = zhegalkin_reduce(tbl)
    print_polynom(zhegalkin_tbl)
# Good job
# Полином Жегалкина:
# 1 ⊕ z ⊕ y ⊕ y*z ⊕ x*y
