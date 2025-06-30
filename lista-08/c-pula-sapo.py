pulo, n = map(int, input().split())
canos_l = list(map(int, input().split()))

def pula_sapo(p: int, canos: list) -> str:
    for i in range(1, n):
        if canos[i-1]:
            if canos[i-1] > (canos[i] + p) or canos[i-1] < (canos[i] - p):
                return "GAME OVER"
    return "YOU WIN"

print(pula_sapo(pulo, canos_l))