def build_length_levels_pattern(length_levels):
    parts = ['[a-zA-Z]{' + str(l) + '}' for l in length_levels]
    return '(?:{0})'.format('|'.join(parts))
