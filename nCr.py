MOD = 10**9 + 7
MAXN = 2 * 10**5 + 5

fact = [1] * MAXN
invfact = [1] * MAXN
for i in range(1, MAXN):
    fact[i] = (fact[i - 1] * i) % MOD
invfact[-1] = pow(fact[-1], MOD - 2, MOD)
for i in range(MAXN - 2, -1, -1):
    invfact[i] = (invfact[i + 1] * (i + 1)) % MOD
def ncr(n, r, _fact=fact, _invfact=invfact, _mod=MOD):
    if r < 0 or r > n:
        return 0
    return _fact[n] * _invfact[r] % _mod * _invfact[n - r] % _mod