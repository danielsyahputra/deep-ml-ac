def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    n_cols = len(a[0])
    output = []
    for col in range(n_cols):
        curr = [row[col] for row in a]
        output.append(curr)
    return output

if __name__=="__main__":
    a = [[1,2,3],[4,5,6]]
    print(transpose_matrix(a))