import ast
import astunparse


class AstEditor:
    def __init__(self, code: str = None, handler=None):
        self.tree = None
        self.handler = None
        if handler:
            self.register_handler(handler)
        if code:
            self.read(code)

    def read(self, code: str):
        self.tree = ast.parse(code)

    def register_handler(self, handler):
        self.handler = handler

    def save_changes(self):
        return astunparse.unparse(self.iterate(self.tree))

    def iterate(self, tree):
        if isinstance(tree, list):
            items = []
            for branch in tree:
                items.append(self.iterate(branch))
            return items

        # if the tree has a body=[...] attribute, iterate over it
        if getattr(tree, 'body', None):
            tree.body = self.iterate(tree.body)

        # let the handler manipulate the tree
        method = getattr(self.handler, '_{0}'.format(tree.__class__.__name__.lower()), self.default)
        return method(tree)

    def default(self, tree):
        return tree

