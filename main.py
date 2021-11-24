while True:
    try:
        numEnts = int(input())
        ents = []
        pos = []
        f = []
        for x in range(numEnts):
            ents.append(int(input()))
        s = int(input())
        for k, v in enumerate(ents[::-1]):
            if k % s == 0:
               pos.append(v)
        total = sum(pos)
        #array = [i for i in range(1, total + 1) if total % i == 0]
        for x in range(1, total  + 1):
            if total % x == 0:
                f.append(x)    
        if len(f) == 2:
            print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')
    except EOFError:
        break