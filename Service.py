from Models.StudenModel import Student, db

class Service:
    
    def create(self, data: dict):
        new_person = Student(
            first_name = data['first_name'],
            second_name = data['second_name'],
            last_name = data['last_name'],
            birthday = data['birthday'],
            course = data['course']
        )
        db.session.add(new_person)
        db.session.commit()
        return new_person.id

    def get(self):
        students = db.session.query(
            Student.first_name, Student.second_name,
            Student.last_name, Student.birthday, Student.course
        )
        srudents_return = []
        for student in students:
            srudents_return.append({
                'first_name': student.first_name,
                'second_name': student.second_name,
                'last_name': student.last_name,
                'birthday': student.birthday,
                'course': student.course
            })
        return srudents_return

    def update(self, id: int, data: dict):
        student = Student.query.filter_by(id=id).first()
        data_update = {i: data[i] for i in data if data[i]}
        student.query.filter_by(id=id).update(data_update)
        db.session.commit()

    def delete(self, id: int):
        Student.query.filter_by(id=id).delete()
        db.session.commit()