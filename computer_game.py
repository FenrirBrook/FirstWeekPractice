import random

while True:
    print("\033[1;33m" + "\n********ROCK, PAPER, SCISSORS GAME********\n" + "\033[0;m")
    print("\t1: \033[3;34m" + "Rock\n"+ "\033[0;m""\t2: \033[3;34m" + "Paper\n"+ "\033[0;m""\t3: \033[3;34m" + "Scissors\n"+ "\033[0;m")
    user_opcion = input("Choose an option: ")

    try:
        user_op = int(user_opcion)
        if user_op > 0 and user_op < 4:
            pc_option = random.choice([1,2,3])
            if user_op == pc_option:
                print("Draw")
            elif user_op == 1 and pc_option == 3:
                print("\033[3;32m" + "You win" + "\033[0;m", "Rock destroy scissors")
            elif user_op == 1 and pc_option == 2:
                print("\033[;31m" + "You lose" + "\033[0;m", "Paper wrap Rock")
            elif user_op == 2 and pc_option == 1:
                print("\033[3;32m" + "You win" + "\033[0;m", "Paper wrap Rock")
            elif user_op == 2 and pc_option == 3:
                print("\033[;31m" + "You lose" + "\033[0;m", "Scissors cut Paper")
            elif user_op == 3 and pc_option == 1:
                print("\033[;31m" + "You lose" + "\033[0;m", "Rock destroy scissors")
            elif user_op == 3 and pc_option == 2:
                print("\033[3;32m" + "You win" + "\033[0;m", "Scissors cut Paper")
        else:
            print('Enter a menu number')
    except:
        print("Enter a menu number")

    reset_game = input("\033[3;34m" + "Do you play again? (s/n): " + "\033[0;m")
    if reset_game.lower() != 's':
        break








# while True:
#     print("\n********ROCK, PAPER, SCISSORS GAME********\n")
#     print("1: Rock\n 2: Paper\n3: Scissors")
#     user_opcion = input("Choose an option: ")

#     try:
#         user_op = int(user_opcion)
#         if user_op > 0 and user_op < 4:
#             pc_option = random.choice([1,2,3])
#             if user_op == pc_option:
#                 print("Draw")
#             elif user_op == 1 and pc_option == 3:
#                 print("You win, Rock destroy scissors")
#             elif user_op == 1 and pc_option == 2:
#                 print("You lose, Paper wrap Rock")
#             elif user_op == 2 and pc_option == 1:
#                 print("You win, Paper wrap Rock")
#             elif user_op == 2 and pc_option == 3:
#                 print("You lose, Scissors cut Paper")
#             elif user_op == 3 and pc_option == 1:
#                 print("You lose", "Rock destroy scissors")
#             elif user_op == 3 and pc_option == 2:
#                 print("You win, Scissors cut Paper")
#         else:
#             print('Enter a menu number')
#     except:
#         print("Enter a menu number")

#     reset_game = input("Do you play again? (s/n): ")
#     if reset_game.lower() != 's':
#         break