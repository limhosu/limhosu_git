class Person:
    def greeting(self):
        print('good moning')

class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 임재환입니다.')

james=Student()
james.greeting()
