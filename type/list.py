'''
.append() 리스트 마지막에 삽입됨
.insert(위치, 객체) 특정 위치 삽입
.index(객체) 객체 위치 확인
.pop() 마지막 객체 삭제
.sort() 정렬
.reverse() 역으로 뒤집기
.extend() 리스트 합치기
'''
list=['수학','과학','영어']
# print(list)
# list.append('국어')
# print(list)
# list.insert(1,'체육')
# print(list)
# print(list.pop())
# print(list)
# list.append('수학')
# print(list)
# print(list.count('수학'))
list2=[1,5,3,4,15,2]
list2.reverse()
print(list2)
list2.sort()
print(list2)
list.extend(list2)
print(list)
