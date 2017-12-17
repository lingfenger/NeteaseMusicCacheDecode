import os
import sys

CODE = 0xA3


def decode(origin_filepath, result_filepath):
    try:
        fin = open(origin_filepath, "rb")
    except IOError as e:
        print(str(e))
        return

    try:
        fout = open(result_filepath, "wb")
    except IOError as e:
        print(str(e))
        return

    music = fin.read()
    print("Source file length: %s" % len(music))
    music_decode = bytearray()
    for i, byte in enumerate(music):
        print("\rProgress: %d%%" % (round((i + 1) * 100 / len(music)))),
        music_decode.append(int(byte.encode('hex'), 16) ^ CODE)

    fout.write(music_decode)
    fin.close()
    fout.close()


if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage python nemusiccd.py <source> [<destination>]")
        print("If destination is not specified, its name is same as souce.")
    elif len(sys.argv) == 2:
        last_sep = sys.argv[1].rfind(os.path.sep)
        source_path = sys.argv[1][:last_sep + 1]
        dest = sys.argv[1][:last_sep + sys.argv[1][last_sep:].find(".")] + ".mp3"
        print("Source: %s\nDestination: %s" % (sys.argv[1], dest))
        decode(sys.argv[1], dest)
    else:
        print("Source: %s\nDestination: %s" % (sys.argv[1], sys.argv[2]))
        decode(sys.argv[1], sys.argv[2])
