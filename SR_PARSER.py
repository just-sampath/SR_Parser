class SR_Parser:
    def __init__(self):
        self.r1 = {}
        self.start = ""

    def getproduction(self):
        k = input("Please Enter the production rules : \n")
        while k:
            if "|" in k:
                v = k.split("->")
                l = v[1].split("|")
                self.r1[l[0]] = v[0]
                self.r1[l[1]] = v[0]
            else:
                v = k.split("->")
                self.r1[v[1]] = v[0]
            k = input()
        for i, j in self.r1.items():
            self.start = j

    @staticmethod
    def dissect(li, ma):
        kl = []
        for i in range(len(li)):
            if li[i:i + len(ma)] == ma:
                kl.append(ma)
                li = li.replace(ma, "-" * len(ma), 1)
            else:
                kl.append(li[i])
        i = 1
        while "-" * i in kl:
            while "-" * i in kl:
                kl.remove("-" * i)
            i += 1
        return kl

    def showtable(self):
        st = input("Please Enter the string : ")
        stack = ""
        ma = ""
        for i in self.r1.keys():
            if len(i) > len(ma) and i.isalpha():
                ma = i
        handle = self.dissect(st, ma)
        i = 0
        print("Stack\t|\tInput\t|\tAction")
        print("        |               |             ")
        print(stack, "   \t", st, "\t", "")
        temp = ""
        while True:
            if handle:
                temp = handle.pop()
            i += 1
            st = "".join(handle)
            if temp in self.r1.keys():
                print(stack + temp, "\t", st, "\t   ", "SHIFT")
                print("        |               |             ")
                stack += self.r1[temp]
                print(stack, "\t", st, "\t   ", "REDUCTION")
                print("        |               |             ")
            else:
                stack += temp
                print(stack, "    \t", st, "\t\t", "SHIFT")
                print("        |               |             ")
            if stack in self.r1.keys():
                stack = self.r1[stack]
                print(stack, "\t", st, "\t\t", "REDUCTION")
                print("        |               |             ")
            if (not handle) and stack != self.start:
                print(stack, "  \t", st, "  \t", "ERROR")
                print("        |               |             ")
                break
            if (not handle) and stack == self.start:
                print(stack, "  \t", st, "  \t\t", "ACCEPTED")
                print("        |               |             ")
                break

    def solve(self):
        self.getproduction()
        self.showtable()


n = SR_Parser()
n.solve()
