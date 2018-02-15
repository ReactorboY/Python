import sys, time

def mainLoop():
    while 1:
        print("Hussain")

if __name__ == '__main__':
    try:
        mainLoop()
    except KeyboardInterrupt:
         print( sys.stderr, "\n exited by user request")
         sys.exit(0)
