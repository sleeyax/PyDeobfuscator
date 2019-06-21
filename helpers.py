

# prepend something ot an argument
# example: prepend 'my' to --argument -> --my-argument
def prepend_argument(arg, to_prepend):
    return arg[:arg.rfind('-') + 1] + to_prepend + '-' + arg[arg.rfind('-') + 1:]
