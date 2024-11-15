from months import Months

group1 = set()
group2 = set()
self = set()
union = set()

def main() -> None:
    i = 0
    l = 0
    while i < 3:
        month = input(f"Enter birth month {i+1}: ".format(i))
        if not (is_birth_month(month)):
            print("Invalid birth month. Please try again!")
            continue
        group1.add(month)
        i += 1
    while l < 3:
        month = input(f"Enter birth month {l+1}: ".format(l))
        if not (is_birth_month(month)):
            print("Invalid birth month. Please try again!")
            continue
        group2.add(month)
        l += 1
    print(group1)
    print(group2)
    self.add(input(f"Enter your birth month: "))
    calculate_set()
    if self.issubset(union):
        print("You have the same birth month with one of your classmates.")
    else:
        print("You don't have the same birth month with any of your classmates.")

def calculate_set() -> None:
    union = str(group1 | group2)
    print("Union: " + union)
    print("Intersection: " + str(group1 & group2))
    print("Difference: " + str(group1 - group2))

def is_birth_month(userMonth) -> bool:
    for month in Months.months:
        if (userMonth == month):
            return True
    return False

if __name__ == "__main__":
    main()