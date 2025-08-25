from pprint import pprint
if __name__ == "__main__":
    with open('prefix.txt') as f:
        file = f.readlines()
    p = {}
    for l in file:
        if l.endswith("exit\n"):
            continue
        if l.endswith('"\n'):
            pName = l.split(" ")[-1][:-1].replace('"','')
            p[pName] = []
        else:
            parts = l.split(" ")
            p[pName].append([parts[-2], parts[-1][:-1]])

    pprint(p)

