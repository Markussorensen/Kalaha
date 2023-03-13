import copy

def MaxStonesInPit(board, player, valid_moves):
    # Sorts the valid moves so that it looks at moves which have highest count of stones first
    # This is a heuristic that is used to determine the best move to make
    num_stones = []
    for move in valid_moves:
        num_stones.append(board.get_num_stones(player, move))
    sorted_moves = [x for _, x in sorted(zip(num_stones, valid_moves), reverse=True)]
    return sorted_moves

def StonesInHouse(board, player, valid_moves):
    # Sorts the valid moves so that it looks at moves which results in the highest number of stones in the house first
    stones_in_house = []
    for move in valid_moves:
        new_board = copy.deepcopy(board)
        new_board.make_move(player, move)
        stones_in_house.append(new_board.get_kalaha(player))
    sorted_moves = [x for _, x in sorted(zip(stones_in_house, valid_moves), reverse=True)]
    return sorted_moves

def MovesEndInKalaha(board, player, valid_moves):
    # Sorts the valid moves so that it looks at moves which results in ending in own Kalaha first
    moves_end_in_kalaha = []
    for move in valid_moves:
        new_board = copy.deepcopy(board)
        new_board.make_move(player, move)
        if new_board.player_turn == player:
            moves_end_in_kalaha.append(1)
        else:
            moves_end_in_kalaha.append(0)
    sorted_moves = [x for _, x in sorted(zip(moves_end_in_kalaha, valid_moves), reverse=True)]
    return sorted_moves
