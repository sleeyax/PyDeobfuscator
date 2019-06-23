import os
import sys
import glob
from loader import args
from modules import deobfuscators
from logger import error, info, debug

debug(args)

# exit if input file or directory doesn't exist
if not os.path.exists(args.input):
    error('directory \'{0}\' does not exist!'.format(args.input))
    sys.exit(0)

# give every deobfuscator access to the parsed arguments
for deobfuscator in deobfuscators:
    deobfuscator.arguments_parsed = args

# recursively create output directories
output_dir = os.path.dirname(args.output)
if not os.path.exists(output_dir):
    info('creating output directories...')
    os.makedirs(output_dir)

# recursively read all files in the input dir to an array
input_files = [f for f in glob.glob('{0}/**/*.py'.format(args.input.rstrip('/')), recursive=True)] \
    if os.path.isdir(args.input) \
    else [args.input]

deobfuscator = next(d for d in deobfuscators if d.name == args.deobfuscator)
info('deobfuscating files using {0}...'.format(deobfuscator.name))
deobfuscator.arguments_parsed = args

for input_file in input_files:
    output_file = input_file.replace(args.input, args.output)
    deobfuscator.deobfuscate(input_file, output_file)