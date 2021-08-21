# customer="김성중"
# person="unkwon"
# while person!=customer:
#     print(f"{customer}님 커피가 준비 되었습니다")
#     person=input("손님, 성함이 어떻게 되세요?: ")
#     if person==customer:
#         print("맛있게 드세요")

absent=[1,4]
nobook=[7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in nobook:
        print("{}개새끼야! 교무실로 따라와! 수업끗".format(student))
        break
    print(f"{student}야, 책 읽어봐")