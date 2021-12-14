from left_join import __version__
from left_join.left_join import left_join

def test_version():
    assert __version__ == '0.1.0'


def test_1() :
    first = {
            'fond': 'enamored',
            'wrath': 'anger',
            'diligent': 'employed',
            'outift': 'garb',
            'guide': 'usher',
        }

    secoend = {
            'fond': 'averse',
            'wrath': 'delight',
            'diligent': 'idle',
            'guide': 'follow',
            'flow': 'jam',
        }


    actual = left_join(first,secoend)
    expected =[ ['fond', 'enamored', 'averse'],
                ['wrath', 'anger', 'delight'],
                ['diligent', 'employed', 'idle'],
                ['outift', 'garb', None],
                ['guide', 'usher', 'follow']]
    assert expected == actual
def test_2() :
    first = {
            'fond': 'enamored',
            'wrath': 'anger',
            'diligent': 'employed',

        }

    secoend = {
            'fond': 'averse',
            'wrath': 'delight',
            'diligent': 'idle',

        }


    actual = left_join(first,secoend)
    expected =[ ['fond', 'enamored', 'averse'],
                ['wrath', 'anger', 'delight'],
                ['diligent', 'employed', 'idle'] ]

    assert expected == actual





def test_3() :
    first = {
            'fond': 'enamored',
        }

    secoend = {
            'fond': 'averse',
        }


    actual = left_join(first,secoend)
    expected =[ ['fond', 'enamored', 'averse'] ]

    assert expected == actual
