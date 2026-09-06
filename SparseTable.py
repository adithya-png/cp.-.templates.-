# Read input
n = int(input())
arr = list(map(int, input().split()))

# --- BUILD ---
st = [arr]
for k in range(n.bit_length() - 1):
    i = 1 << k
    st.append([min(st[-1][j], st[-1][j + i]) for j in range(len(st[-1]) - i)])

# --- QUERY ---
def query(l, r):
    length = r - l + 1
    k = length.bit_length() - 1
    return min(st[k][l], st[k][r - (1 << k) + 1])

# Process queries
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())  # 0-indexed, inclusive [l, r]
    print(query(l, r))