import re


def reindent(line: str, char, width, start_length=1):
    match = re.match(r'^\s+', line)
    if not match:
        return line
    whitespaces = match.group(0)
    length = int(len(whitespaces) / start_length)
    return '{0}{1}'.format(char * width * length, line.strip())
