import re

class AnPlusB(object):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def seq(self, maxi):
        ret, m = [], self.b
        while m < maxi:
            ret.append(m)
            m += self.a
        return ret

    @staticmethod
    def parse(string):
        if re.match(r'(\d+n[+-]\d+)|(\d+[+-]\d+n)|(-?\d+n)', string):
            breakdown = [al for al in re.split('(\d+n?)|([+-])|\s*', string) if al is not None and len(al) > 0]
            da_b = filter(re.compile("^\d+$").match, breakdown)[0];
            if da_b is not None:
                b = int(da_b)
            a = int(filter(re.compile("^\d+n$").match, breakdown)[0][:-1])
            op = filter(re.compile("[+-]").match, breakdown)[0]
            if op == '-':
                if string.endswith('n'):
                    a *= -1
                else:
                    b *= -1
            return AnPlusB(a,b)
        else:
            raise SyntaxError('invalid an+b syntax: ' % string)
