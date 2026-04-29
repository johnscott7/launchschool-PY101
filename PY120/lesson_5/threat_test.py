INITIAL_MARKER = " "
HUMAN_MARKER = "X"
COMPUTER_MARKER = "O"

POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of board
        (4, 5, 6),  # center row of board
        (7, 8, 9),  # bottom row of board
        (1, 4, 7),  # left column of board
        (2, 5, 8),  # middle column of board
        (3, 6, 9),  # right column of board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7),  # diagonal: top-right to bottom-left
    )

dict_test = {1: " ", 2: " ", 3: "X", 4: "O", 5: " ", 6: "O", 7: "X", 8: "", 9:""}

def locate_threat():
    for row in POSSIBLE_WINNING_ROWS:
        row_total = 0
        for num in row:
            if dict_test[num] == COMPUTER_MARKER:
                break
            elif dict_test[num] == HUMAN_MARKER:
                row_total += 1
            elif dict_test[num] == INITIAL_MARKER:
                threat_location = num
            if row_total == 2:
                print(threat_location)
                # return threat_location
        print('Fail')
    
locate_threat()