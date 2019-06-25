import re
from .basemodule import BaseModule


class Declarations(BaseModule):
    def __init__(self):
        self.length_levels = [32, 64, 128]
        self.length_levels_pattern = self.build_length_levels_pattern(self.length_levels)
        self.variables_count = 0
        self.variables = {}
        self.classes = {}
        self.methods = {}

    def build_length_levels_pattern(self, length_levels):
        parts = ['[a-zA-Z]{' + str(l) + '}' for l in length_levels]
        return '|'.join(parts)

    def build_variables_pattern(self, lengths_pattern):
        # ^((?:[a-zA-Z]{32}|[a-zA-Z]{64}|[a-zA-Z]{128})+)\s*=
        return r'^((?:' + lengths_pattern + ')+)\\s*='

    def detect_variable_declaration(self, line: str):
        pattern = self.build_variables_pattern(self.length_levels_pattern)
        match = re.match(pattern, line)
        if match and match.group(1) not in self.variables.keys():
            self.variables_count += 1
            self.variables[match.group(1)] = 'var' + str(self.variables_count)

    def process(self, line: str):
        self.detect_variable_declaration(line)

        # TODO: detect class, method, loop, exception declaration

        for key, value in self.variables.items():
            line = line.replace(key, value)

        return line
