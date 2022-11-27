# test_find_module.py
# we test an immature script
# its testing limitations and complexity
# are a sign of the testing target script's immaturity    

def test_find_module(capsys):
    from .. src import find_module as fm
    captured = capsys.readouterr()
    assert captured.out.strip() == "module exists"
