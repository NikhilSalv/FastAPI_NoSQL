def indivisual_serialiser(todo) -> dict:
    return {
        "id" : str(todo["_id"]),
        "name" : str(todo.get("name", "")),
        "description" : str(todo.get("description","")),
        "completed" : todo.get("completed", False)
    }


def list_serial(todos):
    return [indivisual_serialiser(todo) for todo in todos]