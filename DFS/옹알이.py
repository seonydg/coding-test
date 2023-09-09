import itertools as it
import time
def solution(babbling):
    words = ['aya', 'ye', 'woo', 'ma']
    n = len(words)
    per = []
    # word로 만들 수있는 모든 순열 만들기
    for i in range(1, n + 1):
        for j in it.permutations(words, i):
            per.append(j)
        print(per)
    # 만든 순열을 발음으로 이어붙이기
    answer = []
    for word in per:
        k = ''
        for j in word:
            k += j
        answer.append(k)
        print(answer)

    cnt = 0
    for i in babbling:
        if i in answer:
            cnt += 1
    print(cnt)

    return cnt

if __name__ == '__main__':
    startT = time.time()
    babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
    solution(babbling)
    endT = time.time()
    print(endT - startT)
