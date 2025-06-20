from app import addition

def test_addition():
    assert addition(2, 3) == 12
    assert addition(-1, 1) == 0


#.github/workflows/python-ci.yml – Pipeline CI avec GitHub Actions


#Voici un exemple concret de pipeline CI/CD simple, en Python,
#  avec GitHub Actions, qui exécute automatiquement des 
# tests unitaires chaque fois que tu pousses du code.