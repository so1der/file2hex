import binascii

print("Enter convert mode:\n1) File to Hex\n2) Hex to File")
convert_mode = input()


def makeHex():
    input_file = input('Enter name of the file to be converted(with file extension): ')
    output_file = input('Enter name for new file(without .hex): ')
    with open(input_file, 'rb') as f:
        binary = f.read()
    hex_bytes = binascii.hexlify(binary)
    hexa_str = hex_bytes.decode('utf-8')
    with open(f"{output_file}.hex", "a") as f:
        f.write(hexa_str)
    print(f"Done, {output_file}.hex from {input_file} was created!")


def makeBin():
    input_file = input('Enter name of the file to be converted(without .hex): ')
    output_file = input('Enter name for new file(with file extension): ')
    with open(f"{input_file}.hex", 'r') as f:
        hexadecimal = f.read()
    bin_bytes = binascii.unhexlify(hexadecimal)
    with open(output_file, "wb") as f:
        f.write(bin_bytes)
    print(f"Done, {output_file} from {input_file}.hex was created!")


if __name__ == '__main__':
    try:
        match convert_mode:
            case "1" | "1)" | "File to Hex":
                makeHex()
            case "2" | "2)" | "Hex to File":
                makeBin()
            case _:
                print("Wrong convert mode!")
    except FileNotFoundError:
        print("Input file not found")
    input()
