from framework.templator import render
from components.models import Engine

site = Engine()


class Index:
    def __call__(self, request):
        print(request)
        return "200 OK", render('index.html', object_list=site.categories)


class About:
    def __call__(self, request):
        if len(request) > 0 and 'data' in request[0].keys():
            print(request[0]['data'])
        return "200 OK", render('about.html')


class Login:
    def __call__(self, request):
        return "200 OK", "login"


class Register:
    def __call__(self, request):
        return "200 OK", "register"


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE not found'


class CoursesList:
    def __call__(self, request):
        try:
            category = site.find_category_by_id(int(request['request_params']['id']))
            return "200 OK", render("courses_list.html", objects_list=category.courses, name=category.name,
                                    id=category.id)

        except KeyError:
            return "200 OK", "No courses have been added yet"
