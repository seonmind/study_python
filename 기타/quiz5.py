from random import*
number=0
for customer in range(1,51):
    time=randrange(5,51)
    if 5<=time<=15:
        index="O"
        number+=1
    else:
        index=" "
    print(f"[{index}] {customer}번째 손님 (소요시간 : {time}분)")
print("총 탑승 승객 : {}분".format(number))