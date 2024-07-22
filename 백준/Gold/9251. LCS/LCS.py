X = " " + input()
Y = " " + input()

cnt_lcs = [[0] * len(Y) for _ in range(len(X))]

for i in range(1, len(X)):
    for j in range(1, len(Y)):
        if X[i] == Y[j]:
            cnt_lcs[i][j] = cnt_lcs[i - 1][j - 1] + 1
        else:
            cnt_lcs[i][j] = max(cnt_lcs[i][j - 1], cnt_lcs[i - 1][j])

print(cnt_lcs[len(X) - 1][len(Y) - 1])