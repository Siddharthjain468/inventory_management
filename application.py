import pandas as pd
from src.items import Items
from src.create_pass_and_user import create_user_pass
from src.password_checker import checker

while True:
    a = pd.read_csv('secrets_csv.csv')
    if a.empty:
        print('No user are present')
    print('1 Create user\n2 login')
    n = input()
    bol = False
    if n == '1':
        create_user_pass()
        break
    elif n == '2':
        print('enter user name: ')
        usr = input()
        b = checker(usr)
        break
    else:
        break

# create_user_pass(input('enter user name:'))



# item1 = Items("1001", "Logitech Mouse", "Electronics", 10)
# print(item1)