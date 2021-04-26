class Calcule:
    def consecutive(self, l):
        n_arr = []
        i, n = 0, 0
        for i in range(len(l)-1):
            if l[i] == l[i + 1]:
                n += 1
            else:
                n_arr.append(n)
                n = 0
        return max(n_arr) + 1
    
    def suma(self, n):            
        s = 0
        i = 1
        while n > 0:
            n -= i if i%2 == 1 else 1
            s += i**2 if i%2 == 1 else i
            i += 1
        if n < 0:
            s -= -n*(i - 1)
        return s
