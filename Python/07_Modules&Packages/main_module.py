import second_module


print(f'for this module __name__ will be {__name__}')

def main():
    print('main() is called')

if __name__ == '__main__':
    main()

print(f'Second module __name__ will be {second_module.__name__}')