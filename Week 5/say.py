import cowsay # type: ignore
import sys

if  len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
