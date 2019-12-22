import os
import platform


# This will check the connection on the network and  will return a boolean accordingly
def pingingfunction(GetHost="google.com"):
    get_response = os.system("ping " + ("-n 1 " if platform.system().lower() == "windows" else "-c 1 ") + GetHost)
    if get_response == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(pingingfunction())
