from item import Item, exact, heuristic_1, heuristic_2, read_csv
import time

def main():
    item_list = read_csv('velo_1.csv')

    C = [0.6, 0.8, 1, 1.5, 2, 3, 4, 5, 6]

    print("Running exact algorithm")

    for i in [0.6, 0.8, 1]:
        print("Running algo for C = ", i)

        start = time.time()
        total_mass, total_utility, best_item = exact(item_list, i)
        end = time.time()
        print("     ", end - start)

        print("     ", "total mass : ", total_mass / 100, "total utility : ", total_utility / 100, "\n")
        for i in best_item:
            print("     ", i)

    print("Heuristic 2 algorithm")

    for i in C:
        print("Running algo for C = ", i)

        total_mass, total_utility, best_item = heuristic_1(item_list, i)

        print("     ", "total mass : ", total_mass / 100, "total utility : ", total_utility / 100, "\n")
        for i in best_item:
            print("     ", i)

        time_moy = 0
        n = 1000
        for i in range(n):
            start = time.time()
            heuristic_1(item_list, i)
            time_moy += time.time() - start

        print("     ", time_moy / n, "\n")

    print("Heuristic 2 algorithm")

    for i in C:
        print("Running algo for C = ", i)

        total_mass, total_utility, best_item = heuristic_2(item_list, i)

        print("     ", "total mass : ", total_mass / 100, "total utility : ", total_utility / 100, "\n")
        for i in best_item:
            print("     ", i)

        time_moy = 0
        n = 1000
        for i in range(n):
            start = time.time()
            heuristic_2(item_list, i)
            time_moy += time.time() - start

        print("     ", time_moy / n, "\n")


if __name__ == '__main__':
    main()
