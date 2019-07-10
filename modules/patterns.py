import re


DEF = re.compile(r"def\s*([a-zA-Z_][a-zA-Z0-9_]+)\s*\((.+)\)")
CLASS = re.compile(r"class\s+([a-zA-Z_][a-zA-Z0-9_]+)\s*(?:\(|:)")
CLASS_PARENTS = re.compile(r"class\s+[a-zA-Z_][a-zA-Z0-9_]+\s*\((.+?)\)")
FOR_LOOP = re.compile(r"for\s+([a-zA-Z_][a-zA-Z0-9_]+)\s+in")
IDENTIFIER = "[a-zA-Z_][a-zA-Z0-9_]+"
