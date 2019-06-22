

# prepend something ot an argument
# example: prepend 'my' to --argument -> --my-argument
def prepend_argument(arg, to_prepend):
    return '--{0}-{1}'.format(to_prepend, arg[2:]) if arg[:2] == '--' else '-{0}-{1}'.format(to_prepend, arg[1:])