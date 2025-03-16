from randomuser import RandomUser
import pandas as pd
r=RandomUser()
some_list=r.generate_users(10)
name=r.get_full_name()
try :
 for user in some_list:
    print(user.get_full_name(),'',user.get_email())
    print(user.get_picture())
except Exception as e:
 print(e)
def getuser():
    users=[]
    for user in RandomUser.generate_users(10):
        users.append({'Name':user.get_full_name(),'Gender':user.get_gender(),'City':user.get_city(),'DOB':user.get_dob()})
    return pd.DataFrame(users)
df=getuser()
print(df.info())
print(df)