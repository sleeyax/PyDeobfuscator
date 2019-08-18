# PyDeobfuscator
**Currenlty unmaintained untill further notice** <br>

Deobfuscate obfuscated python files. 
This tool will remove junk, reformat code & make it more readable.

## Supported obfuscators
* [Intensio Obfuscator](https://github.com/Hnfull/Intensio-Obfuscator) (1.0.3)
* [pyminifier](https://github.com/liftoff/pyminifier) (2.1)

## Installation
Requires python 3.5+
```
$ git clone https://github.com/sleeyax/PyDeobfuscator.git
$ cd PyDeobfuscator
```

## Usage
```
$ python deobfuscator.py --help
usage: deobfuscator.py [-h] -i [file | dir] -o [file | dir] [-v] -d
                       [{intensio,pyminifier}] [--int-keep-padding]
                       [--int-keep-classes] [--int-keep-vars]
                       [--int-keep-methods] [--int-keep-loops]
                       [--int-keep-exc] [--min-no-unminify] [--min-no-deobf]
                       [--min-use-tabs] [--min-decompress [{bzip2,gzip,lzma}]]

Python Deobfuscator

optional arguments:
  -h, --help                                      show this help message and
                                                  exit
  -i [file | dir], --input [file | dir]           input file or directory
  -o [file | dir], --output [file | dir]          output file or directory
  -v, --version                                   show program's version
                                                  number and exit
  -d [{intensio,pyminifier}], --deobfuscator [{intensio,pyminifier}]
                                                  deobfuscator to use

intensio (int):
  deobfuscate files obfuscated by Intensio Obfuscator

  --int-keep-padding                              do not remove padding
  --int-keep-classes                              keep obfuscated classes
  --int-keep-vars                                 keep obfuscated variables
  --int-keep-methods                              keep obfuscated methods
  --int-keep-loops                                keep obfuscated (for) loops
  --int-keep-exc                                  keep obfuscated exceptions

pyminifier (min):
  deobfuscate files obfuscated, minified or compressed by pyminifier

  --min-no-unminify                               do not reformat file(s)
  --min-no-deobf                                  do not deobfuscate file(s)
  --min-use-tabs                                  use tabs for indentation
                                                  instead of spaces
  --min-decompress [{bzip2,gzip,lzma}]            decompress file(s)
```

## Screenshots
![intensio example](https://i.imgur.com/G5osnnm.png)

## Examples
## Intensio
Obfuscated:
```
nIkikkWWQKpFDuXtzNqRgtWHdMqYhlSH = "Danny"
dAIIhsSOSuNWCeGuTOSnzZDTFJatdlFq = 'xnmsdFMOkFysdHbwonuGIiZPcwHRXdYk'
KNmfmzoqMvPFzJAGIjTolxpwXGjHIQBo = 'xQckSltgKmruPzksLQuDmeuepupbfVXE'
fvZPgBmjGMgzYNFtWrLOGNHoGLHyjgBW = 'JIukCZLjNlGSosjgoWcoDuwjwxajKwpO'
if dAIIhsSOSuNWCeGuTOSnzZDTFJatdlFq == KNmfmzoqMvPFzJAGIjTolxpwXGjHIQBo:
    tgeedkrBcamwecheSIpcEPSBEahovWTR = 'LLLjNONJUdZNJKBLZntnMjwtvnxfYPUA'
    tgeedkrBcamwecheSIpcEPSBEahovWTR = dAIIhsSOSuNWCeGuTOSnzZDTFJatdlFq
else:
    tgeedkrBcamwecheSIpcEPSBEahovWTR = 'LLLjNONJUdZNJKBLZntnMjwtvnxfYPUA'
    tgeedkrBcamwecheSIpcEPSBEahovWTR = fvZPgBmjGMgzYNFtWrLOGNHoGLHyjgBW
print("Hello,  " + nIkikkWWQKpFDuXtzNqRgtWHdMqYhlSH)
XIKMcrBmPNKXNCJZSCLcnUCfAoLQFpBk = 'PMSSYjsqTWYQcGFNSamZTsnSBEwWWYqt'
MCOqEWdwlXxkMIUwaBdPKsUgaVpjOXYQ = 'plQCVYcpuZEzTmhERzyHBUGwPRpHXITQ'
uGCLQqdMzhfNRasqBiYFcZOUqVTqHvZT = 'QRObAmhPiuwTBVmJJIyaKnQHmBDRkrHK'
JOMTXSNCcFaVtFBZCgnaIoVBbHbdiwRb = 'YISoyHXnpnaYnUoZZLdtywYiPKgQIxym'
wuXTISefIHdfOefFAfQHcctTiFoWAwHW = 'NBJppWosXrCcoxfiiIBrbTrcDsvtGZbT'
NCOuaTudVjzafaxdKkrlghfwcAJxZNXX = 'fzrtrCgDKnrMGTSmpPWdBUgobyhpxqoZ'
if XIKMcrBmPNKXNCJZSCLcnUCfAoLQFpBk != JOMTXSNCcFaVtFBZCgnaIoVBbHbdiwRb:
    MCOqEWdwlXxkMIUwaBdPKsUgaVpjOXYQ = uGCLQqdMzhfNRasqBiYFcZOUqVTqHvZT
    for NCOuaTudVjzafaxdKkrlghfwcAJxZNXX in JOMTXSNCcFaVtFBZCgnaIoVBbHbdiwRb:
        if NCOuaTudVjzafaxdKkrlghfwcAJxZNXX != uGCLQqdMzhfNRasqBiYFcZOUqVTqHvZT:
            MCOqEWdwlXxkMIUwaBdPKsUgaVpjOXYQ = MCOqEWdwlXxkMIUwaBdPKsUgaVpjOXYQ
        else:
            wuXTISefIHdfOefFAfQHcctTiFoWAwHW = XIKMcrBmPNKXNCJZSCLcnUCfAoLQFpBk
else:
    uGCLQqdMzhfNRasqBiYFcZOUqVTqHvZT = XIKMcrBmPNKXNCJZSCLcnUCfAoLQFpBk
    XIKMcrBmPNKXNCJZSCLcnUCfAoLQFpBk = wuXTISefIHdfOefFAfQHcctTiFoWAwHW
    if uGCLQqdMzhfNRasqBiYFcZOUqVTqHvZT == XIKMcrBmPNKXNCJZSCLcnUCfAoLQFpBk:
        for NCOuaTudVjzafaxdKkrlghfwcAJxZNXX in XIKMcrBmPNKXNCJZSCLcnUCfAoLQFpBk:
            if NCOuaTudVjzafaxdKkrlghfwcAJxZNXX == uGCLQqdMzhfNRasqBiYFcZOUqVTqHvZT:
                uGCLQqdMzhfNRasqBiYFcZOUqVTqHvZT = XIKMcrBmPNKXNCJZSCLcnUCfAoLQFpBk
            else:
                uGCLQqdMzhfNRasqBiYFcZOUqVTqHvZT = wuXTISefIHdfOefFAfQHcctTiFoWAwHW

```
Deobfuscated:
```
var1 = "Danny"
print("Hello,  " + var1)
```
## Pyminifier
Compressed:
```
import bz2, base64
exec(bz2.decompress(base64.b64decode('QlpoOTFBWSZTWYxMdf4AABDbgAAQcOgAEoCAK2XfICAAVFaE8pg1MBDNCJk1NNonqaG1NqDSCdHsDpYzWtV8hMEMQIr3YI68EyCTFh8LIYwKipdh8G0OKQBFwT8S6EhPgu5IpwoSEYmOv8A=')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
```
Decompressed:
```
color=input("What's your favorite color? : ")
print(color+" is a nice choice!")
```

See [examples](https://github.com/sleeyax/PyDeobfuscator/tree/master/examples) for more deobfuscation results
