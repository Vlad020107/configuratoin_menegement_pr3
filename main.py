import csv
import argparse

class main:
    def __init__(self):
        self.params = self.parse()
        self.print_params()

    def parse(self):
        parser = argparse.ArgumentParser(
            description="Учебная виртуальная машина"
        )
        parser.add_argument(
            "--source_parse",
            '-s',
            type=str,
            required=True,
            help="Путь к исходному файлу с текстом программы."
        )
        parser.add_argument(
            "--binary_parse",
            '-b',
            type=str,
            required=True,
            help="Путь к двоичному файлу-результату."
        )
        parser.add_argument(
            "--test_mode",
            '-t',
            type=bool,
            required=True,
            help="Режим тестирования."
        )

        args = parser.parse_args()

        params ={
            "source": args.source_parse,
            "binary": args.binary_parse,
            "test": args.test_mode
        }
        return params

    def print_params(self):
        print("Параметры конфигурации\n")
        print("=======================")
        print(f"Путь к исходному файлу с тестом программы: \t{self.params['source']}")
        print("-----------------------")
        print(f"Путь к двоичному файлу-результату: \t{self.params['binary']}")
        print("-----------------------")
        print(f"Режим тестирования \t{self.params['test']}")
        print("-----------------------")

if __name__ == '__main__':
    mymMain = main()
