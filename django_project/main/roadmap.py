from datetime import datetime, date

class Task:
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

    def add_task(self, task):
        assert type(task) is Task, 'Error: Items of list <tasks> should have type Task!'
        self.tasks.append(task)

    def set_task(self, new_task):
        assert type(new_task) is Task, 'Error: Items of list <tasks> should have type Task!'
        for task in self.tasks:
            if task.title == new_task.title:
                task.state = new_task.state
                task.estimate = new_task.estimate
                break
        else:
            return False
        return True

    def delete_task(self, title):
        assert type(title) is str, 'Error: Argument <title> should be a string!'
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                break
        else:
            return False
        return True
