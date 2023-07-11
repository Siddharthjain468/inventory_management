import pandas as pd
class checker():
    
    def __init__(self,use):
        self.user_n = use
        self.user_pass = None
        self.bol = False
        a = pd.read_csv('secrets_csv.csv')
        # user_pass = input('Password')

        if self.user_n in a['user_name'].values:
            print('Enter password: ')
            self.user_pass = input()
            self.count = True
            inde = pd.Index(a['user_name']).get_loc(self.user_n)
            # print(a._get_value(inde, 'password'))
            if a['password'].iloc[inde] == self.user_pass:
                self.bol = True
                print('Correct password')
            else:
                print('Wrong password')
        else:
            print('Invalid user')

            
        # return True
        # password = 'Pass123'
        # i=0
        # while i<3:
        #     in_pass = input('Inputed password the password\n(h/H/hint)\n (exit/escape to exit)')
        #     in_pass = str(in_pass)
        #     in_pass = in_pass.lower()
        #     # print('entered pass = ',in_pass)
        #     if in_pass == 'h' or in_pass == 'hint':
        #         print("pas123")
        #         continue
        #     elif in_pass == 'exit' or in_pass == 'escape':
        #         break
        #     elif password == in_pass:
        #         print('Correct pass')
        #         break
        #     else:
        #         print('wrong pass (' + str(2-i) + ' attempts left)')