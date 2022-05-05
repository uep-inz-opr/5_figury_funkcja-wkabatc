from math import pi

def calc_area(fig):
    l = len(fig)
    if l == 1:
        return pi * fig[0]**2
    if l == 2:
        return fig[0] * fig[1]
    if l == 3:
        s = (fig[0] + fig[1] + fig[2]) / 2
        return (s * (s - fig[0]) * (s - fig[1]) * (s - fig[2])) ** 0.5
    if l >= 4:
        ret = 'Błąd: można podać maksymalnie 3 liczby'
        return 0

i = int(input())
#figures = []
sum = 0

for n in range(i):
    f = list(map(float, input().split()))
    sum = sum + calc_area(f)
    #print(calc_area(f))
    #figures.append(f)

print(format(sum, ".2f"))
#print(figures)