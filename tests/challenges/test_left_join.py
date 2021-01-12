from data_structures_and_algorithms.challenges.left_join.left_join import left_join

import pytest

def test_happy_path(h1,h2):
    actual = left_join(h1,h2)
    expect = [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['outift', 'garb', None], ['guide', 'usher', 'follow']]
    assert actual == expect

def test_second_hashmap_empty(h1):
    actual = left_join(h1,{})
    expect = [['fond', 'enamored', None], ['wrath', 'anger', None], ['diligent', 'employed', None], ['outift', 'garb', None], ['guide', 'usher', None]]
    assert actual == expect

def test_left_hashmap_empty(h2):
    actual = left_join({},h2)
    expect = 'Your left hashmap is empty'
    assert actual == expect


@pytest.fixture
def h1():
    h11 = {
        'fond': 'enamored',
        'wrath': 'anger',
        'diligent': 'employed',
        'outift': 'garb',
        'guide': 'usher',
    }
    return h11

@pytest.fixture
def h2():
    h22 = {
        'fond': 'averse',
        'wrath': 'delight',
        'diligent': 'idle',
        'guide': 'follow',
        'flow': 'jam',
    }
    return h22


