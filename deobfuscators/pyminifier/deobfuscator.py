import re
from modules.declarations.basedeclaration import BaseDeclaration


class Deobfuscator(BaseDeclaration):
    def __init__(self):
        self.variables = {}
        self.keywords = {}
        self.builtins = [
            'ArithmeticError',
            'AssertionError',
            'AttributeError',
            'BaseException',
            'BufferError',
            'BytesWarning',
            'DeprecationWarning',
            'EOFError',
            'Ellipsis',
            'EnvironmentError',
            'Exception',
            'False',
            'FloatingPointError',
            'FutureWarning',
            'GeneratorExit',
            'IOError',
            'ImportError',
            'ImportWarning',
            'IndentationError',
            'IndexError',
            'KeyError',
            'KeyboardInterrupt',
            'LookupError',
            'MemoryError',
            'NameError',
            'None',
            'NotImplemented',
            'NotImplementedError',
            'OSError',
            'OverflowError',
            'PendingDeprecationWarning',
            'ReferenceError',
            'RuntimeError',
            'RuntimeWarning',
            'StandardError',
            'StopIteration',
            'SyntaxError',
            'SyntaxWarning',
            'SystemError',
            'SystemExit',
            'TabError',
            'True',
            'TypeError',
            'UnboundLocalError',
            'UnicodeDecodeError',
            'UnicodeEncodeError',
            'UnicodeError',
            'UnicodeTranslateError',
            'UnicodeWarning',
            'UserWarning',
            'ValueError',
            'Warning',
            'ZeroDivisionError',
            '__IPYTHON__',
            '__IPYTHON__active',
            '__debug__',
            '__doc__',
            '__import__',
            '__name__',
            '__package__',
            'abs',
            'all',
            'any',
            'apply',
            'basestring',
            'bin',
            'bool',
            'buffer',
            'bytearray',
            'bytes',
            'callable',
            'chr',
            'classmethod',
            'cmp',
            'coerce',
            'compile',
            'complex',
            'copyright',
            'credits',
            'delattr',
            'dict',
            'dir',
            'divmod',
            'dreload',
            'enumerate',
            'eval',
            'execfile',
            'exit',
            'file',
            'filter',
            'float',
            'format',
            'frozenset',
            'getattr',
            'globals',
            'hasattr',
            'hash',
            'help',
            'hex',
            'id',
            'input',
            'int',
            'intern',
            'ip_set_hook',
            'ipalias',
            'ipmagic',
            'ipsystem',
            'isinstance',
            'issubclass',
            'iter',
            'jobs',
            'len',
            'license',
            'list',
            'locals',
            'long',
            'map',
            'max',
            'min',
            'next',
            'object',
            'oct',
            'open',
            'ord',
            'pow',
            'print',
            'property',
            'quit',
            'range',
            'raw_input',
            'reduce',
            'reload',
            'repr',
            'reversed',
            'round',
            'set',
            'setattr',
            'slice',
            'sorted',
            'staticmethod',
            'str',
            'sum',
            'super',
            'tuple',
            'type',
            'unichr',
            'unicode',
            'vars',
            'xrange',
            'zip'
        ]

    def assigns_builtin_keyword(self, line):
        match = re.match(r"(.+)=([^\"|'].+)", line)
        if match and line.count('=') == 1:
            if not any(b == match.group(2) for b in self.builtins):
                return False

            self.keywords[match.group(1)] = match.group(2)
            return True

        return False

    def process(self, line: str):

        self.detect_declaration(line, r"([^=]+)=(?:\"|').+(?:\"|')", self.variables, 'var')

        # if a keyword is assigned to a variable (a=print, b=ImportError, ...), store it and remove the line from output
        if self.assigns_builtin_keyword(line.strip()):
            return None

        # replace variable names
        for key, value in self.variables.items():
            line = line.replace(key, value)

        # replace variables with keywords
        for key, value in self.keywords.items():
            line = re.sub(r'\b{0}\b'.format(key), value, line)

        return line
