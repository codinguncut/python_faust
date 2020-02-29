import warnings
warnings.simplefilter('ignore', category=PendingDeprecationWarning)
warnings.simplefilter('ignore')

from scraper.faust_msgpack import raw_msgpack


# FIXME: couldn't find a way to ignore PendingDeprecationWarning
'''
def test_msgpack():
    """ test that msgpack is storing unicode and bytes properly """
    mp = raw_msgpack()

    a = {
        'unicode': u'hello',
        'bytes': b'hello',
        'list': [1, 2, 3]
    }
    b = mp._loads(mp._dumps(a))
    assert type(b['unicode']) == str
    assert type(b['bytes']) == bytes
'''
