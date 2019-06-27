from .basedeclaration import BaseDeclaration


class Module(BaseDeclaration):
    def __init__(self):
        super().__init__()
        self.modules = {}

    def process(self, line):
        if 'from' in line and 'import' in line:
            modules = line.split('import')[1].split(',')
            for module in modules:
                self.detect_declaration(module, '({0})', self.modules, 'module')

        for key, value in self.modules.items():
            line = line.replace(key, value)
        return line