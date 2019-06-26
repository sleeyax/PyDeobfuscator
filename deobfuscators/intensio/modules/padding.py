import re

from .basemodule import BaseModule
from ..helpers import build_length_levels_pattern


class Padding(BaseModule):
    def __init__(self):
        self.trashbin = []
        self.current_line_is_trash = False

    def detect_padding(self, line: str):
        level_pattern = build_length_levels_pattern([32, 64, 128])
        pattern = r"({0}) = (?:'|\"){0}(?:'|\")".format(level_pattern)
        matches = re.search(pattern, line)
        if matches:
            trash = matches.group(1)
            if trash not in self.trashbin:
                self.trashbin.append(trash)
            self.current_line_is_trash = True

    def process(self, line: str):
        # detect start of padding
        self.detect_padding(line)

        # remove the line from output when it matches a fake variable
        if any(t in line for t in self.trashbin):
            self.current_line_is_trash = True
            return None

        # remove stray code from output
        if 'else:' in line and self.current_line_is_trash is True:
            self.current_line_is_trash = False
            return None

        # return line if it does not contain any signs of padding
        self.current_line_is_trash = False
        return line
