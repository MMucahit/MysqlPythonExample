class Student:
    def __init__(self, id, studentnumber, name, surname, birthdate, gender, classid):
        if id  is None:
            self.id = 0
        else:
            self.id = id
        self.studentnumber = studentnumber
        if len(name) > 45:
            raise Exception('name için maksimum 45 karakter girmelisiniz.')
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.classid = classid