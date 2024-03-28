import os


from dotenv import load_dotenv

load_dotenv()

print(os.getenv('TELEGRAM_TOKEN'))


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
