import pytest
import nbformat
from reprexpy.engine import _get_statement_chunks
from reprexpy.engine import _run_nb


def read_ex_fi(file):
    with open(file) as fi:
        return fi.read()


def test_statement_parser():
    code_str = read_ex_fi("../examples/basic-example.py")
    s_chunks = _get_statement_chunks(code_str)
    assert len(s_chunks) == 14


# todo: refactor this so _get_statement_chunks isn't tested twice
def test_nb_exe():
    code_str = read_ex_fi("../examples/basic-example.py")
    s_chunks = _get_statement_chunks(code_str)
    out = _run_nb(s_chunks, "python3")
    assert isinstance(out, type(nbformat.v4.new_notebook()))
