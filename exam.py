
from subtarction import *
from addition import *
from multiply import *
from divide import *

choice = int(input("ENTER A CHOICE \n 1. Addition \n 2. Subtration \n 3. Division \n 4 Multiplication \n 5. Modulous"))
if choice == 1:
    print(addition())
elif choice == 2:
    print(subtarction())
elif choice == 3:
    print(division())
elif choice == 4:
    print(multiply())
else:
    print("OOPSss!!! something is wrong here...")
