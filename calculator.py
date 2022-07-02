# dont steal my code ffs
def start():

    print("welcome to calculator \n")
    def posible_stuff():
        print("heres a list of supported commands \n"
            "A) add \n"
            "B) subtract \n"
            "C) multiply \n"
            "D) divide \n"
            "help) as the na,e suggests, help command is to get help \n"
        )

    def manual():
        print(
            "this is a lightweight calculator which works offline \n"
            "the cool part is it does not even require installation \n"
        )
        posible_stuff()

    posible_stuff()
    to_do = input("plz select a option ? \n ")
    num_1 = int(input("enter num1  "))
    num_2 = int(input("enter num2  "))
    if to_do == "A" or to_do == "a":
        #num_3_for_a = num_2 + num_1
        #print(num_3_for_a)
        print(int(num_1 + num_2))
    elif to_do == "B" or to_do == "b":
        num_3 = num_1 - num_2
        #print("(num 2 - num 1")
        print(num_3)
    elif to_do == "C" or to_do == "c":
        num_3 = num_1 * num_2
        print(num_3)
    elif to_do == "D" or to_do == "d":
        num_3 = num_1 / num_2
        #print("(num 2 / num 1")
        print(num_3)
    if to_do == "help":
        manual()

start()

def restart_and_exit():
    print("do you want to restart ? \n")
    restart = input("y/n \n")
    if restart == "y":
        start()
    if restart == "n":
        print("okay, exiting.....")
        print("end of program")
        exit()

restart_and_exit()

xyz_pro_plus = 1

while (xyz_pro_plus < 2):
    restart_and_exit()

