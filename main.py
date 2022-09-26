import hashlib


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def read_file(filename: str, step: int = 3) -> list:
    hashes = []

    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

        for idx in range(0, len(lines)-2, step):
            hashes.append(dict(phrase=lines[idx].strip('\n'),
                               sha256=lines[idx + 1].strip('\n'),
                               md5=lines[idx + 2].strip('\n')))

    return hashes


def main():
    test_cases = read_file(f"hashes.txt")

    for test_case in test_cases:
        print(f"test subject: {test_case['phrase']}")

        sha256_hash = hashlib.sha256(test_case["phrase"].encode()).hexdigest()
        sha256_valid = True if sha256_hash == test_case["sha256"] else False
        print(f"expected sha256: \t{test_case['sha256']}")
        print(f"actual sha256: \t\t{sha256_hash}")

        md5_hash = hashlib.md5(test_case["phrase"].encode()).hexdigest()
        md5_valid = True if md5_hash == test_case["md5"] else False
        print(f"expected md5: \t\t{test_case['md5']}")
        print(f"actual md5: \t\t{md5_hash}")

        print(f"SHA256: {sha256_valid}\nMD5:\t{md5_valid}")
        result = f"{BColors.OKGREEN}YES{BColors.ENDC}" if sha256_valid is True and md5_valid is True else f"{BColors.FAIL}NO{BColors.ENDC}"
        print(f"VALID? ", end="")
        print(f"\t{result}")
        print()


if __name__ == "__main__":
    main()
