from months import Months

group1 = set()
group2 = set()
union = set()

def main() -> None:
    for i in range(3):
        group1.add(input(f"Enter birth month {i + 1}: ".format(i)))
    for i in range(3):
        group2.add(input(f"Enter birth month {i + 1}: ".format(i)))
    print(group1)
    print(group2)

def isBirthMonth() -> bool:
    pass

if __name__ == "__main__":
    main()