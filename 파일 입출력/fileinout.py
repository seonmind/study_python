'''
변수에 open을 통해 파일을 불러옴
w를 새로쓰기
r은 읽기
a는 이어서 쓰기
반드시 파일을 닫아야 함
'''

# score_file=open("score.txt",'w',encoding='utf8')
# print("수학:100",file=score_file)
# print("영어:100",file=score_file)
# print("코딩:100",file=score_file)
# score_file.write("과학:100")
# score_file.close()

# score_file=open('score.txt','r',encoding='utf8')
# print(score_file.read())
# score_file.close()

# score_file=open('score.txt','r',encoding='utf8')
# while True:
#     line=score_file.readline()
#     print(line)
#     if not line:
#         break
# score_file.close()

score_file=open("score.txt",'r',encoding="utf8")
for line in score_file.readlines():
    print(line)
score_file.close()


