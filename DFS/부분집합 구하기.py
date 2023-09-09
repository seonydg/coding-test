def DFS(v):
    if v > n:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end =' ')
        print()
    else:
        ch[v] = 1
        DFS(v + 1)
        ch[v] = 0
        DFS(v + 1)


if __name__ == '__main__':
    n = int(input())
    ch = [0] * (n + 1)
    DFS(1)

# ▣ 입력예제 1
# 3
# ▣ 출력예제 1
# 1 2 3
# 1 2
# 1 3
# 1
# 2 3
# 2
# 3

# ----------------------------
# arr = []
# def DFS(v):
#     if v > 3:
#         if len(arr) > 0:
#             print(arr)
#     else:
#         arr.append(v)
#         DFS(v + 1)
#         arr.remove(v)
#         DFS(v + 1)
# DFS(1)