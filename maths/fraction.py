class Fraction(object):
    def __init__(self, val):
        self.val = float(val)
        self.numer, self.denom = self.val.as_integer_ratio()

    def limit_denom(self, max_denom):

        from numeric import gcd
        numer, denom = self.val.as_integer_ratio()
        numer = int(numer * (max_denom // float(denom)))
        denom = max_denom
        _gcd = gcd(numer, denom)

        self.numer = numer // _gcd
        self.denom = denom // _gcd 
        return self

    @property
    def numerator(self):
        return self.numer

    @property
    def denominator(self):
        return self.denom
