from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import UUID, uuid4


app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Todo API UP"}

class TodoCreate(BaseModel):
    title: str
    completed: bool = False
    

class Todo(TodoCreate):
    id : UUID

todos: dict[UUID, Todo] = {}

@app.post("/todo", status_code=201)
async def create_todo(todo: TodoCreate) -> Todo:
    todo = Todo(id=uuid4(), **todo.model_dump())
    todos[todo.id] = todo
    return todo

@app.post("/todos", status_code=201)
async def create_todo_list(new_todos: list[TodoCreate]) -> list[Todo]:
    created = []
    for incoming in new_todos:
        todo = Todo(id=uuid4(), **incoming.model_dump())
        todos[todo.id] = todo
        created.append(todo)
    return created

@app.get("/todos")
async def list_todos() -> list[Todo]:
    return list(todos.values())

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: UUID) -> Todo:
    if todo_id not in todos:
        raise HTTPException(status_code = 404, detail=f"Todo {todo_id} not found in the todo list")
    return todos[todo_id]

@app.put("/todo/{todo_id}")
async def update_todo(todo_id: UUID, todo: TodoCreate) -> Todo:
    if todo_id not in todos:
        raise HTTPException(status_code = 404, detail=f"Todo {todo_id} not found in the todo list")
    
    todo = Todo(id=todo_id, **todo.model_dump())
    todos[todo_id] = todo
    return todo
        

@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id: UUID) -> None:
    if todo_id not in todos:
        raise HTTPException(status_code = 404, detail=f"Todo {todo_id} not found in the todo list")
    del todos[todo_id]