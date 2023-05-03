def voting(n):
    input_vote = []
    n = int(input('Jumlah vote: '))
    for i in range(n):
        vt = input('Masukkan vote: ')
        input_vote.append(vt)

    input_vote = 0
    for vote in voting:
        if vote in input_vote:
            input_vote[vote] += 1
        else:
            input_vote[vote] = 1
    pemenang = None
    batas_vote = 0
    for calon, votes in input_vote.items():
        if votes > batas_vote and votes >len(input_vote) / 2:
            batas_vote = votes
            pemenang = calon
    if pemenang:
        print(pemenang)
    else:
        print('None')
