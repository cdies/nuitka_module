import ast
from pathlib import Path

def pretty_print(text):
    print(f'{text[:160]} \n...\n {text[-100:]}')

so_file_module = Path('so/bin_module.cpython-310-x86_64-linux-gnu.so').read_bytes()
so_file_module = str(so_file_module)
so_dump = ast.dump(ast.parse(so_file_module), indent=2)

py_file_module = Path('py/bin_module.py').read_text()
py_dump = ast.dump(ast.parse(py_file_module), indent=2)

pretty_print(so_dump)
pretty_print(py_dump)