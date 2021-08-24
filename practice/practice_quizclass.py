
class Word:
    def __init__(self,word,sample1,sample2,answer):
        self.word=word
        self.sample1=sample1
        self.sample2=sample2
        self.answer=answer
    def show_question(self):
        msg=(f"{self.word}의 뜻은?\n"
        f"1. {self.sample1}\n"
        f"2. {self.sample2}")
        print(msg)
    def check_answer(self,ans):
        if ans==self.answer:
            print("정답")
        else:
            print("오답")
word=Word("얼죽아","얼어죽어도 아메리카노","얼음 죽염 아이스",1)
word.show_question()
word.check_answer(int(input("=> ")))