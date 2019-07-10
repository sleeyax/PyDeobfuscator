from re import match
from abc import ABC, abstractmethod
from logger import show_progress


class BaseDeobfuscator(ABC):
    def __init__(self):
        super().__init__()
        self.name = 'unknown'
        self.id = 'uk'
        self.description = 'an unknown deobfuscator'
        self.arguments = []
        self._arguments_parsed = None

    def add_argument(self, *args, **kwargs):
        self.arguments.append([args, kwargs])

    def set_parsed_arguments(self, parsed):
        self._arguments_parsed = parsed

    def get_argument_value(self, argument: str):
        """
        Returns the CLI argument value

        :param argument:
        :return:
        """
        arg_name = '{0}_{1}'.format(self.id, argument.lstrip('-')).replace('-', '_')
        return getattr(self._arguments_parsed, arg_name)

    def deobfuscate_using_modules(self, io: dict, modules: list, whitelist_regex_patterns: list = None, blacklisted_regex_patterns: list = None):
        """
        Default obfuscation method

        :param io: dictionary mapping input files to output file
        :param modules: modules to use when processing each line
        :param whitelist_regex_patterns: processing will only continue if it matches all of the whitelisted regex patterns
        :param blacklisted_regex_patterns: do not process a line if it matches any of the blacklisted regex patterns
        :return:
        """
        whitelisted = whitelist_regex_patterns if whitelist_regex_patterns else []
        blacklisted = blacklisted_regex_patterns if blacklisted_regex_patterns else []

        for input_file, output_file in io.items():
            with open(input_file, 'r') as i, open(output_file, 'w') as o:
                for line in i:
                    line = line.rstrip('\n')

                    can_continue = True

                    # if the line doesn't match any of these regex patterns, skip it
                    for pattern in whitelisted:
                        if not match(pattern, line):
                            can_continue = False

                    # if the line does match any of these regex patterns, skip it
                    for pattern in blacklisted:
                        if match(pattern, line):
                            can_continue = False

                    if can_continue:
                        for m in modules:
                            line = m.process(line)
                            if line is None:
                                break

                    if line is not None:
                        o.write(line + '\n')

            show_progress(input_file, output_file, io.keys())

    @abstractmethod
    def deobfuscate(self, io: dict):
        pass
