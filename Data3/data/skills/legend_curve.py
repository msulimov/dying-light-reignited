from math import e

c = 0
L = 510000
x0 = 42.0
k = -0.021

def curve(i: int) -> int:
    return int(c + L/(1 + pow(e, (k*(i-x0)))))


for i in range(1, 251):
    print(f"<level id=\"{i}\" type=\"Legend\">"
          f"<prop n=\"ExpToNextLevelLegend\" v=\"{curve(i)}\"/></level>")

input() # let them copy level data
