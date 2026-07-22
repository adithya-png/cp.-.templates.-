# N numbers * 30 bits + buffer
MAX_BIT_NODES = 3000005 
MAX_BITS = 30
ch_bit = [[0] * MAX_BIT_NODES for _ in range(2)]
cnt_bit = [0] * MAX_BIT_NODES
cn_bit = 1

def init_bit_trie():
    global cn_bit
    for i in range(cn_bit):
        cnt_bit[i] = 0
        ch_bit[0][i] = 0
        ch_bit[1][i] = 0
    cn_bit = 1

def insert_bit(num: int):
    global cn_bit
    cur = 0
    cnt_bit[cur] += 1
    
    for i in range(MAX_BITS, -1, -1):
        bit = (num >> i) & 1
        
        if ch_bit[bit][cur] == 0:
            ch_bit[bit][cur] = cn_bit
            cn_bit += 1
            
        cur = ch_bit[bit][cur]
        cnt_bit[cur] += 1

def remove_bit(num: int):
    # Only call if 'num' is guaranteed to exist
    cur = 0
    cnt_bit[cur] -= 1
    
    for i in range(MAX_BITS, -1, -1):
        bit = (num >> i) & 1
        cur = ch_bit[bit][cur]
        cnt_bit[cur] -= 1

def get_max_xor(num: int) -> int:
    if cnt_bit[0] == 0:
        return 0
        
    cur = 0
    max_xor = 0
    
    for i in range(MAX_BITS, -1, -1):
        bit = (num >> i) & 1
        opp = 1 - bit
        
        if ch_bit[opp][cur] != 0 and cnt_bit[ch_bit[opp][cur]] > 0:
            max_xor |= (1 << i)
            cur = ch_bit[opp][cur]
        else:
            cur = ch_bit[bit][cur]
            
    return max_xor