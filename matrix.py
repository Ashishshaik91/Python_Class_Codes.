import numpy as np
from scipy.sparse import csr_matrix

is_on = True
while is_on:
    rows = int(input("No. of Rows: "))
    column = int(input("No. of Columns: "))
    mat = []
    for i in range(rows):
        a = map(int, input("Put the values: ").split(' '))
        b = list(a)
        if len(b) <= column:
            mat.append(b)
        else:
            print("Invalid number of columns")
            break

    print("\nTHE MATRIX:")
    for i in mat:
        print(*i)   # Put the value of list without commas and brackets!!
    # final = np.array(mat)
    # print(final)
    print("\n")
    sp = csr_matrix(mat)
    print(f"The Sparce Matrix is: ")
    print(sp)
    if input("Wanna practice again(Y/N): ").lower() == "n":
        is_on = False
# i1 = int(input("Choose Row: "))
# i2 = int(input("Choose Column: "))
# print(f"The Element at required position is: {mat[i1-1][i2-1]}")




