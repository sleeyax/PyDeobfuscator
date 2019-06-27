import re

from ..helpers import build_length_levels_pattern
from .basemodule import BaseModule


class Declarations(BaseModule):
    def __init__(self):
        self.characters_to_match = build_length_levels_pattern([32, 64, 128])
        self.modules = {}
        self.variables = {}
        self.classes = {}
        self.methods = {}
        self.for_loops = {}
        self.method_arguments = {}
        self.exceptions = {}

    def detect_declaration(self, line: str, pattern: str, collection: dict, keyword: str, auto_format: bool = True):
        line = line.strip()
        if auto_format:
            pattern = pattern.format(self.characters_to_match)
        match = re.match(pattern, line)
        if match and match.group(1) not in collection.keys():
            count = len(collection.items()) + 1
            collection[match.group(1)] = keyword + str(count)

    def detect_variable_declaration(self, line: str):
        line = line.strip()

        # check if multiple vars are defined (a, b = 'c', 'd')
        if re.match('{0}\\s*,'.format(self.characters_to_match), line) and '=' in line:
            match = re.match(r'(.+?)=', line)
            variables = match.group(1).split(',')
            for variable in variables:
                self.detect_declaration(variable, '({0})', self.variables, 'var')

        # single variable declaration (a = 'b')
        else:
            self.detect_declaration(line, '({0})\\s*=', self.variables, 'var')

    def detect_class_declaration(self, line: str):
        self.detect_declaration(line, 'class\\s+({0}?)(?:\\(|:)', self.classes, 'Class')

    def detect_method_declaration(self, line: str):
        self.detect_declaration(line, 'def\\s+({0})', self.methods, 'method')

    def detect_for_loop_declaration(self, line: str):
        self.detect_declaration(line, 'for\\s+({0})\\s+in', self.for_loops, 'i')

    def detect_modules(self, line: str):
        if 'from' in line and 'import' in line:
            modules = line.split('import')[1].split(',')
            for module in modules:
                self.detect_declaration(module, '({0})', self.modules, 'module')

    def detect_method_arguments(self, line: str):
        match = re.search(r'def\s*[a-zA-Z_][a-zA-Z0-9_]*\s*\((.+)\)', line)
        if match:
            args = match.group(1).split(',')
            for arg in args:
                self.detect_declaration(arg, '({0})', self.method_arguments, 'arg')

    def detect_exception(self, line: str):
        if 'except' in line and 'as' in line:
            exceptions = line.split('as')[1].split(',')
            for ex in exceptions:
                self.detect_declaration(ex, '({0})', self.exceptions, 'ex')

    def process(self, line: str):
        self.detect_variable_declaration(line)
        self.detect_class_declaration(line)
        self.detect_method_declaration(line)
        self.detect_method_arguments(line)
        self.detect_for_loop_declaration(line)
        self.detect_modules(line)
        self.detect_exception(line)

        collections = [
            self.modules, self.classes, self.methods, self.method_arguments,
            self.variables, self.for_loops, self.exceptions
        ]
        for collection in collections:
            for key, value in collection.items():
                line = line.replace(key, value)

        return line
