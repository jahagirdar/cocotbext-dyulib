class ReadMemHex:
    def __init__(self, filename, interface, numbytes=4):
        with open(filename, 'r') as file:
            print(f"reading {filename}")
            while (line := file.readline()):
                words = line.split(' ')
                print(words.pop(0))
                if words[0][0] == '@':
                    address = words[0][1:]
                else:
                    interface.write(address, words)

                print(line.split(' '))

        pass


if __name__ == "__main__":
    ReadMemHex("ram.hex")
