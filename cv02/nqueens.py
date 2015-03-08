import os
CESTA_K_MINISAT = "..\\tools\\win\\minisat.exe"
class NQueens:
    def q(self,r,s):
        return r*self.n+s+1
    def zapis_problem(self,subor):
        for i in range(self.n):
            for j in range(self.n):
                subor.write("{} ".format(self.q(i,j)))
            subor.write("0\n")
        for r in range(self.n):
            for i in range(self.n):
                for j in range(i+1,self.n):
                    subor.write("{} {} 0\n".format(-self.q(r,i),-self.q(r,j)))
        for s in range(self.n):
            for i in range(self.n):
                for j in range(i+1,self.n):
                    subor.write("{} {} 0\n".format(-self.q(i,s),-self.q(j,s)))
                
    def dekoduj_riesenie(self,ries):
        ret=[]
        for c in [int(x) for x in ries.split()]:
            if c>0:
                r=(c-1)//self.n
                s=(c-1)%self.n
                ret.append((r,s))
        return ret
    def solve(self,n):
        self.n=n
        with open("vstup.txt", "w") as self.o:
            self.zapis_problem(self.o)
        os.system("{} vstup.txt vystup.txt".format(CESTA_K_MINISAT))
        try:
            with open("vystup.txt", "r") as i:
                sat = i.readline()
                if sat == "SAT\n":
                    ries = i.readline()
                    return self.dekoduj_riesenie(ries)
                else:
                    return []
        except IOError as e:
            print("Chyba pri nacitavani vystupneho suboru ({0}): {1}".format(
                    e.errno, e.strerror))
            return 1
