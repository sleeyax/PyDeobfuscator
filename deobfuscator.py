import os
import sys
import glob
from loader import args
from modules import deobfuscators
from logger import error, info, debug, header

print("""\033[92m
  _____       _____             _      __                     _             
 |  __ \     |  __ \           | |    / _|                   | |            
 | |__) |   _| |  | | ___  ___ | |__ | |_ _   _ ___  ___ __ _| |_ ___  _ __ 
 |  ___/ | | | |  | |/ _ \/ _ \| '_ \|  _| | | / __|/ __/ _` | __/ _ \| '__|
 | |   | |_| | |__| |  __/ (_) | |_) | | | |_| \__ \ (_| (_| | || (_) | |   
 |_|    \__, |_____/ \___|\___/|_.__/|_|  \__,_|___/\___\__,_|\__\___/|_|   
         __/ |                                                              
        |___/                                                               

\033[0m""")

# exit if input file or directory doesn't exist
if not os.path.exists(args.input):
    error('directory or file \'{0}\' does not exist!'.format(args.input))
    sys.exit(0)

# recursively read all files in the input dir to an array
input_files = [f for f in glob.glob('{0}/**/*.py'.format(args.input.rstrip('/')), recursive=True)] \
    if os.path.isdir(args.input) \
    else [args.input]

deobfuscator = next(d for d in deobfuscators if d.name == args.deobfuscator)
header(' using \033[94m{0}\033[0m deobfuscator '.format(deobfuscator.name))
deobfuscator.arguments_parsed = args

# amp input files to output files
io = {}
for input_file in input_files:
    output_file = input_file.replace(args.input, args.output)

    # recursively create output directories
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    io[input_file] = output_file

deobfuscator.deobfuscate(io)
