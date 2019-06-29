import tempfile
import re
import base64
import bz2
import zlib
import lzma
from helpers import read_file_contents


def decompress(input_file: str, method: str):
    content = read_file_contents(input_file)

    if 'exec' not in content and 'decompress' not in content:
        return False

    # create temporary file to write the decompressed code to
    temp = tempfile.NamedTemporaryFile(mode='r+b')

    match = re.search(r"b64decode\('(.+)'\)", content)
    if match:
        compressed = base64.b64decode(match.group(1))
        if method == 'bzip2':
            temp.write(bz2.decompress(compressed))
        elif method == 'gzip':
            temp.write(zlib.decompress(compressed))
        elif method == 'lzma':
            temp.write(lzma.decompress(compressed))

        # finally, write temp file contents to input file
        temp.seek(0)
        with open(input_file, 'wb') as o:
            for line in temp:
                o.write(line)

        # destroy temp file
        temp.close()

        return True

    else:
        return False
