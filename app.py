from dbmanager import Dbmanager

class App:
    def __init__(self):
        self.db = Dbmanager()

    def initApp(self):
        msg = '1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış için(Q)'
        while True:
            print(msg)
            islem = input('Seçim: ')

            if islem == '1':
                self.displayStudents()
            elif islem == '2':
                pass
            elif islem == '3':
                pass
            elif islem == '4':
                pass
            elif islem == '5':
                pass
            elif islem == '6':
                pass
            elif islem == 'Q' or 'q':
                break
            else:
                print('Yanlış seçim')

    def displayStudents(self):
        classes = self.db.getClasses()
        for i in classes:
            print(f'{i.id}:{i.name}')
        classid = input('Hangi sınıf')
        students = self.db.GetStudentsByClassId(classid)
        print('Öğrenci Listesi')
        for index,i in enumerate(students):
            print(f'{index+1}-{i.name} {i.surname}')



app = App()
app.initApp()              