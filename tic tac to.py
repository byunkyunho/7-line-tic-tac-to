import os
ttt_list = [" "," "," "," "," "," "," "," "," "]
def main(player):
    ttt_list[int(input("\nChoose player {} number 1 ~ 9 >>>".format(player))) - 1] = player
    print("\n{}\nI {} I {} I {} I\n{}\nI {} I {} I {} I\n{}\nI {} I {} I {} I\n{}".format("-"*14, ttt_list[0], ttt_list[1],ttt_list[2],"-"*14,ttt_list[3],ttt_list[4],ttt_list[5],"-"*14,ttt_list[6],ttt_list[7],ttt_list[8],"-"*14))
    if ttt_list[0] == player and ttt_list[0] == ttt_list[4] and ttt_list[4] == ttt_list[8] or ttt_list[0] == player and ttt_list[0] == ttt_list[1] and ttt_list[1] == ttt_list[2] or ttt_list[3] == player and ttt_list[3] == ttt_list[4] and ttt_list[4] == ttt_list[5] or ttt_list[6] == player and ttt_list[6] == ttt_list[7] and ttt_list[7] == ttt_list[8] or  ttt_list[2] == player and ttt_list[2] == ttt_list[4] and ttt_list[2] == ttt_list[6] or ttt_list[0] == player and ttt_list[0] == ttt_list[3] and ttt_list[3] == ttt_list[6] or ttt_list[1] == player and ttt_list[1] == ttt_list[4] and ttt_list[4] == ttt_list[7] or ttt_list[2] == player and ttt_list[2] == ttt_list[5] and ttt_list[5] == ttt_list[8]:
        print("\nPlayer {} Win!\n".format(player))
        os._exit(1)
while True:
    main("O")
    main("X")