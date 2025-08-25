from pprint import pprint
import textfsm

if __name__ == "__main__":
    with open("hosts.txt") as f:
        hosts = f.read()

    with open("hostsTemplate1.txt") as f:
        parser = textfsm.TextFSM(f)
    p = parser.ParseText(hosts)
    text = "{\n"
    for i in p:
        x = "\", \"".join(i[1:])
        text += f'"{i[0]}": [' + f'"{x}"],\n'
    print(f"{text}\n"+"}")
    for i in p:
        print(i)
