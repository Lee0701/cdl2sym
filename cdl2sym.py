import sys

def main(args):
    input, output = args
    with open(input, 'rb') as f:
        data = list(f.read())

    result = []

    for i, d in enumerate(data):
        bank = i // 0x4000
        offset = i % 0x4000
        if bank != 0:
            offset += 0x4000

        if d == 0x09:
            type = 'code'
        elif d == 0x01:
            type = 'code'
        else:
            type = 'data'
        length = 1
        result.append(f'{bank:02x}:{offset:04x} .{type}:{length:04x}')

    result = '\n'.join(result) + '\n'

    with open(output, 'w') as f:
        f.write(result)

    return 0

if __name__ == '__main__':
    main(sys.argv[1:])
