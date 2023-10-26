def fast_exponentiation_algorithm(a, n, m):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        p = 1
        ak = a
        i = n
        print(f"ak    i    s    p")
        while i > 0:
            s = i % 2
            if s == 1:
                p = p * ak % m
            ak = ak * ak % m
            i = (i-s) / 2
            print(f"{ak}    {i}    {s}    {p}")
        return p

print(f"p = {fast_exponentiation_algorithm(12, 233761, 355207)}")

def euqlid(n, m):
    while n!=0 and m !=0:
        if(n>m):
            n %= m
        else:
            m %= n
    return n+m

print(euqlid(233761, 355207))