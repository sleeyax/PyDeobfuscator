import argparse
from modules import deobfuscators
from helpers import prepend_argument

argparser = argparse.ArgumentParser(
    description='Python Deobfuscator',
    formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=50)
)
argparser.add_argument('-i', '--input', nargs='?', required=True, help='input file or directory', metavar='file | dir')
argparser.add_argument('-o', '--output', nargs='?', required=True, help='output file or directory', metavar='file | dir')
argparser.add_argument('-v', '--version', action='version', version='beta')
argparser.add_argument('-d', '--deobfuscator', nargs='?', required=True, help='deobfuscator to use', choices=['intensio', 'pyminifier'])


for deobfuscator in deobfuscators:
    group = argparser.add_argument_group('{0} ({1})'.format(deobfuscator.name, deobfuscator.argument_id), deobfuscator.description)

    for arg in deobfuscator.arguments:
        parameters, options = arg

        # Make sure parameters are unique by prepending the argument id
        parameters_list = list(parameters)
        for i in range(0, len(parameters_list)):
            parameters_list[i] = prepend_argument(parameters_list[i], deobfuscator.argument_id)

        group.add_argument(*tuple(parameters_list), **options)

args = argparser.parse_args()