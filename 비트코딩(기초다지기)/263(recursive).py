def possible_sequences(n, m):
    if n == 1:
        if 1 <= m <= 6:
            return [[m]]
        else:
            return []
    else: #(n>1)
        sequences = []
        for i in range(1, 7):
            if m - i < 1:
                break
            for seq in possible_sequences(n - 1, m - i):
                sequences.append([i] + seq)
        return sequences

print(possible_sequences(3,7))