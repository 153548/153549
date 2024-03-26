with open('26-145.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.strip().split())) for i in file.readlines()]
    m, k_low = data[0]
    vagon_high, vagon_low = m, m
    k_high = k_low
    data.pop(0)
print(sorted(data, reverse=True))
train = [[8, 8, 0] for _ in range(24)]
print(train)
detishki = 0
for i in data:
    if 4 >= i[0] > 2:
        for j in range(24):
            if train[j][0] > 0:
                train[j][0] -= 1
                train[j][2] += 4 - i[0]
                detishki += i[1]
                break
    elif 2 >= i[0] > 0:
        for j in range(24):
            if train[j][1] > 0:
                train[j][1] -= 1
                train[j][2] += 2 - i[0]
                detishki += i[1]
                break
print(train, detishki)





