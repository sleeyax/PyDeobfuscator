from .basedeclaration import BaseDeclaration
import re


class Other(BaseDeclaration):
    def __init__(self):
        super().__init__()
        self.others = {}

    def process(self, line):
        matches = re.findall('({0})'.format(self.characters_to_match), line)
        for match in matches:
            self.detect_declaration(match, '({0})', self.others, 'other')

        for key, value in self.others.items():
            line = line.replace(key, value)
        return line
