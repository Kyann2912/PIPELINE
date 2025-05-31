from app import addition

def test_addition():
    assert addition(2, 3) == 9
    assert addition(-1, 1) == 0


#.github/workflows/python-ci.yml – Pipeline CI avec GitHub Actions