import re
from ..basemodule import BaseModule
from abc import ABC, abstractmethod


class BaseDeclaration(BaseModule, ABC):
    def detect_declaration(self, line: str, pattern: str, collection: dict, keyword: str, ai_keyword: bool = True, strip: bool = True):
        """
        Detects a declaration (i.e var, class, def, ...) in the specified line of text

        :param line: line of text to search through
        :param pattern: regex pattern to apply
        :param collection: dictionary where a key : value pair of pattern match.group(1) : keyword will be saved
        :param keyword: replacement value
        :param ai_keyword: whether or not an auto incrementing integer should be appended to the keyword
        :param strip: whether or not the line should be stripped of whitespaces first
        :return:
        """
        line = line.strip() if strip else line
        match = re.match(pattern, line)
        if match and match.group(1) not in collection.keys():
            if ai_keyword:
                count = len(collection.items()) + 1
                collection[match.group(1)] = keyword + str(count)
            else:
                collection[match.group(1)] = keyword

    @abstractmethod
    def process(self, line):
        pass
