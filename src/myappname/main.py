import sys


def runapp(param):
    if len(param) != 2:
        print('\nInsert one param')
    else:
        print('\nParam correct')


if __name__ == '__main__':
    runapp(sys.argv)
