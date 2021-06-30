# C:/Users/delen/Pictures/Cyberpunk 2077
import os


def main():
    i = 0
    path = "C:/Users/delen/Pictures/Cyberpunk 2077/"  # import path
    for filename in os.listdir(path):   # using a forloop loop through renaming
        my_dest = "img" + str(i) + ".png"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1


if __name__ == '__main__':  # make sure when the program is running the main is called
    main()
