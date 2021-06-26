import requests


url = "https://static.cingulo.com/bi/user_activities.json"
response_data = requests.get(url)
data_users = response_data.json()

# Variáveis de Janeiro
jan_01 = 0
jan_02 = 0
jan_03 = 0
jan_04 = 0
jan_05 = 0
jan_06 = 0
jan_07 = 0
jan_08 = 0
jan_09 = 0
jan_10 = 0
jan_11 = 0
jan_12 = 0
jan_13 = 0
jan_14 = 0
jan_15 = 0
jan_16 = 0
jan_17 = 0
jan_18 = 0
jan_19 = 0
jan_20 = 0
jan_21 = 0
jan_22 = 0
jan_23 = 0
jan_24 = 0
jan_25 = 0
jan_26 = 0
jan_27 = 0
jan_28 = 0
jan_29 = 0
jan_30 = 0
jan_31 = 0

# Variáveis de fevereiro
fev_01 = 0
fev_02 = 0
fev_03 = 0
fev_04 = 0
fev_05 = 0
fev_06 = 0
fev_07 = 0
fev_08 = 0
fev_09 = 0
fev_10 = 0
fev_11 = 0
fev_12 = 0
fev_13 = 0
fev_14 = 0
fev_15 = 0
fev_16 = 0
fev_17 = 0
fev_18 = 0
fev_19 = 0
fev_20 = 0
fev_21 = 0
fev_22 = 0
fev_23 = 0
fev_24 = 0
fev_25 = 0
fev_26 = 0
fev_27 = 0
fev_28 = 0

# Variáveis de Março


a = 0
b = 0
i = 0

for b in range(365):
    while i < 40:
        if data_users[i]['activities'][b] == 1:
            a += 1
        i += 1
    if b == 0:
        jan_01 = a
    elif b == 1:
        jan_02 = a
    elif b == 2:
        jan_03 = a
    elif b == 3:
        jan_04 = a
    elif b == 4:
        jan_05 = a
    elif b == 5:
        jan_06 = a
    elif b == 6:
        jan_07 = a
    elif b == 7:
        jan_08 = a
    elif b == 8:
        jan_09 = a
    elif b == 9:
        jan_10 = a
    elif b == 10:
        jan_11 = a
    elif b == 11:
        jan_12 = a
    elif b == 12:
        jan_13 = a
    elif b == 13:
        jan_14 = a
    elif b == 14:
        jan_15 = a
    elif b == 15:
        jan_16 = a
    elif b == 16:
        jan_17 = a
    elif b == 17:
        jan_18 = a
    elif b == 18:
        jan_19 = a
    elif b == 19:
        jan_20 = a
    elif b == 20:
        jan_21 = a
    elif b == 21:
        jan_22 = a
    elif b == 22:
        jan_23 = a
    elif b == 23:
        jan_24 = a
    elif b == 24:
        jan_25 = a
    elif b == 25:
        jan_26 = a
    elif b == 26:
        jan_27 = a
    elif b == 27:
        jan_28 = a
    elif b == 28:
        jan_29 = a
    elif b == 29:
        jan_30 = a
    elif b == 30:
        jan_31 = a

    i = 0
    a = 0
    b += 1
