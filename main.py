def table(data, title):
    count, index = 0, 0
    res, lens = [], []
    for i in data:
        if data.index(i) == 0:
            i.insert(0, "id")
        else:
            i.insert(0, " " + str(count))
        count += 1
    for arr in data:
        res.append([str(sum(len(i) for i in arr)), f"{data.index(arr)}"])
    for i in res:
        lens.append(int(i[0]))
    top_bottom = max(lens)
    for i in res:
        if str(top_bottom) in i:
            index = int(i[1])
    top_bottom += int(top_bottom/2)
    print(f'{int(top_bottom / 2 - len(title)) * " "}' + title)
    print(top_bottom * "=")
    for i in range(len(data[0])):
        spaces = len(data[index][i]) - len(data[0][i])
        print("|  " + "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(96, 238, 243, data[0][i]),
              end=f'{(spaces + 1) * " "}')
    print("  |" + "\n" + top_bottom * "=")
    for j in range(1, len(data)):
        for i in range(len(data[j])):
            spaces = len(data[index][i]) - len(data[j][i])
            item = data[j][i] if len(data[j][i]) > len(data[0][i]) else data[j][i] + (len(data[0][i]) - len(data[j][i])-1) * " "
            print("|  " + item, end=f'{(spaces + 2) * " "}')
        print("  |" + "\n" + top_bottom * "-")
    return "\n "


print(table(
    [
        ['name', 'phone', 'email'],
        ['Hedayat Farahi', '07xxxxxxxx', 'hedayatxxxxxxx@gmail.com'],
    ], "Data"
))
