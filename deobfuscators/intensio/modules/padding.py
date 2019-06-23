import re

from .basemodule import BaseModule


class Padding(BaseModule):
    def __init__(self):
        self.length_levels = [32, 64, 128]
        self.pattern = self.build_pattern(self.length_levels)

    def build_pattern(self, length_levels):
        parts = ['[a-zA-Z]{' + str(l) + '}' for l in length_levels]
        level_pattern = '|'.join(parts)
        # ^((?:[a-zA-Z]{32}|[a-zA-Z]{64}|[a-zA-Z]{128})) = (?:'|\")(?:[a-zA-Z]{32}|[a-zA-Z]{64}|[a-zA-Z]{128})(?:'|\")$
        return r"^((?:" + level_pattern + ")) = (?:'|\")(?:" + level_pattern + ")(?:'|\")$"

    def process(self, line):
        # TODO: implement
        pass
