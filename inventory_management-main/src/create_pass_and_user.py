import pandas as pd
class create_user_pass():
    def __init__():
        counter  = False
        file = {'user_name':'','password':''}
        a = pd.read_csv('secrets_csv.csv')
        # print(a)
        while True:
            user = input()
            if user in a['user_name'].values:
                print('user already exists')
                break
            if user == '':
                break
            if file['user_name'] in file:
                print('User already exists')
            else:
                counter = True
                file['user_name'] = user
                password = input()
                file['password'] = password
        
        if counter == True:
            df = pd.DataFrame(file, index = [0])
            df.to_csv('secrets_csv.csv', mode='a', index=False, header=False)
            # print(pd.read_csv("secrets_csv.csv"))
        else:
            print('no data')
          

