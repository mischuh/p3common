import common.validators as validate


def strings(value):
    print(validate.is_str(value))


def main():
    strings(123)


if __name__ == '__main__':
    main()
