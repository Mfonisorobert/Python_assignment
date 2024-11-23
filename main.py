# main.py

import pset1
import pset2
import pset3
import pset4

def run_pset1():
    print("PSet 1: Todo List\n")
    print("Todos for Monday:", pset1.get_todos_for_day("Monday"))
    print("\nAll Todos:")
    pset1.display_all_todos()

def run_pset2():
    print("\nPSet 2: Bio Info Dictionary")
    print(pset2.bio_info)

def run_pset3():
    print("\nPSet 3: Looping Through Bio Info")
    pset3.print_bio_info(pset2.bio_info)

def run_pset4():
    print("\nPSet 4: Doubling Items in List (1-50)")
    print(pset4.doubled_numbers)

if __name__ == "__main__":
    run_pset1()
    run_pset2()
    run_pset3()
    run_pset4()
