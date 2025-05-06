n = int(input())

n1 = int(n/2 + 0.5)

n2 = int(n1/2 + 0.5)


nReal = list(range(n1,1,-1))

nReal2 = list(range(n2,1,-1))


nCompostos = [x * y for x in nReal for y in nReal2]

nCompostos2 = [x for x in nCompostos if x <= n]

nCompostosreal = list(dict.fromkeys(nCompostos2))
nCompostosreal.sort(reverse=False)

print(nCompostosreal)

