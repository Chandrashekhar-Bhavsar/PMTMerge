

arrY = [["START", "IN PROGRESS", "REVIEW", "DONE"],
        ["REVIEW", "RESOLVED", "DONE"],
        ["DONE", "RE-OPENED", "RE-ASSIGN", "IN PROGRESS"],
        ["DONE", "COMPLETED"]]

for sublist in arrY:
    pairs = zip(sublist, sublist[1:])
    for pair in pairs:
        print(pair)
        current_state=pair[0]
        next_state=pair[1]
        print("current state",current_state)
        print("next_state",next_state)