#_________3 variables:___________
BITS_C = 18  #2^18 expects upto 2e5
BITS_B = 18  
#A can be any number of bits,pray that its all<64
SHIFT_B = BITS_C
SHIFT_A = BITS_C + BITS_B
MASK_C = (1 << BITS_C) - 1
MASK_B = (1 << BITS_B) - 1
pack = lambda a, b, c: (a << SHIFT_A) | (b << SHIFT_B) | c
unpack = lambda p: (p >> SHIFT_A, (p >> SHIFT_B) & MASK_B, p & MASK_C)

#_________2 variables:___________
BITS_B = 18  
MASK_B = (1 << BITS_B) - 1
pack = lambda a, b: (a << BITS_B) | b
unpack = lambda p: (p >> BITS_B, p & MASK_B)

'''
make the size as small as possible
pretty much will not work if >64
Usage example:
# Packing into the heap
heapq.heappush(pq, pack(a ,b ,c))
# Unpacking from the heap
a, b, c= unpack(heapq.heappop(pq))
really didn't have to make ts into a template but whatever
'''
