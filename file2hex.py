import binascii

input_file = input('Enter name of the file to be converted: ')
output_file = input('Enter name for hex file (without .hex): ')

def makeHex(input_file, output_file):
    with open(input_file, 'rb') as f:
        binary = f.read()
    hex_bytes = binascii.hexlify(binary)
    hexa_str = hex_bytes.decode('utf-8')
    f = open(f"{output_file}.hex", "a")
    f.write(hexa_str)
    f.close()
    print(f"Done, {output_file}.hex was created!")

if __name__ == '__main__':
    makeHex(input_file, output_file)
    input()