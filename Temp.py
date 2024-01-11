def gameWinner(colors):
    while True:
        wm = None
        for i in range(1, len(colors) - 1):
            if colors[i] == 'w' and colors[i - 1] == 'w' and colors[i + 1] == 'w':
                wm = i
                break

        if wm is not None:
            colors = colors[:wm] + colors[wm + 1:]
        else:
            return 'bob'  

        bm = None
        for i in range(1, len(colors) - 1):
            if colors[i] == 'b' and colors[i - 1] == 'b' and colors[i + 1] == 'b':
                bm = i
                break

        if bm is not None:
            colors = colors[:bm] + colors[bm + 1:]
        else:
            return 'wendy'  
