import sys

KEY = '891001agij-178thta-hj-yqqiqq0-uqiqy12-s-jhgjgkf23-ush-1223-vaba'.encode()

if len(sys.argv) < 3:
    print('Usage: encrypt.py <src> <dst>')
    sys.exit(1)

src, dst = sys.argv[1], sys.argv[2]

src_file = open(src, 'r', encoding='utf-8')
src_data = src_file.read()
src_file.close()

dst_data = bytearray()

idx = 0
for i in range(len(src_data)):
    ch = ord(src_data[i])

    for j in chr(ch + KEY[idx]).encode():
        dst_data.append(j)

    idx += 1
    if idx >= len(KEY):
        idx = 0

print(dst_data)

with open(dst, 'wb') as dst_file:
    dst_file.write(dst_data)
