from Ex1 import TodoList

def test_add_task():
    todo = TodoList()
    todo.add_task('Aprender Python')
    assert 'Aprender Python' in todo.tasks

def test_remove_task():
    todo = TodoList()
    todo.add_task('Aprender Python')
    todo.remove_task('Aprender Python')
    assert 'Aprender Python' not in todo.tasks

def test_show_tasks(capsys):
    todo = TodoList()
    todo.add_task('Aprender Python')
    todo.show_tasks()
    captured = capsys.readouterr()
    assert 'Aprender Python' in captured.out

def test_clear_tasks():
    todo = TodoList()
    todo.add_task('Aprender Python')
    todo.clear_tasks()
    assert not todo.tasks