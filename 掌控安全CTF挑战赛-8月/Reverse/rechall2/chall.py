# Python 3.11.4
import marshal
import pickle
import pickletools
import dis
import types

from fickling.fickle import Pickled
import ast

code = b'\x80\x04ctypes\nFunctionType\nctypes\nCodeType\n(I1\nI0\nI0\nI1\nI13\nI3\nC\xb6\x97\x00t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x04\x00\x00\x00\x00\x00\x00\x00\x00|\x00t\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00S\x00(Nt(Vbytes\nVdecode\nVmap\nVint\nV__add__\nVrange\nVlen\nt(\x8c\x10BanG Its Mygo!!!tVLiang ge ren xiang biao da de han yi ne, shi\nVWo xi huan ni, Ni xi huan wo\nVDan shi ne, hui yan 13 ji\nI1\nC\x02\x02\x01C\x00tRcbuiltins\nglobals\n)R\x86R\x940g0\nC\x08btgipdhl\x85Rg0\nC\nssp+ai]h\\\\\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\x05imnrp\x85R\x93VTell me your answer >\n\x85R\x85R\x940g0\nC\x06r`lakh\x85Rg0\nC\x04sdca\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\nssp+ai]h\\\\\x85R\x93VD0_Y0u_Kn0w_Wh4t_th3_D0oR_Th1s_K3y_Op3ns?\n\x85R\x85R0g0\nC\x06r`lakh\x85Rg0\nC\tr`la^tn^k\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\x03ldl\x85R\x93g1\n\x85R\x85R\x940g0\nC\x08btgipdhl\x85Rg0\nC\x03m`n\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\x0bimr+[ZrhjVU\x85R\x93g1\ng0\nC\x08btgipdhl\x85Rg0\nC\x03m`n\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\x0bimr+[Z[g\\VU\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\x03m`n\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\nimr+[ZikWV\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\x03m`n\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\x0eimr+[Zfl``\\iSR\x85R\x93g2\ng0\nC\x08btgipdhl\x85Rg0\nC\x0clhqq*ZYfmcUT\x85R\x93(I4\nlg0\nC\x08btgipdhl\x85Rg0\nC\x03ldl\x85R\x93g1\n\x85R\x86R\x87Rg0\nC\x08btgipdhl\x85Rg0\nC\x03m`n\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\x0eimr+[Zll``\\iSR\x85R\x93g2\ng0\nC\x08btgipdhl\x85Rg0\nC\x0clhqq*ZYfmcUT\x85R\x93(I4\nlg0\nC\x08btgipdhl\x85Rg0\nC\x03ldl\x85R\x93g1\n\x85R\x86R\x87R\x87Rg0\nC\x08btgipdhl\x85Rg0\nC\x0clhqq*ZYfmcUT\x85R\x93(I255\nlg0\nC\x08btgipdhl\x85Rg0\nC\x03ldl\x85R\x93g1\n\x85R\x86R\x87R\x87R\x940g0\nC\x08btgipdhl\x85Rg0\nC\x10lhqq*ZY`]k_iY`QP\x85R\x93(VGood job! You made it!\nVNah, dont give up!\nlg0\nC\x08btgipdhl\x85Rg0\nC\nimr+[ZikWV\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\x03amw\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\x03m`n\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\x0bimr+[ZrhjVU\x85R\x93(I235\nI128\nI107\nI33\nI10\nI206\nI158\nI151\nI158\nI88\nI130\nI190\nI155\nI207\nI94\nI28\nI65\nI9\nI102\nI5\nI241\nI184\nI74\nI129\nI3\nI46\nI216\nI20\nI112\nI95\nI201\nI86\nI215\nI220\nI220\nI7\nI45\nI81\nI145\nI229\nI152\nI241\nI4\nI135\nI16\nI118\nI102\nI144\nlg3\n\x87R\x85Rg0\nC\x08btgipdhl\x85Rg0\nC\nimr+[Zh^WV\x85R\x93g0\nC\x08btgipdhl\x85Rg0\nC\x03ldl\x85R\x93g2\n\x85RI48\n\x86R\x86R\x86R.'
fickled_object = Pickled.load(code)
print(ast.dump(fickled_object.ast, indent=4))
# pickletools.dis(code)
# print(code.decode())
# a = pickle.loads(code)
# print(a)

code_obj = types.CodeType(1, 0, 0, 1, 13, 3,
                          b'\x97\x00t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x06\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x00\x00j\x04\x00\x00\x00\x00\x00\x00\x00\x00|\x00t\x0b\x00\x00\x00\x00\x00\x00\x00'
                          b'\x00\x00\x00t\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00\xa6\x01\x00\x00\xab\x01\x00'
                          b'\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6'
                          b'\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00'
                          b'\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00S\x00',
                          (), ('bytes', 'decode', 'map', 'int', '__add__', 'range', 'len'), ('BanG Its Mygo!!!',),
                          'Liang ge ren xiang biao da de han yi ne, shi', 'Wo xi huan ni, Ni xi huan wo',
                          'Dan shi ne, hui yan 13 ji', 1, b'\x02\x01', b'', ())
a = types.FunctionType(code_obj, globals())(b'btgipdhl')
print(b'btgipdhl', a)
a = types.FunctionType(code_obj, globals())(b'ssp+ai]h\\\\')
print(b'ssp+ai]h\\\\', a)
a = types.FunctionType(code_obj, globals())(b'imnrp')
print(b'imnrp', a)
a = types.FunctionType(code_obj, globals())(b'r`lakh')
print(b'r`lakh', a)
a = types.FunctionType(code_obj, globals())(b'sdca')
print(b'sdca', a)
a = types.FunctionType(code_obj, globals())(b'r`la^tn^k')
print(b'r`la^tn^k', a)
a = types.FunctionType(code_obj, globals())(b'ldl')
print(b'ldl', a)
a = types.FunctionType(code_obj, globals())(b'm`n')
print(b'm`n', a)
a = types.FunctionType(code_obj, globals())(b'imr+[ZrhjVU')
print(b'imr+[ZrhjVU', a)
a = types.FunctionType(code_obj, globals())(b'imr+[Z[g\\VU')
print(b'imr+[Z[g\\VU', a)
a = types.FunctionType(code_obj, globals())(b'imr+[ZikWV')
print(b'imr+[ZikWV', a)
a = types.FunctionType(code_obj, globals())(b'imr+[Zfl``\\iSR')
print(b'imr+[Zfl``\\iSR', a)
a = types.FunctionType(code_obj, globals())(b'lhqq*ZYfmcUT')
print(b'lhqq*ZYfmcUT', a)
a = types.FunctionType(code_obj, globals())(b'imr+[Zh^WV')
print(b'imr+[Zh^WV', a)
a = types.FunctionType(code_obj, globals())(b'lhqq*ZY`]k_iY`QP')
print(b'lhqq*ZY`]k_iY`QP', a)
a = types.FunctionType(code_obj, globals())(b'lhqq*ZYfmcUT')
print(b'lhqq*ZYfmcUT', a)
a = types.FunctionType(code_obj, globals())(b'imr+[Zll``\\iSR')
print(b'imr+[Zll``\\iSR', a)
a = types.FunctionType(code_obj, globals())(b'amw')
print(b'amw', a)
# with open("code.pyc", "wb") as f:
#     # pyc header from main.pyc
#     f.write(b'\xA7\x0D\x0D\x0A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
#     marshal.dump(code_obj, f)

# return bytes.decode(bytes(map(int.__add__, BanG Its Mygo!!!, range(len(BanG Its Mygo!!!)))))

s = [235,128,107,33,10,206,158,151,158,88,130,190,155,207,94,28,65,9,102,5,241,184,74,129,3,46,216,20,112,95,201,86,215,220,220,7,45,81,145,229,152,241,4,135,16,118,102,144]
print(len(s))
for i in range(len(s)):
    s[i] ^= 48
print(s)