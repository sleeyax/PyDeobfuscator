import re

from .basemodule import BaseModule


class Padding(BaseModule):
    def __init__(self):
        self.length_levels = [32, 64, 128]
        self.pattern = self.build_pattern(self.length_levels)
        self.trash = []
        self.current_line_is_trash = False

    def build_pattern(self, length_levels):
        parts = ['[a-zA-Z]{' + str(l) + '}' for l in length_levels]
        level_pattern = '|'.join(parts)
        # ((?:[a-zA-Z]{32}|[a-zA-Z]{64}|[a-zA-Z]{128})) = (?:'|\")(?:[a-zA-Z]{32}|[a-zA-Z]{64}|[a-zA-Z]{128})(?:'|\")
        return r"((?:" + level_pattern + ")) = (?:'|\")(?:" + level_pattern + ")(?:'|\")"

    def process(self, line: str):
        # remove the line from output when it matches a fake variable
        matches = [t for t in self.trash if t in line]
        if len(matches) > 0:
            self.current_line_is_trash = True
            return None

        # if this line declares a fake variable, add it to the list & remove it from output
        matches = re.search(self.pattern, line)
        if matches:
            trash = matches.group(1)
            if trash not in self.trash:
                self.current_line_is_trash = True
                self.trash.append(trash)
            return None

        # remove stray code from output
        if 'else:' in line and self.current_line_is_trash is True:
            self.current_line_is_trash = False
            return None

        # return line if it does not contain any signs of padding
        self.current_line_is_trash = False
        return line
