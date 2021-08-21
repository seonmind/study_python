# try:
#     num=[]
#     num.append(int(input("첫번째 숫자를 입력하시오: ")))
#     num.append(int(input("두번째 숫자를 입력하시오: ")))
#     num.append(num[0]/num[1])
#     print(f"{num[0]}나누기 {num[1]}는 {num[2]}")
# except ValueError as err:
#     print(err)
# except Exception as err:
#     print(err)

'''
raise 를 통해 error 상황이 아니더라도 에러 발생시키는 것 가능
class를 통해 Exection class를 상속받은 새로운 error class를 만들면 사용자 저으이 error 사용 가능
raise를 통해 사용자 정의 eroor 유발
finally는 에러발생 여부와 무관하게 무조건 실행되는 구문
'''
class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

print("한자리 숫자 계산기")
try:
    num=[]
    num.append(int(input("첫번째 숫자를 입력하시오: ")))
    num.append(int(input("두번째 숫자를 입력하시오: ")))
    num.append(num[0]/num[1])
    print(f"{num[0]}나누기 {num[1]}는 {num[2]}")
    if num[0]>=10 | num[1]>=10:
        raise BigNumberError('기모찌')
except BigNumberError as err:
    print(err)
except Exception as err:
    print(err)
finally:
    print("ㅋㅋ 감사링")