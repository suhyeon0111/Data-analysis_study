colors = ['red', 'yellow', 'blue', 'pink']
result = ''
for s in colors:
    result += s


print(result)   

# 간단하게 코딩

result2 = ''.join(colors)   
print(result2)

# 문자열의 분리
items = 'zero one two three'.split()  # 공백을 기준으로 
print(items)

example = 'python,jquery,javascript'
print(example.split(","))

a,b,c = example.split(",")
print(a,b,c)

# 문자열의 결합 join
colors2 = ['red', 'blue', 'yellow', 'green']
result3 = ''.join(colors)
print(result3)
result3 = '-'.join(colors)
print(result3)

# 리스트 컴프리헨션 다루기
result4 = [i for i in range(10)]
print(result4)   
# 필터링
result5 = [i for i in range(10) if i % 2 == 0]
print(result5)

result6 = [i if i % 2 == 0 else 10 for i in range(10)]
print(result6)

# 중첩 반복문
word_1 = "hello"    
word_2 = "world"
result7 = [i + j for i in word_1 for j in word_2]
print(result7)

a = "1234"
b = "5678"
result8 = [i + j for i in a for j in b]
print(result8)

case_1 = ["a", "b", "c"]
case_2 = ["d", "e", "a"]

result9 = [i + j for i in case_1 for j in case_2 if not(i == j)]
print(result9)

# 이차원 리스트
words = 'the quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words] 
print(stuff)

result01 = [[i +j for i in case_1] for j in case_2]
print(result01)