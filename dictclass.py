class DictClass(object):
    '''
    Create inheritable dicts with class syntax. This is very conveninent
    for writing dictionaries used in configurations because you can layer
    the configs and also class syntas is much more pleasing to type.


    >>> class Foo(DictClass):
    ...     foo = 'bar'
    ...     tar = 'zar'
    ...     bar = 'foo'
    >>> class Bar(Foo):
    ...     bar = 'bar' 
    ...     foo = 'foo'
    >>> class Zar(Bar):
    ...     foo = 'zar'
    >>> assert Zar.as_dict() == dict(foo='zar', bar='bar', tar='zar')
    '''
    @classmethod
    def as_dict(cls):

        def _items(d):
            return dict((k,v) for k,v in d.items() if not k.startswith('_'))

        d = {}
        for base in reversed(cls.mro()):
            d.update(_items(base.__dict__))
        d.update(_items(cls.__dict__))
        d.pop('as_dict', None)
        d.pop('mro', None)
        return d

import doctest
test = doctest.DocTestSuite()
