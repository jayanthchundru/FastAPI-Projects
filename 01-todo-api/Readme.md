# Project 1 — Todo API

In-memory CRUD API built with FastAPI.

## Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/` | Health check |
| `POST` | `/todos` | Create todos (bulk) |
| `GET` | `/todos` | List all todos |
| `GET` | `/todos/{todo_id}` | Get one todo |
| `PUT` | `/todos/{todo_id}` | Replace a todo |
| `DELETE` | `/todos/{todo_id}` | Delete a todo |

Interactive docs at `/docs`.

## Run it

```bash
uv run uvicorn main:app --reload --port 8001
```

## Concepts covered

- Route decorators and HTTP methods
- Pydantic models for validation and response shaping
- Path parameters with type coercion
- HTTP status codes (201, 204, 404)
- Error handling via `HTTPException`
- Auto-generated OpenAPI / Swagger UI

## Key design choices

- **UUIDs over client-supplied IDs** — server generates them, no conflict checks needed.
- **Separate `TodoCreate` and `Todo` models** — input shape vs stored shape kept distinct.
- **Bulk create by default** — `POST /todos` takes a list; single create is a list of one.

## Known limitations

In-memory storage, no auth, no tests, no pagination — all addressed in later projects.
