import re
from ..basemodule import BaseModule
from deobfuscators.intensio.helpers import build_length_levels_pattern
from abc import ABC, abstractmethod


class BaseDeclaration(BaseModule, ABC):
    def __init__(self):
        self.characters_to_match = build_length_levels_pattern([32, 64, 128])

    def detect_declaration(self, line: str, pattern: str, collection: dict, keyword: str, auto_format: bool = True):
        line = line.strip()
        if auto_format:
            pattern = pattern.format(self.characters_to_match)
        match = re.match(pattern, line)
        if match and match.group(1) not in collection.keys():
            count = len(collection.items()) + 1
            collection[match.group(1)] = keyword + str(count)

    @abstractmethod
    def process(self, line):
        pass
