import sys

def main(args):
    input, output = args
    with open(input, 'rb') as f:
        data = list(f.read())
    data = data[0x09:]

    result = []

    i = 0
    while i < len(data):
        bank = i // 0x4000
        offset = i % 0x4000
        if bank != 0:
            offset += 0x4000

        d = data[i]

        if (d & 0x01) != 0x00:
            if (d & 0x08) != 0x00:
                result.append(f'{bank:02x}:{offset:04x} Call_{bank:02x}_{offset:04x}')
            if (d & 0x04) != 0x00:
                result.append(f'{bank:02x}:{offset:04x} Jump_{bank:02x}_{offset:04x}')
            d = 0x01
            data[i] = d

        j = i
        while data[j] == d:
            if j + 1 == len(data):
                break
            if (j + 1) % 0x4000 == 0:
                break
            j += 1
        length = j - i + 1
        i += length

        if d == 0x01:
            type = 'code'
        else:
            type = 'data'

        result.append(f'{bank:02x}:{offset:04x} .{type}:{length:04x}')

    result = '\n'.join(result) + '\n'

    with open(output, 'w') as f:
        f.write(result)

    return 0

if __name__ == '__main__':
    main(sys.argv[1:])
