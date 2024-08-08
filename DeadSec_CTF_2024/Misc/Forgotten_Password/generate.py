from io import BytesIO
import os
import subprocess
import pycdlib # pip install pycdlib

try:
    FLAG = open("flag.txt","r").read()
except FileNotFoundError:
    FLAG = "fake_flag_for_testing"

iso = pycdlib.PyCdlib()
iso.new(interchange_level=4)

iso.add_fp(BytesIO(FLAG.encode()), len(FLAG), '/flag.txt;1')

iso.write('challenge.iso')
iso.close()

subprocess.check_output(["zip", "challenge.zip", "challenge.iso", "-P", FLAG])