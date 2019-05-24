#!/usr/sbin/python3
import lhafile
import struct
import sys
import pathlib

inf = sys.argv[1]
a = lhafile.LhaFile(inf)
for info in a.infolist():
    name = b''.join([struct.pack('B', ord(i)) for i in info.filename])
    name = name.decode('shift_jis')
    sep = name.split('\\')
    if len(sep) > 1:
        d = pathlib.Path(*sep[:-1])
        d.mkdir(parents=True, exist_ok=True)
    pathlib.Path(*sep).write_bytes(a.read(info.filename))
