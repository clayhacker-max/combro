import os
import sys
import zlib
import base64
import marshal
import binascii
import py_compile
from time import sleep as waktu

p  = '\x1b[0m'
m  = '\x1b[31m'
i  = '\x1b[32m'
b  = '\x1b[34m'
k  = '\x1b[33;1m'
cg = '\x1b[36m'
ba = '\x1b[96;1m'
pu = '\x1b[35m'
gr = '\x1b[37m'
pb = '\x1b[47m'
cout = 0
logo = '         \x1b[34m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mAuthor   \x1b[37m: Mr.Gaming\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mMy Team  \x1b[37m: Black Coder Crush\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mwhatsapp \x1b[37m: 085624490403\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mCodeName \x1b[37m: \x1b[36mComPilez \x1b[0;1mv1.3 \x1b[33;1mnews update !\n         \x1b[34m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'

def main():
    global b
    global binascii
    global cg
    global cout
    global gr
    global i
    global m
    os.system('clear')
    try:
        print logo
        print '\n         \x1b[37m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n         \x1b[37m\xe2\x95\x91       \x1b[33;1m\xe2\x9c\xa4 \x1b[32mCompile Marshal \x1b[33;1m\xe2\x9c\xa4\n         \x1b[37m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n          \x1b[37m\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\n      \x1b[32m[ \x1b[37m1 \x1b[32m] \x1b[37mCompile Marshal\n      \x1b[32m[ \x1b[37m2 \x1b[32m] \x1b[37mCompile Marshal > base64\n      \x1b[32m[ \x1b[37m3 \x1b[32m] \x1b[37mCompile Marshal > base64 > pycom\n      \x1b[32m[ \x1b[37m4 \x1b[32m] \x1b[37mCompile By Gaming 1 [Hard]\n      \x1b[32m[ \x1b[37m5 \x1b[32m] \x1b[37mCompile By Gaming 2 [easy]\n      \x1b[32m[ \x1b[37m6 \x1b[32m] \x1b[37mCompile By Gaming 3 [Laters]\n      \x1b[32m[ \x1b[31mE \x1b[32m] \x1b[33;1mExit\n          \x1b[37m\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\n'
        chos = raw_input('[!] Pilih >> %s' % i)
        if chos == '1':
            os.system('clear')
            print logo
            print '         \x1b[37m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n         \x1b[37m\xe2\x95\x91       \x1b[33;1m\xe2\x9c\xa4 \x1b[32mCompile Marshal \x1b[33;1m\xe2\x9c\xa4\n         \x1b[37m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
            file = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            cot = int(raw_input('%s[%s\xe2\x9b\xa5%s] %sCout >> %s' % (b, m, b, gr, i)))
            if cot < 400:
                out = file.replace('.py', '') + '_enc.py'
                oa = open(file).read()
                ni = compile(oa, '<Goblok>', 'exec')
                bo = marshal.dumps(ni)
                ab = repr(bo)
                s = open(out, 'w')
                s.write('#Compile By Mr.Gaming\n#My Team : Black Coder Crush\nimport marshal\nexec(marshal.loads(' + str(ab) + '))')
                s.close()
                while True:
                    if cot >= cout:
                        nz = open(out).read()
                        dn = compile(nz, '<Goblok>', 'exec')
                        bx = marshal.dumps(dn)
                        nl = repr(bx)
                        ns = open(out, 'w')
                        ns.write('#Compile By Mr.Gaming\n#My Team : Black Coder Crush\nimport marshal\nexec(marshal.loads(' + str(nl) + '))')
                        ns.close()
                        cout += 1
                    else:
                        break

                print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % out
                raw_input('%s[%s\xe2\x9d\x97%s] %sBack %s\xe2\x9e\xa4 %s' % (b, m, b, gr, i, cg))
                main()
            else:
                print '%s[%s+%s] %sCout Terlalu Besar \xe2\x9d\x97' % (b, m, b, gr)
                waktu(0.8)
                main()
        elif chos == '2':
            os.system('clear')
            print logo
            print '         \x1b[37m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n         \x1b[37m\xe2\x95\x91       \x1b[33;1m\xe2\x9c\xa4 \x1b[32mCompile Marshal \x1b[33;1m\xe2\x9c\xa4\n         \x1b[37m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
            file = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            cot = int(raw_input('%s[%s\xe2\x9b\xa5%s] %sCout >> %s' % (b, m, b, gr, i)))
            if cot < 400:
                out = file.replace('.py', '') + '_enc.py'
                oa = open(file).read()
                ni = compile(oa, '<Goblok>', 'exec')
                bo = marshal.dumps(ni)
                ab = repr(bo)
                s = open(out, 'w')
                s.write('#Compile By Mr.Gaming\n#My Team : Black Coder Crush\nimport marshal\nexec(marshal.loads(' + str(ab) + '))')
                s.close()
                while True:
                    if cot >= cout:
                        nz = open(out).read()
                        dn = compile(nz, '<Goblok>', 'exec')
                        bx = marshal.dumps(dn)
                        nl = repr(bx)
                        ns = open(out, 'w')
                        ns.write('#Compile By Mr.Gaming\n#My Team : Black Coder Crush\nimport marshal\nexec(marshal.loads(' + str(nl) + '))')
                        ns.close()
                        cout += 1
                    else:
                        break

                mx = open(out).read()
                nl = base64.b32encode(mx)
                xn = open(out, 'w')
                xn.write("#Compile By Mr.Gaming\n#My Team : Black Coder Crush\nimport base64\nexec(base64.b32decode('%s'))\n" % nl)
                xn.close()
                print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % out
                raw_input('%s[%s\xe2\x9d\x97%s] %sBack %s\xe2\x9e\xa4 %s' % (b, m, b, gr, i, cg))
                main()
            else:
                print '%s[%s+%s] %sCout Terlalu Besar \xe2\x9d\x97' % (b, m, b, gr)
                waktu(0.8)
                main()
        elif chos == '3':
            os.system('clear')
            print logo
            print '         \x1b[37m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n         \x1b[37m\xe2\x95\x91       \x1b[33;1m\xe2\x9c\xa4 \x1b[32mCompile Marshal \x1b[33;1m\xe2\x9c\xa4\n         \x1b[37m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
            file = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            cot = int(50)
            if cot < 400:
                out = file.replace('.py', '') + '_enc.py'
                oa = open(file).read()
                ni = compile(oa, '<Goblok>', 'exec')
                bo = marshal.dumps(ni)
                ab = repr(bo)
                s = open(out, 'w')
                s.write('#Compile By Mr.Gaming\n#My Team : Black Coder Crush\nimport marshal\nexec(marshal.loads(' + str(ab) + '))')
                s.close()
                while True:
                    if cot >= cout:
                        nz = open(out).read()
                        dn = compile(nz, '<Goblok>', 'exec')
                        bx = marshal.dumps(dn)
                        nl = repr(bx)
                        ns = open(out, 'w')
                        ns.write('#Compile By Mr.Gaming\n#My Team : Black Coder Crush\nimport marshal\nexec(marshal.loads(' + str(nl) + '))')
                        ns.close()
                        cout += 1
                    else:
                        break

                mx = open(out).read()
                nl = base64.b32encode(mx)
                xn = open(out, 'w')
                xn.write("#Compile By Mr.Gaming\n#My Team : Black Coder Crush\nimport base64\nexec(base64.b32decode('%s'))\n" % nl)
                xn.close()
                py_compile.compile(out)
                print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % out
                os.system('rm ' + out)
                raw_input('%s[%s\xe2\x9d\x97%s] %sBack %s\xe2\x9e\xa4 %s' % (b, m, b, gr, i, cg))
                main()
        elif chos == '4':
            os.system('clear')
            print logo
            print '         \x1b[37m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n         \x1b[37m\xe2\x95\x91       \x1b[33;1m\xe2\x9c\xa4 \x1b[32mCompile Marshal \x1b[33;1m\xe2\x9c\xa4\n         \x1b[37m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
            file = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            out = file.replace('.py', '') + '_enc.py'
            oa = open(file).read()
            u = []
            c = []
            for x in oa:
                u.append(ord(x))

            for a in u:
                c.append('n' * a)

            fi = ('d={}\nexec("".join([chr(len(i)) for i in d]))').format(c)
            og = open(out, 'w')
            og.write(fi)
            og.close()
            oa = open(out).read()
            cot = int(50)
            ni = compile(oa, '<Goblok>', 'exec')
            bo = marshal.dumps(ni)
            ab = repr(bo)
            s = open(out, 'w')
            s.write('#Compile By Mr.Gaming\n#My Team : Black Coder Crush\nimport marshal\nexec(marshal.loads(' + str(ab) + '))')
            s.close()
            while True:
                if cot >= cout:
                    nz = open(out).read()
                    dn = compile(nz, '<Goblok>', 'exec')
                    bx = marshal.dumps(dn)
                    nl = repr(bx)
                    ns = open(out, 'w')
                    ns.write('#Compile By Mr.Gaming\n#My Team : Black Coder Crush\nimport marshal\nexec(marshal.loads(' + str(nl) + '))')
                    ns.close()
                    cout += 1
                else:
                    break

            mx = open(out).read()
            nl = base64.b32encode(mx)
            xn = open(out, 'w')
            xn.write("#Compile By Mr.Gaming\n#My Team : Black Coder Crush\nimport base64\nexec(base64.b32decode('%s'))\n" % nl)
            xn.close()
            op = open(out).read()
            g = []
            d = []
            for c in op:
                g.append(ord(c))

            for o in g:
                d.append('x' * o)

            fi = ('d={}\nexec("".join([chr(len(i)) for i in d]))').format(d)
            og = open(out, 'w')
            og.write(fi)
            og.close()
            py_compile.compile(out)
            print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % out
            os.system('rm ' + out)
            raw_input('%s[%s\xe2\x9d\x97%s] %sBack %s\xe2\x9e\xa4 %s' % (b, m, b, gr, i, cg))
            main()
        elif chos == '5':
            os.system('clear')
            print logo
            print '         \x1b[37m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n         \x1b[37m\xe2\x95\x91       \x1b[33;1m\xe2\x9c\xa4 \x1b[32mCompile Marshal \x1b[33;1m\xe2\x9c\xa4\n         \x1b[37m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
            ia = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            a = open(ia).read()
            z = []
            u = []
            for x in a:
                z.append(ord(x))

            for c in z:
                u.append(zlib.compress(str(c)))

            o = []
            for p in u:
                o.append(marshal.dumps(p))

            fip = ('import marshal;import zlib\nd={}\nexec("".join([chr(int(zlib.decompress(marshal.loads(i)))) for i in d]))').format(o)
            js = ia.replace('.py', '_enc.py')
            ox = open(js, 'w')
            ox.write(fip)
            ox.close()
            p = []
            n = []
            gn = open(js).read()
            for l in gn:
                p.append(ord(l))

            for b in p:
                n.append('x' * b)

            fin = ('d={}\nexec("".join([chr(len(i)) for i in d]))').format(n)
            bp = open(js, 'w')
            bp.write(fin)
            bp.close()
            bx = open(js).read()
            xs = binascii.hexlify(bx)
            fc = ('exec ("{}").decode("hex")').format(xs)
            nk = open(js, 'w')
            nk.write(fc)
            nk.close()
            py_compile.compile(js)
            os.system('rm ' + js)
            print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%s \x1b[32m] \x1b[37m!' % js
            raw_input('[!] Back \xe2\x9e\xa4 %s' % i)
            main()
        elif chos == '6':
            os.system('clear')
            print logo
            print '         \x1b[37m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n         \x1b[37m\xe2\x95\x91       \x1b[33;1m\xe2\x9c\xa4 \x1b[32mCompile Marshal \x1b[33;1m\xe2\x9c\xa4\n         \x1b[37m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
            ia = raw_input('%s[%s\xe2\x9b\xa5%s] %sFile >> %s' % (b, i, b, gr, i))
            bc = open(ia).read()
            xs = binascii.hexlify(bc)
            js = ia.replace('.py', '_enc.py')
            fc = ('exec ("{}").decode("hex")').format(xs)
            nk = open(js, 'w')
            nk.write(fc)
            nk.close()
            p = []
            n = []
            gn = open(js).read()
            for l in gn:
                p.append(ord(l))

            for b in p:
                n.append('x' * b)

            fin = ('d={}\nexec("".join([chr(len(i)) for i in d]))').format(n)
            bp = open(js, 'w')
            bp.write(fin)
            bp.close()
            py_compile.compile(js)
            os.system('rm ' + js)
            print '\x1b[34m[\x1b[31m!\x1b[34m] \x1b[37mDone Di Simpan \x1b[32m[ \x1b[37m%sc \x1b[32m] \x1b[37m!' % js
            raw_input('[!] Back \xe2\x9e\xa4 %s' % i)
            main()
        elif chos == 'e' or chos == 'E':
            sys.exit()
        else:
            print '%s[%s!%s] %sWrong Input !' % (b, m, b, gr)
            waktu(0.5)
            main()
    except KeyboardInterrupt:
        print '%s[%s!%s] %sCtrl+C not Working Pliss ctr+d !' % (b, m, b, gr)
        waktu(0.5)
        main()
    except EOFError:
        sys.exit()
    except IOError:
        print '%s[%s\xe2\x9d\x97%s] %sFile Tidak Di Temukan !' % (b, m, b, gr)
        waktu(0.5)
        main()
    except ValueError:
        print '%s[%s!%s] %sCout Berupa Angka ! ' % (b, m, b, gr)


main()
# global ba ## Warning: Unused global
# global k ## Warning: Unused global
# global pb ## Warning: Unused global
# global pu ## Warning: Unused global
