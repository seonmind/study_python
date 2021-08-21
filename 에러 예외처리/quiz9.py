chicken=10
waiting=1
class SoldoutError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self): 
        return self.msg
while(True):
    print(f"[남은 치킨 : {chicken}마리]")
    try:
        order=int(input("치킨을 몇마리 주문하시겠습니까?: "))
        if order>chicken:
            print("재료가 부족합니다")
        elif order<=0:
            raise ValueError
        else:
            chicken-=order
            print(f"[대기번호 {waiting}] {order}마리 주문이 완료 되었습니다\n[남은 치킨 : {chicken}]")
            waiting+=1
        if chicken==0:
            raise SoldoutError("재료가 소진되었습니다")
    except ValueError:
        print("잘못된 값을 입력하였습니다")
    except SoldoutError as err:
        print(err)    
        break
    
    


    