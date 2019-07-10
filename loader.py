import argparse
from loaded import deobfuscators

argparser = argparse.ArgumentParser(
    description='Python Deobfuscator',
    formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=50)
)
argparser.add_argument('-i', '--input', nargs='?', required=True, help='input file or directory', metavar='file | dir')
argparser.add_argument('-o', '--output', nargs='?', required=True, help='output file or directory', metavar='file | dir')
argparser.add_argument('-v', '--version', action='version', version='0.0.1')
argparser.add_argument('-d', '--deobfuscator', nargs='?', required=True, help='deobfuscator to use', choices=['intensio', 'pyminifier'])


def _prepend_argument(argument: str, to_prepend: str):
    """
    Prepend as string to an argument
    :param argument:
    :param to_prepend:
    :return:
    """
    return '--{0}-{1}'.format(to_prepend, argument[2:]) if argument[:2] == '--' \
        else '-{0}-{1}'.format(to_prepend, argument[1:])


for deobfuscator in deobfuscators:
    group = argparser.add_argument_group('{0} ({1})'.format(deobfuscator.name, deobfuscator.id), deobfuscator.description)

    for arg in deobfuscator.arguments:
        parameters, options = arg

        # Make sure parameters are unique by prepending the argument id
        parameters_list = list(parameters)
        for i in range(0, len(parameters_list)):
            parameters_list[i] = _prepend_argument(parameters_list[i], deobfuscator.id)

        group.add_argument(*tuple(parameters_list), **options)

args = argparser.parse_args()
