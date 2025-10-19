def test(cuvant, text):
    print(f"---{cuvant.__name__} | {text}---")


def main():
    cuvant = input()
    text = input()
    test(cuvant, text)

if __name__ == '__main__':
    main()