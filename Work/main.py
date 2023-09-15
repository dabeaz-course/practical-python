
import pcost
import sys
if __name__ == '__main__':
    file_name = input("Enter the file name:")
    file_sys_name = sys.argv[1]

cost = pcost.portfolio_cost(file_name)
print("\n file:",file_name, " Cost:",cost)

cost = pcost.portfolio_cost(file_sys_name)
print("\n file:",file_sys_name, " Cost:",cost)
