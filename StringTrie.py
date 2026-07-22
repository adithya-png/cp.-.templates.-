# Adjust MAX_STR_NODES based on the sum of lengths of all strings in a testcase + 5
MAX_STR_NODES = 1000005 

# 26 lists of size MAX_STR_NODES
ch_str = [[0] * MAX_STR_NODES for _ in range(26)]
cnt_str = [0] * MAX_STR_NODES
end_str = [0] * MAX_STR_NODES
cn_str = 1

def init_string_trie():
    global cn_str
    for i in range(cn_str):
        cnt_str[i] = 0
        end_str[i] = 0
        for c in range(26):
            ch_str[c][i] = 0
    cn_str = 1

def insert_str(s: str):
    global cn_str
    cur = 0
    cnt_str[cur] += 1
    
    for char in s:
        idx = ord(char) - 97
        if ch_str[idx][cur] == 0:
            ch_str[idx][cur] = cn_str
            cn_str += 1
        cur = ch_str[idx][cur]
        cnt_str[cur] += 1
        
    end_str[cur] += 1

def exists_str(s: str) -> bool:
    cur = 0
    for char in s:
        idx = ord(char) - 97
        if ch_str[idx][cur] == 0:
            return False
        cur = ch_str[idx][cur]
    return end_str[cur] > 0

def remove_str(s: str):
    # Only call if 's' is guaranteed to exist
    cur = 0
    cnt_str[cur] -= 1
    
    for char in s:
        idx = ord(char) - 97
        cur = ch_str[idx][cur]
        cnt_str[cur] -= 1
        
    end_str[cur] -= 1

def count_prefix(p: str) -> int:
    cur = 0
    for char in p:
        idx = ord(char) - 97
        if ch_str[idx][cur] == 0:
            return 0
        cur = ch_str[idx][cur]
    return cnt_str[cur]

def count_words(s: str) -> int:
    cur = 0
    for char in s:
        idx = ord(char) - 97
        if ch_str[idx][cur] == 0:
            return 0
        cur = ch_str[idx][cur]
    return end_str[cur]