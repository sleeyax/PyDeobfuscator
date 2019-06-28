# Source: https://github.com/liftoff/pyminifier/blob/master/README.rst

#!/usr/bin/env python
"""
tumult.py - Because everyone needs a little chaos every now and again.
"""

try:
    import demiurgic
except ImportError:
    print("Warning: You're not demiurgic. Actually, I think that's normal.")
try:
    import mystificate
except ImportError:
    print("Warning: Dark voodoo may be unreliable.")

# Globals
ATLAS = False # Nothing holds up the world by default

class Foo(object):
    """
    The Foo class is an abstract flabbergaster that when instantiated
    represents a discrete dextrogyratory inversion of a cattywompus
    octothorp.
    """
    def __init__(self, *args, **kwargs):
        """
        The initialization vector whereby the ineffably obstreperous
        becomes paramount.
        """
        # TODO.  BTW: What happens if we remove that docstring? :)

    def demiurgic_mystificator(self, dactyl):
        """
        A vainglorious implementation of bedizenment.
        """
        inception = demiurgic.palpitation(dactyl) # Note the imported call
        demarcation = mystificate.dark_voodoo(inception)
        return demarcation

    def test(self, whatever):
        """
        This test method tests the test by testing your patience.
        """
        print(whatever)

if __name__ == "__main__":
    print("Forming...")
    f = Foo("epicaricacy", "perseverate")
    f.test("Codswallop")