from typing import List

class Todo:
    _id_increment = 1

    def __init__(self,userId : int, taskDescription : str, dueDate:int,  tags : List[str], is_completed=False):
        self.id = Todo._id_increment
        Todo._id_increment +=1
        self.userId = userId
        self.taskDescription = taskDescription
        self.tags = tags
        self.dueDate = dueDate
        self.is_completed = is_completed
    

class TodoList:

    def __init__(self):
        Todo._id_increment = 1
        self.todos : List[Todo] = []
        
    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:

        task = Todo(userId=userId, taskDescription=taskDescription,dueDate=dueDate, tags=tags, is_completed=False)

        self.todos.append(task)

        return task.id
        

    def getAllTasks(self, userId: int) -> List[str]:

        user_tasks = [task for task in self.todos if task.userId == userId and not task.is_completed]

        user_tasks = sorted(user_tasks, key=lambda task:task.dueDate)

        return [task.taskDescription for task in user_tasks]
        

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        
        tagged_tasks = [task for task in self.todos if task.userId == userId and not task.is_completed and tag in task.tags]

        tagged_tasks = sorted(tagged_tasks, key=lambda task:task.dueDate)

        return [task.taskDescription for task in tagged_tasks]

    def completeTask(self, userId: int, taskId: int) -> None:
        for task in self.todos:
            if task.userId == userId and task.id == taskId and not task.is_completed:
                task.is_completed = True
                return  


if __name__ == '__main__':
    todo = TodoList()
    print(todo.addTask(1, "Task1",50 ,[]))
    print(todo.addTask(1, "Task2", 100, ["P1"]))
    print(todo.getAllTasks(1))
    print(todo.addTask(1, "Task3", 30, ["P1"]))
    print(todo.getTasksForTag(1, "P1"))