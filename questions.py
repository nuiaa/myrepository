class Question():
    #sorular kategorileşir
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    #cevabı kontrol eden fonksiyon
    def checkAnswer(self,answer):
        return self.answer==answer

class quiz():
    #quiz(questions) listedeki soruları düzenleyen init
    def __init__(self,questions):
        self.questions=questions #question argumanı özellik aldı
        self.questionsIndex=0 #kaçıncı sorudan başlayacağımızı belirtiyor
        self.score=0 #doğru cevap sayısı başlatılıyor

    #question=quiz(liste).getquestions() olarak objeleştirildi 
    #soruların içinden kaçıncı sorudan başlanacağını belirler
    #self daha sonradan tanımlanacak quiz sınıfının yerine kullanıldı
    def getquestions(self):
        return self.questions[self.questionsIndex]
    
    def displayquestions(self):
        question=self.getquestions()
        print(f"soru {self.questionsIndex+1}:{question.text}")
        for i in question.choices:
            print("-"+i)

        answer=input("cevap: ")
        self.guess(answer)
        self.loadQuestion()
    def guess(self,answer):
        question=self.getquestions()

        if question.checkAnswer(answer):
            self.score+=1
        self.questionsIndex+=1
        
    def loadQuestion(self):
        if len(self.questions) == self.questionsIndex:
            self.showScore()
        else: 
            self.displayProgress()
            self.displayquestions()
    
    def showScore(self):
        print("score: ",self.score)
    
    def displayProgress(self):
        totalQuestion=len(self.questions)
        questionNumber=self.questionsIndex + 1

        if questionNumber>totalQuestion:
            print("quiz bitti")
        else:
            print(f"question {questionNumber} of {totalQuestion}".center(100,"*"))


q1=Question("en iyi programlama dili hangisi",["c#","java","python"],"python")
q2=Question("en popüler programlama dili hangisi",["java","c#","python"],"python")
q3=Question("en çok kazandiran programlama dili hangisi",["c#","python","java"],"python")

questions=[q1,q2,q3]
#objeleştirme
quiz = quiz(questions)

quiz.loadQuestion()