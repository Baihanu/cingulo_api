import requests
from cinguloapi.activities.models import UserActivity, JanuaryDailyActivity


url = "https://static.cingulo.com/bi/user_activities.json"
response_data = requests.get(url)
data_users = response_data.json()

user_activity = UserActivity()
januarydailyactivity = JanuaryDailyActivity()


class RegisterUserActivity:

    user_activity.user_id = data_users[1]['id']
    user_activity.activities = data_users[1]['activities']
    user_activity.save()


class RegisterJanuaryDailyUserActivity:

    januarydailyactivity.user_id = data_users[0]['id']
    januarydailyactivity.day_01 = data_users[0]['activities'][0]
    januarydailyactivity.day_02 = data_users[0]['activities'][1]
    januarydailyactivity.day_03 = data_users[0]['activities'][2]
    januarydailyactivity.day_04 = data_users[0]['activities'][3]
    januarydailyactivity.day_05 = data_users[0]['activities'][4]
    januarydailyactivity.day_06 = data_users[0]['activities'][5]
    januarydailyactivity.day_07 = data_users[0]['activities'][6]
    januarydailyactivity.day_08 = data_users[0]['activities'][7]
    januarydailyactivity.day_09 = data_users[0]['activities'][8]
    januarydailyactivity.day_10 = data_users[0]['activities'][9]
    januarydailyactivity.day_11 = data_users[0]['activities'][10]
    januarydailyactivity.day_12 = data_users[0]['activities'][11]
    januarydailyactivity.day_13 = data_users[0]['activities'][12]
    januarydailyactivity.day_14 = data_users[0]['activities'][13]
    januarydailyactivity.day_15 = data_users[0]['activities'][14]
    januarydailyactivity.day_16 = data_users[0]['activities'][15]
    januarydailyactivity.day_17 = data_users[0]['activities'][16]
    januarydailyactivity.day_18 = data_users[0]['activities'][17]
    januarydailyactivity.day_19 = data_users[0]['activities'][18]
    januarydailyactivity.day_20 = data_users[0]['activities'][19]
    januarydailyactivity.day_21 = data_users[0]['activities'][20]
    januarydailyactivity.day_22 = data_users[0]['activities'][21]
    januarydailyactivity.day_23 = data_users[0]['activities'][22]
    januarydailyactivity.day_24 = data_users[0]['activities'][23]
    januarydailyactivity.day_25 = data_users[0]['activities'][24]
    januarydailyactivity.day_26 = data_users[0]['activities'][25]
    januarydailyactivity.day_27 = data_users[0]['activities'][26]
    januarydailyactivity.day_28 = data_users[0]['activities'][27]
    januarydailyactivity.day_29 = data_users[0]['activities'][28]
    januarydailyactivity.day_30 = data_users[0]['activities'][29]
    januarydailyactivity.day_31 = data_users[0]['activities'][30]
    januarydailyactivity.save()


#    janeiro = user['activities'][0:31]
#    fevereiro = user['activities'][31:59]
#    marco = user['activities'][59:90]
#    abril = user['activities'][90:120]
#    maio = user['activities'][120:151]
#    junho = user['activities'][151:181]
#    julho = user['activities'][181:212]
#    agosto = user['activities'][212:243]
#    setembro = user['activities'][243:273]
#    outubro = user['activities'][273:304]
#    novembro = user['activities'][304:334]
#    dezembro = user['activities'][334:365]
