from datetime import datetime, timedelta, date
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from wsgiref.simple_server import make_server

class Task:
    def __init__(self, title, estimate):
        assert type(title) is str, 'Error: Argument <title> should be a string!'
        assert type(estimate) is date, 'Error: Argument <estimate> should be a datetime.date!'
        self.title = title
        self.estimate = estimate
        self.state = 'in_progress'

    def __init__(self, title, state, estimate):
        assert type(title) is str, 'Error: Argument <title> should be a string!'
        assert type(state) is str and (state == "ready" or state == "in_progress"), 'Error: Argument <state> shoud be string "ready" or "in_progress"'
        assert type(estimate) is date, 'Error: Argument <estimate> should be a datetime.date!'
        self.title = title
        self.estimate = estimate
        self.state = state

    @property
    def remaining(self):
        if self.state == 'in_progress':
            return self.estimate.__sub__(datetime.now().date())
        return 0

    @property
    def is_failed(self):
        return self.state == 'in_progress' and self.estimate < datetime.now().date()

    def ready(self):
        self.state = 'ready'

class Roadmap:
    def __init__(self, tasks = []):
        assert type(tasks) is list, 'Error: Argument <tasks> should be a list!'
        for item in tasks :
            assert type(item) is Task, 'Error: Items of list <tasks> should have type Task!'
        self.tasks = tasks

    @property
    def today(self):
        result = []
        for item in self.tasks :
            if item.estimate == datetime.now().date() :
                result.append(item)
        return result

    def filter(self, state):
        assert type(state) is str, 'State should be a string!'
        result = []
        for item in self.tasks:
            if item.state == state:
                result.append(item)
        return result

def get_dataset(filename):
    with open(filename, 'rt', encoding='utf-8') as input:
        package = load(input, Loader=Loader)
        dataset = package.get('dataset')
        if not isinstance(dataset, list):
            raise ValueError('wrong format')
        data = []
        for elem in dataset :
            data.append(Task(elem[0], elem[1], elem[2]))
        return data


def wsgi_application(environ, start_response):
    response_headers = [('Content-type', 'text/plain')]
    start_response('200 OK', response_headers)

    roadmap = Roadmap(get_dataset("dataset.yml"))
    critical_tasks = []
    for task in roadmap.filter("in_progress"):
        if task.remaining <= timedelta(days=3):
            critical_tasks.append((task.title + task.state + str(task.estimate)).encode('utf-8'))
    return critical_tasks

if __name__ == '__main__':
    server = make_server('127.0.0.1', 8080, wsgi_application)
    server.serve_forever()
