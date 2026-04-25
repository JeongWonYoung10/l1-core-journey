def solution(keyinput, board):
    moves = {"up" : (0,1), "down" : (0,-1), "right" : (1,0), "left" : (-1,0)}
    x, y = 0, 0
    x_limit = board[0] // 2
    y_limit = board[1] // 2
    for key in keyinput:
        dx, dy = moves[key]
        if -x_limit <= x+dx <= x_limit and -y_limit <= y+dy <= y_limit:
            x += dx
            y += dy
    return [x, y]
        
