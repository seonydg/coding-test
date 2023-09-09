from collections import deque

def getTF(bk):
    stack = []
    for i in bk:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False

    return True

def solution(s):
    dQ = deque()
    dQ.append(s) # 'dQ = deque()'하면 괄호 하나하나가 리스트에 원소로 담긴다.
    result = set() #             괄호 전체가 하나의 문자로 담겨야 한다.
    visited = set()
    while dQ:
        for i in range(len(dQ)):
            bracket = dQ.popleft()
            if getTF(bracket):
                print('bracket:', bracket)
                result.add(bracket)
                continue # 현재의 큐 레벨에서만 반복문 실행
            for j in range(len(bracket)):
                nextBk = bracket[:j] + bracket[j + 1:]
                if nextBk not in visited:
                    dQ.append(nextBk)
                    visited.add(bracket)
        if len(result) != 0:
            break

    return len(result)


if __name__ == '__main__':
    s = input()
    print(solution(s))

# 입력예제
# ()(()()
# 출력예제
# 2