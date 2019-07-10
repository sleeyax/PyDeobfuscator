from .basedeclaration import BaseDeclaration
import re


class Other(BaseDeclaration):
    def __init__(self, pattern):
        super().__init__()
        self.others = {}
        self.pattern = pattern

    def process(self, line):
        pattern = '(' + self.pattern + ')'
        matches = re.findall(pattern, line)

        for match in matches:
            self.detect_declaration(match, pattern, self.others, 'other')

        for key, value in self.others.items():
            line = line.replace(key, value)

        return line
