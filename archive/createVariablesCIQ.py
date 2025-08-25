import openpyxl
import re
import json


if __name__ == '__main__':
    ciq_file = "tablaCIQ.xlsx"
    var_file = "configVariablesPre.xlsx"

    wb = openpyxl.load_workbook(ciq_file, data_only=True)

    # vprnInternet
    vprnContent = {}
    vprnContent["vprnInt"] = [wb['vprns']['b1'].value, wb['vprns']['b2'].value, wb['vprns']['b3'].value,
                                wb['vprns']['b10'].value.split("\n"),
                                [[x, "blackhole", "no shutdown"] for x in wb['vprns']['b11'].value.split("\n")],
                                wb['vprns']['b12'].value.split("\n"),
                                wb['vprns']['b5'].value, wb['vprns']['b6'].value,
                                wb['vprns']['b8'].value, wb['vprns']['b7'].value, wb['vprns']['b9'].value]
    wb['services']['b16'].value = json.dumps(vprnContent)

    # vprnWhole
    vprnContent = {}
    subscribersW = json.loads(wb['vprns']['c13'].value)
    vprnContent["vprnWhol"] = [wb['vprns']['c1'].value, wb['vprns']['c2'].value, wb['vprns']['c3'].value,
                                json.loads(wb['vprns']['c13'].value),
                                wb['vprns']['c10'].value.split("\n"),
                                wb['vprns']['c5'].value, wb['vprns']['c6'].value,
                                wb['vprns']['c8'].value, wb['vprns']['c7'].value, wb['vprns']['c9'].value,
                                wb['vprns']['c4'].value]
    wb['services']['b17'].value = json.dumps(vprnContent)

    start = 15
    inc = 0
    for s in subscribersW:
        subscribersW[s] = json.loads(wb['vprns']['c' + str(start + inc)].value)
        inc += 2
    wb['services']['b18'].value = json.dumps(subscribersW)

    # vprnRetail
    col = ['d', 'e', 'f', 'g', 'h']
    vprn = ""
    vprnContent = {}
    for i in col:
        vprnContent[wb["vprns"][i + "1"].value] = []
        vprnContent[wb["vprns"][i + "1"].value].append(wb["vprns"][i + "2"].value)
        vprnContent[wb["vprns"][i + "1"].value].append(wb["vprns"][i + "3"].value)
        vprnContent[wb["vprns"][i + "1"].value].append(json.loads(wb["vprns"][i + "13"].value))
        vprnContent[wb["vprns"][i + "1"].value].append(json.loads(wb["vprns"][i + "10"].value))
        vprnContent[wb["vprns"][i + "1"].value].append(wb["vprns"][i + "5"].value)
        vprnContent[wb["vprns"][i + "1"].value].append(wb["vprns"][i + "6"].value)
        vprnContent[wb["vprns"][i + "1"].value].append(wb["vprns"][i + "8"].value)
        vprnContent[wb["vprns"][i + "1"].value].append(wb["vprns"][i + "7"].value)
        vprnContent[wb["vprns"][i + "1"].value].append(wb["vprns"][i + "9"].value)
        vprnContent[wb["vprns"][i + "1"].value] += wb["vprns"][i + "11"].value.split("\n")
    wb['services']['b19'].value = json.dumps(vprnContent)

    # Saps
    x = {}
    for c in ['C', 'F']:
        x[wb["saps"][c + "1"].value] = []
        for cell in wb['saps'][c]:
            if cell.value != wb["saps"][c + "1"].value and cell.value:
                x[wb["saps"][c + "1"].value].append(cell.value)
    content = json.dumps(x)
    wb['services']['b20'].value = content
    subscribersInterfacesR = {}
    keys = 13
    prefixes, prefixes6 = {}, {}
    for c in ['D', 'E', 'F', 'G', 'h']:
        inc = 2
        vprn = wb["vprns"][c+'1'].value
        subsInts = json.loads(wb["vprns"][c+str(keys)].value)
        name4 = "IPv4_" + str(vprn)
        prefixes[name4] = []
        name6 = "IPv6_" + str(vprn)
        prefixes6[name6] = []
        for value in subsInts:
            v = json.loads(wb["vprns"][c+str(keys+inc)].value)
            inc += 2
            subsInts[value] = v
            prefixes[name4] += [[x.replace("1/", "0/"), 'exact'] for x in v[1]]
            prefixes[name4].append([v[2] + "/32", "exact"])
            prefixes6[name6] += [[re.sub(r"\s+.*$", "", x), "exact"] for x in v[7] if x != ""]
            prefixes6[name6].append([v[8] + "/128", "exact"])
        row = 1
        for c in wb['additionalPrefixes']['A']:
            name = wb['additionalPrefixes']['A'+str(row)].value
            value = wb['additionalPrefixes']['B' + str(row)].value
            prefixes[name] = [[x, 'exact'] for x in value.split("\n") if x != ""]
            row += 1
        prefixes.update(prefixes6)
        subscribersInterfacesR.update(subsInts)
    wb['services']['b21'].value = json.dumps(subscribersInterfacesR)
    # Prefixes
    prefixes["default_IPv4"] = [["0.0.0.0/0", "exact"]]
    prefixes["default_IPv6"] = [["::/0", "exact"]]
    wb['services']['b22'].value = json.dumps(prefixes)

    # Policy Statements
    content = {}
    for c in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        content[wb['policyStatement'][c+'1'].value] = json.loads(wb['policyStatement'][c+'2'].value)
    wb['services']['b23'].value = json.dumps(content)

    # Hosts
    content = {}
    for c in wb["hosts"]["L"]:
        print(c.value)
        if c.value != "JSON":
            content.update(json.loads(c.value))
    wb['services']['b25'].value = json.dumps(content)
    print(f"Saving {var_file}")
    wb.save(var_file)



