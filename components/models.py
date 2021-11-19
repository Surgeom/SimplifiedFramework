import quopri


class User:
    pass


class Teacher(User):
    pass


class Student(User):
    pass


class UserFactory:
    types = {
        'student': Student,
        'teacher': Teacher,
    }

    @classmethod
    def create(cls, type_):
        return cls.types[type_]()


class Course:
    def __init__(self, name, category):
        self.name = name,
        self.category = category,
        self.category.courses.append(self)


class InterectiveCourse(Course):
    pass


class RecordCourse(Course):
    pass


class CourseFactory:
    types = {
        'intcourse': InterectiveCourse,
        'reccourse': RecordCourse,
    }

    @classmethod
    def create(cls, type_):
        return cls.types[type_]()


class Category:
    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result


class Engine:
    def __init__(self):
        self.teachers = [],
        self.students = [],
        self.courses = [],
        self.categories = []

    @staticmethod
    def create_user(type_):
        return UserFactory.create(type_)

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    def find_category_by_id(self, id):
        for item in self.categories:
            if item.id == id:
                return item
        raise Exception(f"нет категории с id = {id}")

    @staticmethod
    def create_course(type_, name, category):
        return CourseFactory.create(type_, name, category)

    def get_course(self, name):
        for item in self.courses:
            if item.name == name:
                return item
            return None

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace("%", "=").replace("+", " "), "utf-8")
        val_decode_str = quopri.decodestring(val_b).decode("utf-8")
        return val_decode_str
