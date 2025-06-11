from fractions import gcd


class Fraction:

    def __init__(self,top,bottom):
        self.num = top
        self.deno = bottom

    def show(self):
        print(self.num ,"/", self.deno)

    def __str__(self):
        return str(self.num)+"/"+str(self.deno)

    def __add__(self, otherfunction):
        newnum = self.num*otherfunction.deno + self.deno*otherfunction.num
        newdeno = self.deno*otherfunction.deno
        common = gcd(newnum,newdeno)
        return Fraction(newnum//common,newdeno//common)

    def __eq__(self, otherfraction):
        num1 = self.num*otherfraction.deno
        num2 = self.deno*otherfraction.num

        return num1==num2

f1 = Fraction(3,5)
f2 = Fraction(4,8)
f3 = f1+f2
print(f1.__eq__(f2))
print(f3)
