prices = [105, 110, 108, 112, 115, 116, 114]
i = 0
while i < len(prices) - 2:
    avg = sum(prices[i:i+3]) / 3
    print(avg)
    i = i + 1

