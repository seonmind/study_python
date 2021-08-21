'''
중복 안되고 순서 없음
list를 set화 시키는 것 가능
합집합 교집합 가능
intersection &
union |
defference -
add 로 객체 추가
remove 로 객체 삭제

'''
set={1,3,3,4,5}
set2={2,3,4,4}
print(set.intersection(set2))
print(set.union(set2))
print(set.difference(set2))
set.add(1000)
print(set)
set.remove(1000)
print(set)