from .task import Task

class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = Task
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        amount = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                amount += 1
        return f"Cleared {amount} tasks."

    def view_section(self):
        string = f"Section {self.name}:\n"
        for task in self.tasks:
            string += task.details() + "\n"
        return string.strip()
