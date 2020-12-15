from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import *

def test_multi_bracket_validation_1():
    actual= multi_bracket_validation('(hadi)')
    expected= True
    assert actual==expected



def test_multi_bracket_validation_2():
    actual= multi_bracket_validation(f'{{}}')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_3():
    actual= multi_bracket_validation(f'{{}}(){{}}')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_4():
    actual= multi_bracket_validation('()[[Extra Characters]]')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_5():
    actual= multi_bracket_validation(f'(){{}}[[]]')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_6():
    actual= multi_bracket_validation(f'{{}}{{Code}}[Fellows](())')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_7():
    actual= multi_bracket_validation(f'[({{}}]')
    expected= False
    assert actual==expected

def test_multi_bracket_validation_8():
    actual= multi_bracket_validation('(](')
    expected= False
    assert actual==expected

