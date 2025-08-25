from pprint import pprint
import textfsm

if __name__ == "__main__":
    with open("saps.txt") as f:
        hosts = f.read()

    with open("sapsTemplate.txt") as f:
        parser = textfsm.TextFSM(f)
    p = parser.ParseText(hosts)
    for x in p:
        print(f"{x[0]},{x[1]}")
