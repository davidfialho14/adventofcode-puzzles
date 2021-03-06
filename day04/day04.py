from typing import Iterator


def is_passphrase_valid(passphrase: str, transform) -> bool:
    words = passphrase.split(' ')
    distinct_words = set(transform(word) for word in words)
    return len(words) == len(distinct_words)


def check_passphrases(passphrases: Iterator[str], transform=lambda word: word) -> int:
    return sum(1 for passphrase in passphrases if is_passphrase_valid(passphrase, transform))


def input(path: str) -> Iterator[str]:
    with open(path) as file:
        for line in file:
            yield line.strip()


def main() -> None:
    print("Solution part 1:", check_passphrases(input("input.txt")))
    print("Solution part 2:", check_passphrases(input("input.txt"), lambda word: str(sorted(word))))


if __name__ == '__main__':
    main()
