# test_find_module.py
# we test a script that does not return any value but does print (ie. STDOUT)
# its testing limitations and complexity
# are an indicator that the target script is is not best practice.    

def test_find_module(capsys):
    from .. src import find_module as fm
    module_name = "pyodbc"
    fm.main(module_name)
    captured = capsys.readouterr()
    assert captured.out.strip() == f"pass - module exists: {module_name}"
