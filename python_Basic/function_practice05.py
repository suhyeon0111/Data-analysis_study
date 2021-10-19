from collections import namedtuple
  # tuple의 형태로 구조체를 저장하는 방법


Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p)  # Point(x=11, y=22)
print(p.x, p.y, end=" ")  # 11 22
print()
print(p[0] + p[1])  # 33


from collections import Counter

c = Counter(a = 4, b = 2, c = 0, d = -2)    
d = Counter(a = 1, b = 2, c = 3, d = 4) 
c.subtract(d)

print(c | d)