import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class Dbmanager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def GetStudentById(self, id):
        sql = 'Select * From student where id = %s'
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            # print(obj)
            return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6])
        except mysql.connector.Error as err:
            print('Error: ', err)      

    def GetStudentsByClassId(self, classid):
        sql = 'Select * From student where classid = %s'
        value = (classid,)
        self.cursor.execute(sql, value)
        liste = []
        try:
            obj = self.cursor.fetchall()
            # print(obj)
            for i in obj:
                liste.append(Student(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
            return liste
        except mysql.connector.Error as err:
            print('Error: ', err)

    def AddStudent(self, student: Student):
        sql = 'INSERT INTO Student(StudentNumber, Name, Surname, Birthdate, Gender, Classid) VALUES (%s, %s, %s, %s, %s, %s)'
        value = (student.studentnumber, student.name, student.surname, student.birthdate, student.gender, student.classid)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('Hata: ', err)    

    def EditStudent(self, student: Student):
        sql = 'update student set studentnumber = %s, name = %s, surname = %s, birthdate = %s, gender = %s, classid = %s where id = %s'
        value = (student.studentnumber, student.name, student.surname, student.birthdate, student.gender, student.classid, student.id)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('Hata: ', err)         

    def AddTeacher(self, teacher: Teacher):
        pass

    def EditTeacher(self, teacher: Teacher):
        pass

    def getClasses(self):
        sql = 'select * from class'
        self.cursor.execute(sql)
        liste = []
        try:
            obj = self.cursor.fetchall()
            # print(obj)
            for i in obj:
                liste.append(Class(i[0], i[1], i[2]))
            return liste
        except mysql.connector.Error as err:
            print('Error: ', err)
    
    def __delattr__(self):
        self.connection.close()
        print('Db kapandı.')




# db = Dbmanager()
# clas = db.getClasses()
# print(clas[0].name)

# Student = db.GetStudentById(2)

# Student.name = 'Muhammed'
# Student.surname = 'NAS'
# Student.studentnumber = '0229'
# db.AddStudent(Student)

# std = Student(None, 297, 'Abdi', 'NAS', None, 'E', 1 )
# db.AddStudent(std)

# Student = db.GetStudentById(2)

# Student.name = 'Mustafa'
# Student.surname = 'NAS'
# Student.studentnumber = '0197'

# db.EditStudent(Student)

