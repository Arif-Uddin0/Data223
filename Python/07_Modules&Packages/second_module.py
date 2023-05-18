


def second_func():
    print('This is the second function being called')


def main():
    print(f'If this is the main module, this will be called')
    second_func()

if __name__ == '__main__':
    main()