import requests
import json


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
mar_01 = 0
mar_02 = 0
mar_03 = 0
mar_04 = 0
mar_05 = 0
mar_06 = 0
mar_07 = 0
mar_08 = 0
mar_09 = 0
mar_10 = 0
mar_11 = 0
mar_12 = 0
mar_13 = 0
mar_14 = 0
mar_15 = 0
mar_16 = 0
mar_17 = 0
mar_18 = 0
mar_19 = 0
mar_20 = 0
mar_21 = 0
mar_22 = 0
mar_23 = 0
mar_24 = 0
mar_25 = 0
mar_26 = 0
mar_27 = 0
mar_28 = 0
mar_29 = 0
mar_30 = 0
mar_31 = 0

# Variáveis de Abril
apr_01 = 0
apr_02 = 0
apr_03 = 0
apr_04 = 0
apr_05 = 0
apr_06 = 0
apr_07 = 0
apr_08 = 0
apr_09 = 0
apr_10 = 0
apr_11 = 0
apr_12 = 0
apr_13 = 0
apr_14 = 0
apr_15 = 0
apr_16 = 0
apr_17 = 0
apr_18 = 0
apr_19 = 0
apr_20 = 0
apr_21 = 0
apr_22 = 0
apr_23 = 0
apr_24 = 0
apr_25 = 0
apr_26 = 0
apr_27 = 0
apr_28 = 0
apr_29 = 0
apr_30 = 0

# Variáveis de Maio
may_01 = 0
may_02 = 0
may_03 = 0
may_04 = 0
may_05 = 0
may_06 = 0
may_07 = 0
may_08 = 0
may_09 = 0
may_10 = 0
may_11 = 0
may_12 = 0
may_13 = 0
may_14 = 0
may_15 = 0
may_16 = 0
may_17 = 0
may_18 = 0
may_19 = 0
may_20 = 0
may_21 = 0
may_22 = 0
may_23 = 0
may_24 = 0
may_25 = 0
may_26 = 0
may_27 = 0
may_28 = 0
may_29 = 0
may_30 = 0
may_31 = 0

# Variáveis de Junho
jun_01 = 0
jun_02 = 0
jun_03 = 0
jun_04 = 0
jun_05 = 0
jun_06 = 0
jun_07 = 0
jun_08 = 0
jun_09 = 0
jun_10 = 0
jun_11 = 0
jun_12 = 0
jun_13 = 0
jun_14 = 0
jun_15 = 0
jun_16 = 0
jun_17 = 0
jun_18 = 0
jun_19 = 0
jun_20 = 0
jun_21 = 0
jun_22 = 0
jun_23 = 0
jun_24 = 0
jun_25 = 0
jun_26 = 0
jun_27 = 0
jun_28 = 0
jun_29 = 0
jun_30 = 0

# Variáveis de Julho
jul_01 = 0
jul_02 = 0
jul_03 = 0
jul_04 = 0
jul_05 = 0
jul_06 = 0
jul_07 = 0
jul_08 = 0
jul_09 = 0
jul_10 = 0
jul_11 = 0
jul_12 = 0
jul_13 = 0
jul_14 = 0
jul_15 = 0
jul_16 = 0
jul_17 = 0
jul_18 = 0
jul_19 = 0
jul_20 = 0
jul_21 = 0
jul_22 = 0
jul_23 = 0
jul_24 = 0
jul_25 = 0
jul_26 = 0
jul_27 = 0
jul_28 = 0
jul_29 = 0
jul_30 = 0
jul_31 = 0

# Variáveis de Agosto
aug_01 = 0
aug_02 = 0
aug_03 = 0
aug_04 = 0
aug_05 = 0
aug_06 = 0
aug_07 = 0
aug_08 = 0
aug_09 = 0
aug_10 = 0
aug_11 = 0
aug_12 = 0
aug_13 = 0
aug_14 = 0
aug_15 = 0
aug_16 = 0
aug_17 = 0
aug_18 = 0
aug_19 = 0
aug_20 = 0
aug_21 = 0
aug_22 = 0
aug_23 = 0
aug_24 = 0
aug_25 = 0
aug_26 = 0
aug_27 = 0
aug_28 = 0
aug_29 = 0
aug_30 = 0
aug_31 = 0

# Variáveis de Setembro
sep_01 = 0
sep_02 = 0
sep_03 = 0
sep_04 = 0
sep_05 = 0
sep_06 = 0
sep_07 = 0
sep_08 = 0
sep_09 = 0
sep_10 = 0
sep_11 = 0
sep_12 = 0
sep_13 = 0
sep_14 = 0
sep_15 = 0
sep_16 = 0
sep_17 = 0
sep_18 = 0
sep_19 = 0
sep_20 = 0
sep_21 = 0
sep_22 = 0
sep_23 = 0
sep_24 = 0
sep_25 = 0
sep_26 = 0
sep_27 = 0
sep_28 = 0
sep_29 = 0
sep_30 = 0

# Variáveis de Outubro
oct_01 = 0
oct_02 = 0
oct_03 = 0
oct_04 = 0
oct_05 = 0
oct_06 = 0
oct_07 = 0
oct_08 = 0
oct_09 = 0
oct_10 = 0
oct_11 = 0
oct_12 = 0
oct_13 = 0
oct_14 = 0
oct_15 = 0
oct_16 = 0
oct_17 = 0
oct_18 = 0
oct_19 = 0
oct_20 = 0
oct_21 = 0
oct_22 = 0
oct_23 = 0
oct_24 = 0
oct_25 = 0
oct_26 = 0
oct_27 = 0
oct_28 = 0
oct_29 = 0
oct_30 = 0
oct_31 = 0

# Variáveis de Novembro
nov_01 = 0
nov_02 = 0
nov_03 = 0
nov_04 = 0
nov_05 = 0
nov_06 = 0
nov_07 = 0
nov_08 = 0
nov_09 = 0
nov_10 = 0
nov_11 = 0
nov_12 = 0
nov_13 = 0
nov_14 = 0
nov_15 = 0
nov_16 = 0
nov_17 = 0
nov_18 = 0
nov_19 = 0
nov_20 = 0
nov_21 = 0
nov_22 = 0
nov_23 = 0
nov_24 = 0
nov_25 = 0
nov_26 = 0
nov_27 = 0
nov_28 = 0
nov_29 = 0
nov_30 = 0

# Variáveis de Dezembro
dec_01 = 0
dec_02 = 0
dec_03 = 0
dec_04 = 0
dec_05 = 0
dec_06 = 0
dec_07 = 0
dec_08 = 0
dec_09 = 0
dec_10 = 0
dec_11 = 0
dec_12 = 0
dec_13 = 0
dec_14 = 0
dec_15 = 0
dec_16 = 0
dec_17 = 0
dec_18 = 0
dec_19 = 0
dec_20 = 0
dec_21 = 0
dec_22 = 0
dec_23 = 0
dec_24 = 0
dec_25 = 0
dec_26 = 0
dec_27 = 0
dec_28 = 0
dec_29 = 0
dec_30 = 0
dec_31 = 0


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
    elif b == 31:
        fev_01 = a
    elif b == 32:
        fev_02 = a
    elif b == 33:
        fev_03 = a
    elif b == 34:
        fev_04 = a
    elif b == 35:
        fev_05 = a
    elif b == 36:
        fev_06 = a
    elif b == 37:
        fev_07 = a
    elif b == 38:
        fev_08 = a
    elif b == 39:
        fev_09 = a
    elif b == 40:
        fev_10 = a
    elif b == 41:
        fev_11 = a
    elif b == 42:
        fev_12 = a
    elif b == 43:
        fev_13 = a
    elif b == 44:
        fev_14 = a
    elif b == 45:
        fev_15 = a
    elif b == 46:
        fev_16 = a
    elif b == 47:
        fev_17 = a
    elif b == 48:
        fev_18 = a
    elif b == 49:
        fev_19 = a
    elif b == 50:
        fev_20 = a
    elif b == 51:
        fev_21 = a
    elif b == 52:
        fev_22 = a
    elif b == 53:
        fev_23 = a
    elif b == 54:
        fev_24 = a
    elif b == 55:
        fev_25 = a
    elif b == 56:
        fev_26 = a
    elif b == 57:
        fev_27 = a
    elif b == 58:
        fev_28 = a
    elif b == 59:
        mar_01 = a
    elif b == 60:
        mar_02 = a
    elif b == 61:
        mar_03 = a
    elif b == 62:
        mar_04 = a
    elif b == 63:
        mar_05 = a
    elif b == 64:
        mar_06 = a
    elif b == 65:
        mar_07 = a
    elif b == 66:
        mar_08 = a
    elif b == 67:
        mar_09 = a
    elif b == 68:
        mar_10 = a
    elif b == 69:
        mar_11 = a
    elif b == 70:
        mar_12 = a
    elif b == 71:
        mar_13 = a
    elif b == 72:
        mar_14 = a
    elif b == 73:
        mar_15 = a
    elif b == 74:
        mar_16 = a
    elif b == 75:
        mar_17 = a
    elif b == 76:
        mar_18 = a
    elif b == 77:
        mar_19 = a
    elif b == 78:
        mar_20 = a
    elif b == 79:
        mar_21 = a
    elif b == 80:
        mar_22 = a
    elif b == 81:
        mar_23 = a
    elif b == 82:
        mar_24 = a
    elif b == 83:
        mar_25 = a
    elif b == 84:
        mar_26 = a
    elif b == 85:
        mar_27 = a
    elif b == 86:
        mar_28 = a
    elif b == 87:
        mar_29 = a
    elif b == 88:
        mar_30 = a
    elif b == 89:
        mar_31 = a
    elif b == 90:
        apr_01 = a
    elif b == 91:
        apr_02 = a
    elif b == 92:
        apr_03 = a
    elif b == 93:
        apr_04 = a
    elif b == 94:
        apr_05 = a
    elif b == 95:
        apr_06 = a
    elif b == 96:
        apr_07 = a
    elif b == 97:
        apr_08 = a
    elif b == 98:
        apr_09 = a
    elif b == 99:
        apr_10 = a
    elif b == 100:
        apr_11 = a
    elif b == 101:
        apr_12 = a
    elif b == 102:
        apr_13 = a
    elif b == 103:
        apr_14 = a
    elif b == 104:
        apr_15 = a
    elif b == 105:
        apr_16 = a
    elif b == 106:
        apr_17 = a
    elif b == 107:
        apr_18 = a
    elif b == 108:
        apr_19 = a
    elif b == 109:
        apr_20 = a
    elif b == 110:
        apr_21 = a
    elif b == 111:
        apr_22 = a
    elif b == 112:
        apr_23 = a
    elif b == 113:
        apr_24 = a
    elif b == 114:
        apr_25 = a
    elif b == 115:
        apr_26 = a
    elif b == 116:
        apr_27 = a
    elif b == 117:
        apr_28 = a
    elif b == 118:
        apr_29 = a
    elif b == 119:
        apr_30 = a
    elif b == 120:
        may_01 = a
    elif b == 121:
        may_02 = a
    elif b == 122:
        may_03 = a
    elif b == 123:
        may_04 = a
    elif b == 124:
        may_05 = a
    elif b == 125:
        may_06 = a
    elif b == 126:
        may_07 = a
    elif b == 127:
        may_08 = a
    elif b == 128:
        may_09 = a
    elif b == 129:
        may_10 = a
    elif b == 130:
        may_11 = a
    elif b == 131:
        may_12 = a
    elif b == 132:
        may_13 = a
    elif b == 133:
        may_14 = a
    elif b == 134:
        may_15 = a
    elif b == 135:
        may_16 = a
    elif b == 136:
        may_17 = a
    elif b == 137:
        may_18 = a
    elif b == 138:
        may_19 = a
    elif b == 139:
        may_20 = a
    elif b == 140:
        may_21 = a
    elif b == 141:
        may_22 = a
    elif b == 142:
        may_23 = a
    elif b == 143:
        may_24 = a
    elif b == 144:
        may_25 = a
    elif b == 145:
        may_26 = a
    elif b == 146:
        may_27 = a
    elif b == 147:
        may_28 = a
    elif b == 148:
        may_29 = a
    elif b == 149:
        may_30 = a
    elif b == 150:
        may_31 = a
    elif b == 151:
        jun_01 = a
    elif b == 152:
        jun_02 = a
    elif b == 153:
        jun_03 = a
    elif b == 154:
        jun_04 = a
    elif b == 155:
        jun_05 = a
    elif b == 156:
        jun_06 = a
    elif b == 157:
        jun_07 = a
    elif b == 158:
        jun_08 = a
    elif b == 159:
        jun_09 = a
    elif b == 160:
        jun_10 = a
    elif b == 161:
        jun_11 = a
    elif b == 162:
        jun_12 = a
    elif b == 163:
        jun_13 = a
    elif b == 164:
        jun_14 = a
    elif b == 165:
        jun_15 = a
    elif b == 166:
        jun_16 = a
    elif b == 167:
        jun_17 = a
    elif b == 168:
        jun_18 = a
    elif b == 169:
        jun_19 = a
    elif b == 170:
        jun_20 = a
    elif b == 171:
        jun_21 = a
    elif b == 172:
        jun_22 = a
    elif b == 173:
        jun_23 = a
    elif b == 174:
        jun_24 = a
    elif b == 175:
        jun_25 = a
    elif b == 176:
        jun_26 = a
    elif b == 177:
        jun_27 = a
    elif b == 178:
        jun_28 = a
    elif b == 179:
        jun_29 = a
    elif b == 180:
        jun_30 = a
    elif b == 181:
        jul_01 = a
    elif b == 182:
        jul_02 = a
    elif b == 183:
        jul_03 = a
    elif b == 184:
        jul_04 = a
    elif b == 185:
        jul_05 = a
    elif b == 186:
        jul_06 = a
    elif b == 187:
        jul_07 = a
    elif b == 188:
        jul_08 = a
    elif b == 189:
        jul_09 = a
    elif b == 190:
        jul_10 = a
    elif b == 191:
        jul_11 = a
    elif b == 192:
        jul_12 = a
    elif b == 193:
        jul_13 = a
    elif b == 194:
        jul_14 = a
    elif b == 195:
        jul_15 = a
    elif b == 196:
        jul_16 = a
    elif b == 197:
        jul_17 = a
    elif b == 198:
        jul_18 = a
    elif b == 199:
        jul_19 = a
    elif b == 200:
        jul_20 = a
    elif b == 201:
        jul_21 = a
    elif b == 202:
        jul_22 = a
    elif b == 203:
        jul_23 = a
    elif b == 204:
        jul_24 = a
    elif b == 205:
        jul_25 = a
    elif b == 206:
        jul_26 = a
    elif b == 207:
        jul_27 = a
    elif b == 208:
        jul_28 = a
    elif b == 209:
        jul_29 = a
    elif b == 210:
        jul_30 = a
    elif b == 211:
        jul_31 = a
    elif b == 212:
        aug_01 = a
    elif b == 213:
        aug_02 = a
    elif b == 214:
        aug_03 = a
    elif b == 215:
        aug_04 = a
    elif b == 216:
        aug_05 = a
    elif b == 217:
        aug_06 = a
    elif b == 218:
        aug_07 = a
    elif b == 219:
        aug_08 = a
    elif b == 220:
        aug_09 = a
    elif b == 221:
        aug_10 = a
    elif b == 222:
        aug_11 = a
    elif b == 223:
        aug_12 = a
    elif b == 224:
        aug_13 = a
    elif b == 225:
        aug_14 = a
    elif b == 226:
        aug_15 = a
    elif b == 227:
        aug_16 = a
    elif b == 228:
        aug_17 = a
    elif b == 229:
        aug_18 = a
    elif b == 230:
        aug_19 = a
    elif b == 231:
        aug_20 = a
    elif b == 232:
        aug_21 = a
    elif b == 233:
        aug_22 = a
    elif b == 234:
        aug_23 = a
    elif b == 235:
        aug_24 = a
    elif b == 236:
        aug_25 = a
    elif b == 237:
        aug_26 = a
    elif b == 238:
        aug_27 = a
    elif b == 239:
        aug_28 = a
    elif b == 240:
        aug_29 = a
    elif b == 241:
        aug_30 = a
    elif b == 242:
        aug_31 = a
    elif b == 243:
        sep_01 = a
    elif b == 244:
        sep_02 = a
    elif b == 245:
        sep_03 = a
    elif b == 246:
        sep_04 = a
    elif b == 247:
        sep_05 = a
    elif b == 248:
        sep_06 = a
    elif b == 249:
        sep_07 = a
    elif b == 250:
        sep_08 = a
    elif b == 251:
        sep_09 = a
    elif b == 252:
        sep_10 = a
    elif b == 253:
        sep_11 = a
    elif b == 254:
        sep_12 = a
    elif b == 255:
        sep_13 = a
    elif b == 256:
        sep_14 = a
    elif b == 257:
        sep_15 = a
    elif b == 258:
        sep_16 = a
    elif b == 259:
        sep_17 = a
    elif b == 260:
        sep_18 = a
    elif b == 261:
        sep_19 = a
    elif b == 262:
        sep_20 = a
    elif b == 263:
        sep_21 = a
    elif b == 264:
        sep_22 = a
    elif b == 265:
        sep_23 = a
    elif b == 266:
        sep_24 = a
    elif b == 267:
        sep_25 = a
    elif b == 268:
        sep_26 = a
    elif b == 269:
        sep_27 = a
    elif b == 270:
        sep_28 = a
    elif b == 271:
        sep_29 = a
    elif b == 272:
        sep_30 = a
    elif b == 273:
        oct_01 = a
    elif b == 274:
        oct_02 = a
    elif b == 275:
        oct_03 = a
    elif b == 276:
        oct_04 = a
    elif b == 277:
        oct_05 = a
    elif b == 278:
        oct_06 = a
    elif b == 279:
        oct_07 = a
    elif b == 280:
        oct_08 = a
    elif b == 281:
        oct_09 = a
    elif b == 282:
        oct_10 = a
    elif b == 283:
        oct_11 = a
    elif b == 284:
        oct_12 = a
    elif b == 285:
        oct_13 = a
    elif b == 286:
        oct_14 = a
    elif b == 287:
        oct_15 = a
    elif b == 288:
        oct_16 = a
    elif b == 289:
        oct_17 = a
    elif b == 290:
        oct_18 = a
    elif b == 291:
        oct_19 = a
    elif b == 292:
        oct_20 = a
    elif b == 293:
        oct_21 = a
    elif b == 294:
        oct_22 = a
    elif b == 295:
        oct_23 = a
    elif b == 296:
        oct_24 = a
    elif b == 297:
        oct_25 = a
    elif b == 298:
        oct_26 = a
    elif b == 299:
        oct_27 = a
    elif b == 300:
        oct_28 = a
    elif b == 301:
        oct_29 = a
    elif b == 302:
        oct_30 = a
    elif b == 303:
        oct_31 = a
    elif b == 304:
        nov_01 = a
    elif b == 305:
        nov_02 = a
    elif b == 306:
        nov_03 = a
    elif b == 307:
        nov_04 = a
    elif b == 308:
        nov_05 = a
    elif b == 309:
        nov_06 = a
    elif b == 310:
        nov_07 = a
    elif b == 311:
        nov_08 = a
    elif b == 312:
        nov_09 = a
    elif b == 313:
        nov_10 = a
    elif b == 314:
        nov_11 = a
    elif b == 315:
        nov_12 = a
    elif b == 316:
        nov_13 = a
    elif b == 317:
        nov_14 = a
    elif b == 318:
        nov_15 = a
    elif b == 319:
        nov_16 = a
    elif b == 320:
        nov_17 = a
    elif b == 321:
        nov_18 = a
    elif b == 322:
        nov_19 = a
    elif b == 323:
        nov_20 = a
    elif b == 324:
        nov_21 = a
    elif b == 325:
        nov_22 = a
    elif b == 326:
        nov_23 = a
    elif b == 327:
        nov_24 = a
    elif b == 328:
        nov_25 = a
    elif b == 329:
        nov_26 = a
    elif b == 330:
        nov_27 = a
    elif b == 331:
        nov_28 = a
    elif b == 332:
        nov_29 = a
    elif b == 333:
        nov_30 = a
    elif b == 334:
        dec_01 = a
    elif b == 335:
        dec_02 = a
    elif b == 336:
        dec_03 = a
    elif b == 337:
        dec_04 = a
    elif b == 338:
        dec_05 = a
    elif b == 339:
        dec_06 = a
    elif b == 340:
        dec_07 = a
    elif b == 341:
        dec_08 = a
    elif b == 342:
        dec_09 = a
    elif b == 343:
        dec_10 = a
    elif b == 344:
        dec_11 = a
    elif b == 345:
        dec_12 = a
    elif b == 346:
        dec_13 = a
    elif b == 347:
        dec_14 = a
    elif b == 348:
        dec_15 = a
    elif b == 349:
        dec_16 = a
    elif b == 350:
        dec_17 = a
    elif b == 351:
        dec_18 = a
    elif b == 352:
        dec_19 = a
    elif b == 353:
        dec_20 = a
    elif b == 354:
        dec_21 = a
    elif b == 355:
        dec_22 = a
    elif b == 356:
        dec_23 = a
    elif b == 357:
        dec_24 = a
    elif b == 358:
        dec_25 = a
    elif b == 359:
        dec_26 = a
    elif b == 360:
        dec_27 = a
    elif b == 361:
        dec_28 = a
    elif b == 362:
        dec_29 = a
    elif b == 363:
        dec_30 = a
    elif b == 364:
        dec_31 = a

    i = 0
    a = 0
    b += 1

jan_data = {'Dia 01': jan_01, 'Dia 02': jan_02, 'Dia 03': jan_03, 'Dia 04': jan_04, 'Dia 05': jan_05, 'Dia 06': jan_06,
            'Dia 07': jan_07, 'Dia 08': jan_08, 'Dia 09': jan_09, 'Dia 10': jan_10, 'Dia 11': jan_11, 'Dia 12': jan_12,
            'Dia 13': jan_13, 'Dia 14': jan_14, 'Dia 15': jan_15, 'Dia 16': jan_16, 'Dia 17': jan_17, 'Dia 18': jan_18,
            'Dia 19': jan_19, 'Dia 20': jan_20, 'Dia 21': jan_21, 'Dia 22': jan_22, 'Dia 23': jan_23, 'Dia 24': jan_24,
            'Dia 25': jan_25, 'Dia 26': jan_26, 'Dia 27': jan_27, 'Dia 28': jan_28, 'Dia 29': jan_29, 'Dia 30': jan_30,
            'Dia 31': jan_31}

fev_data = {'Dia 01': fev_01, 'Dia 02': fev_02, 'Dia 03': fev_03, 'Dia 04': fev_04, 'Dia 05': fev_05, 'Dia 06': fev_06,
            'Dia 07': fev_07, 'Dia 08': fev_08, 'Dia 09': fev_09, 'Dia 10': fev_10, 'Dia 11': fev_11, 'Dia 12': fev_12,
            'Dia 13': fev_13, 'Dia 14': fev_14, 'Dia 15': fev_15, 'Dia 16': fev_16, 'Dia 17': fev_17, 'Dia 18': fev_18,
            'Dia 19': fev_19, 'Dia 20': fev_20, 'Dia 21': fev_21, 'Dia 22': fev_22, 'Dia 23': fev_23, 'Dia 24': fev_24,
            'Dia 25': fev_25, 'Dia 26': fev_26, 'Dia 27': fev_27, 'Dia 28': fev_28}

mar_data = {'Dia 01': mar_01, 'Dia 02': mar_02, 'Dia 03': mar_03, 'Dia 04': mar_04, 'Dia 05': mar_05, 'Dia 06': mar_06,
            'Dia 07': mar_07, 'Dia 08': mar_08, 'Dia 09': mar_09, 'Dia 10': mar_10, 'Dia 11': mar_11, 'Dia 12': mar_12,
            'Dia 13': mar_13, 'Dia 14': mar_14, 'Dia 15': mar_15, 'Dia 16': mar_16, 'Dia 17': mar_17, 'Dia 18': mar_18,
            'Dia 19': mar_19, 'Dia 20': mar_20, 'Dia 21': mar_21, 'Dia 22': mar_22, 'Dia 23': mar_23, 'Dia 24': mar_24,
            'Dia 25': mar_25, 'Dia 26': mar_26, 'Dia 27': mar_27, 'Dia 28': mar_28, 'Dia 29': mar_29, 'Dia 30': mar_30,
            'Dia 31': mar_31}

apr_data = {'Dia 01': apr_01, 'Dia 02': apr_02, 'Dia 03': apr_03, 'Dia 04': apr_04, 'Dia 05': apr_05, 'Dia 06': apr_06,
            'Dia 07': apr_07, 'Dia 08': apr_08, 'Dia 09': apr_09, 'Dia 10': apr_10, 'Dia 11': apr_11, 'Dia 12': apr_12,
            'Dia 13': apr_13, 'Dia 14': apr_14, 'Dia 15': apr_15, 'Dia 16': apr_16, 'Dia 17': apr_17, 'Dia 18': apr_18,
            'Dia 19': apr_19, 'Dia 20': apr_20, 'Dia 21': apr_21, 'Dia 22': apr_22, 'Dia 23': apr_23, 'Dia 24': apr_24,
            'Dia 25': apr_25, 'Dia 26': apr_26, 'Dia 27': apr_27, 'Dia 28': apr_28, 'Dia 29': apr_29, 'Dia 30': apr_30}

may_data = {'Dia 01': may_01, 'Dia 02': may_02, 'Dia 03': may_03, 'Dia 04': may_04, 'Dia 05': may_05, 'Dia 06': may_06,
            'Dia 07': may_07, 'Dia 08': may_08, 'Dia 09': may_09, 'Dia 10': may_10, 'Dia 11': may_11, 'Dia 12': may_12,
            'Dia 13': may_13, 'Dia 14': may_14, 'Dia 15': may_15, 'Dia 16': may_16, 'Dia 17': may_17, 'Dia 18': may_18,
            'Dia 19': may_19, 'Dia 20': may_20, 'Dia 21': may_21, 'Dia 22': may_22, 'Dia 23': may_23, 'Dia 24': may_24,
            'Dia 25': may_25, 'Dia 26': may_26, 'Dia 27': may_27, 'Dia 28': may_28, 'Dia 29': may_29, 'Dia 30': may_30,
            'Dia 31': may_31}

jun_data = {'Dia 01': jun_01, 'Dia 02': jun_02, 'Dia 03': jun_03, 'Dia 04': jun_04, 'Dia 05': jun_05, 'Dia 06': jun_06,
            'Dia 07': jun_07, 'Dia 08': jun_08, 'Dia 09': jun_09, 'Dia 10': jun_10, 'Dia 11': jun_11, 'Dia 12': jun_12,
            'Dia 13': jun_13, 'Dia 14': jun_14, 'Dia 15': jun_15, 'Dia 16': jun_16, 'Dia 17': jun_17, 'Dia 18': jun_18,
            'Dia 19': jun_19, 'Dia 20': jun_20, 'Dia 21': jun_21, 'Dia 22': jun_22, 'Dia 23': jun_23, 'Dia 24': jun_24,
            'Dia 25': jun_25, 'Dia 26': jun_26, 'Dia 27': jun_27, 'Dia 28': jun_28, 'Dia 29': jun_29, 'Dia 30': jun_30}

jul_data = {'Dia 01': jul_01, 'Dia 02': jul_02, 'Dia 03': jul_03, 'Dia 04': jul_04, 'Dia 05': jul_05, 'Dia 06': jul_06,
            'Dia 07': jul_07, 'Dia 08': jul_08, 'Dia 09': jul_09, 'Dia 10': jul_10, 'Dia 11': jul_11, 'Dia 12': jul_12,
            'Dia 13': jul_13, 'Dia 14': jul_14, 'Dia 15': jul_15, 'Dia 16': jul_16, 'Dia 17': jul_17, 'Dia 18': jul_18,
            'Dia 19': jul_19, 'Dia 20': jul_20, 'Dia 21': jul_21, 'Dia 22': jul_22, 'Dia 23': jul_23, 'Dia 24': jul_24,
            'Dia 25': jul_25, 'Dia 26': jul_26, 'Dia 27': jul_27, 'Dia 28': jul_28, 'Dia 29': jul_29, 'Dia 30': jul_30,
            'Dia 31': jul_31}

aug_data = {'Dia 01': aug_01, 'Dia 02': aug_02, 'Dia 03': aug_03, 'Dia 04': aug_04, 'Dia 05': aug_05, 'Dia 06': aug_06,
            'Dia 07': aug_07, 'Dia 08': aug_08, 'Dia 09': aug_09, 'Dia 10': aug_10, 'Dia 11': aug_11, 'Dia 12': aug_12,
            'Dia 13': aug_13, 'Dia 14': aug_14, 'Dia 15': aug_15, 'Dia 16': aug_16, 'Dia 17': aug_17, 'Dia 18': aug_18,
            'Dia 19': aug_19, 'Dia 20': aug_20, 'Dia 21': aug_21, 'Dia 22': aug_22, 'Dia 23': aug_23, 'Dia 24': aug_24,
            'Dia 25': aug_25, 'Dia 26': aug_26, 'Dia 27': aug_27, 'Dia 28': aug_28, 'Dia 29': aug_29, 'Dia 30': aug_30,
            'Dia 31': aug_31}

sep_data = {'Dia 01': sep_01, 'Dia 02': sep_02, 'Dia 03': sep_03, 'Dia 04': sep_04, 'Dia 05': sep_05, 'Dia 06': sep_06,
            'Dia 07': sep_07, 'Dia 08': sep_08, 'Dia 09': sep_09, 'Dia 10': sep_10, 'Dia 11': sep_11, 'Dia 12': sep_12,
            'Dia 13': sep_13, 'Dia 14': sep_14, 'Dia 15': sep_15, 'Dia 16': sep_16, 'Dia 17': sep_17, 'Dia 18': sep_18,
            'Dia 19': sep_19, 'Dia 20': sep_20, 'Dia 21': sep_21, 'Dia 22': sep_22, 'Dia 23': sep_23, 'Dia 24': sep_24,
            'Dia 25': sep_25, 'Dia 26': sep_26, 'Dia 27': sep_27, 'Dia 28': sep_28, 'Dia 29': sep_29, 'Dia 30': sep_30}

oct_data = {'Dia 01': oct_01, 'Dia 02': oct_02, 'Dia 03': oct_03, 'Dia 04': oct_04, 'Dia 05': oct_05, 'Dia 06': oct_06,
            'Dia 07': oct_07, 'Dia 08': oct_08, 'Dia 09': oct_09, 'Dia 10': oct_10, 'Dia 11': oct_11, 'Dia 12': oct_12,
            'Dia 13': oct_13, 'Dia 14': oct_14, 'Dia 15': oct_15, 'Dia 16': oct_16, 'Dia 17': oct_17, 'Dia 18': oct_18,
            'Dia 19': oct_19, 'Dia 20': oct_20, 'Dia 21': oct_21, 'Dia 22': oct_22, 'Dia 23': oct_23, 'Dia 24': oct_24,
            'Dia 25': oct_25, 'Dia 26': oct_26, 'Dia 27': oct_27, 'Dia 28': oct_28, 'Dia 29': oct_29, 'Dia 30': oct_30,
            'Dia 31': oct_31}

nov_data = {'Dia 01': nov_01, 'Dia 02': nov_02, 'Dia 03': nov_03, 'Dia 04': nov_04, 'Dia 05': nov_05, 'Dia 06': nov_06,
            'Dia 07': nov_07, 'Dia 08': nov_08, 'Dia 09': nov_09, 'Dia 10': nov_10, 'Dia 11': nov_11, 'Dia 12': nov_12,
            'Dia 13': nov_13, 'Dia 14': nov_14, 'Dia 15': nov_15, 'Dia 16': nov_16, 'Dia 17': nov_17, 'Dia 18': nov_18,
            'Dia 19': nov_19, 'Dia 20': nov_20, 'Dia 21': nov_21, 'Dia 22': nov_22, 'Dia 23': nov_23, 'Dia 24': nov_24,
            'Dia 25': nov_25, 'Dia 26': nov_26, 'Dia 27': nov_27, 'Dia 28': nov_28, 'Dia 29': nov_29, 'Dia 30': nov_30}

dec_data = {'Dia 01': dec_01, 'Dia 02': dec_02, 'Dia 03': dec_03, 'Dia 04': dec_04, 'Dia 05': dec_05, 'Dia 06': dec_06,
            'Dia 07': dec_07, 'Dia 08': dec_08, 'Dia 09': dec_09, 'Dia 10': dec_10, 'Dia 11': dec_11, 'Dia 12': dec_12,
            'Dia 13': dec_13, 'Dia 14': dec_14, 'Dia 15': dec_15, 'Dia 16': dec_16, 'Dia 17': dec_17, 'Dia 18': dec_18,
            'Dia 19': dec_19, 'Dia 20': dec_20, 'Dia 21': dec_21, 'Dia 22': dec_22, 'Dia 23': dec_23, 'Dia 24': dec_24,
            'Dia 25': dec_25, 'Dia 26': dec_26, 'Dia 27': dec_27, 'Dia 28': dec_28, 'Dia 29': dec_29, 'Dia 30': dec_30,
            'Dia 31': dec_31}

jan_json = json.dumps(jan_data)
fev_json = json.dumps(fev_data)
mar_json = json.dumps(mar_data)
apr_json = json.dumps(apr_data)
may_json = json.dumps(may_data)
jun_json = json.dumps(jun_data)
jul_json = json.dumps(jul_data)
aug_json = json.dumps(aug_data)
sep_json = json.dumps(sep_data)
oct_json = json.dumps(oct_data)
nov_json = json.dumps(nov_data)
dec_json = json.dumps(dec_data)

year_data = {
    'Dia 01': jan_01, 'Dia 02': jan_02, 'Dia 03': jan_03, 'Dia 04': jan_04, 'Dia 05': jan_05, 'Dia 06': jan_06, 'Dia 07': jan_07,
    'Dia 08': jan_08, 'Dia 09': jan_09, 'Dia 10': jan_10, 'Dia 11': jan_11, 'Dia 12': jan_12, 'Dia 13': jan_13, 'Dia 14': jan_14,
    'Dia 15': jan_15, 'Dia 16': jan_16, 'Dia 17': jan_17, 'Dia 18': jan_18, 'Dia 19': jan_19, 'Dia 20': jan_20, 'Dia 21': jan_21,
    'Dia 22': jan_22, 'Dia 23': jan_23, 'Dia 24': jan_24, 'Dia 25': jan_25, 'Dia 26': jan_26, 'Dia 27': jan_27, 'Dia 28': jan_28,
    'Dia 29': jan_29, 'Dia 30': jan_30, 'Dia 31': jan_31, 'Dia 32': fev_01, 'Dia 33': fev_02, 'Dia 34': fev_03, 'Dia 35': fev_04,
    'Dia 36': fev_05, 'Dia 37': fev_06, 'Dia 38': fev_07, 'Dia 39': fev_08, 'Dia 40': fev_09, 'Dia 41': fev_10, 'Dia 42': fev_11,
    'Dia 43': fev_12, 'Dia 44': fev_13, 'Dia 45': fev_14, 'Dia 46': fev_15, 'Dia 47': fev_16, 'Dia 48': fev_17, 'Dia 49': fev_18,
    'Dia 50': fev_19, 'Dia 51': fev_20, 'Dia 52': fev_21, 'Dia 53': fev_22, 'Dia 54': fev_23, 'Dia 55': fev_24, 'Dia 56': fev_25,
    'Dia 57': fev_26, 'Dia 58': fev_27, 'Dia 59': fev_28, 'Dia 60': mar_01, 'Dia 61': mar_02, 'Dia 62': mar_03, 'Dia 63': mar_04,
    'Dia 64': mar_05, 'Dia 65': mar_06, 'Dia 66': mar_07, 'Dia 67': mar_08, 'Dia 68': mar_09, 'Dia 69': mar_10, 'Dia 70': mar_11,
    'Dia 71': mar_12, 'Dia 72': mar_13, 'Dia 73': mar_14, 'Dia 74': mar_15, 'Dia 75': mar_16, 'Dia 76': mar_17, 'Dia 77': mar_18,
    'Dia 78': mar_19, 'Dia 79': mar_20, 'Dia 80': mar_21, 'Dia 81': mar_22, 'Dia 82': mar_23, 'Dia 83': mar_24, 'Dia 84': mar_25,
    'Dia 85': mar_26, 'Dia 86': mar_27, 'Dia 87': mar_28, 'Dia 88': mar_29, 'Dia 89': mar_30, 'Dia 90': mar_31, 'Dia 91': apr_01,
    'Dia 92': apr_02, 'Dia 93': apr_03, 'Dia 94': apr_04, 'Dia 95': apr_05, 'Dia 96': apr_06, 'Dia 97': apr_07, 'Dia 98': apr_08,
    'Dia 99': apr_09, 'Dia 100': apr_10, 'Dia 101': apr_11, 'Dia 102': apr_12, 'Dia 103': apr_13, 'Dia 104': apr_14, 'Dia 105': apr_15,
    'Dia 106': apr_16, 'Dia 107': apr_17, 'Dia 108': apr_18, 'Dia 109': apr_19, 'Dia 110': apr_20, 'Dia 111': apr_21, 'Dia 112': apr_22,
    'Dia 113': apr_23, 'Dia 114': apr_24, 'Dia 115': apr_25, 'Dia 116': apr_26, 'Dia 117': apr_27, 'Dia 118': apr_28, 'Dia 119': apr_29,
    'Dia 120': apr_30, 'Dia 121': may_01, 'Dia 122': may_02, 'Dia 123': may_03, 'Dia 124': may_04, 'Dia 125': may_05, 'Dia 126': may_06,
    'Dia 127': may_07, 'Dia 128': may_08, 'Dia 129': may_09, 'Dia 130': may_10, 'Dia 131': may_11, 'Dia 132': may_12, 'Dia 133': may_13,
    'Dia 134': may_14, 'Dia 135': may_15, 'Dia 136': may_16, 'Dia 137': may_17, 'Dia 138': may_18, 'Dia 139': may_19, 'Dia 140': may_20,
    'Dia 141': may_21, 'Dia 142': may_22, 'Dia 143': may_23, 'Dia 144': may_24, 'Dia 145': may_25, 'Dia 146': may_26, 'Dia 147': may_27,
    'Dia 148': may_28, 'Dia 149': may_29, 'Dia 150': may_30, 'Dia 151': may_31, 'Dia 152': jun_01, 'Dia 153': jun_02, 'Dia 154': jun_03,
    'Dia 155': jun_04, 'Dia 156': jun_05, 'Dia 157': jun_06, 'Dia 158': jun_07, 'Dia 159': jun_08, 'Dia 160': jun_09, 'Dia 161': jun_10,
    'Dia 162': jun_11, 'Dia 163': jun_12, 'Dia 164': jun_13, 'Dia 165': jun_14, 'Dia 166': jun_15, 'Dia 167': jun_16, 'Dia 168': jun_17,
    'Dia 169': jun_18, 'Dia 170': jun_19, 'Dia 171': jun_20, 'Dia 172': jun_21, 'Dia 173': jun_22, 'Dia 174': jun_23, 'Dia 175': jun_24,
    'Dia 176': jun_25, 'Dia 177': jun_26, 'Dia 178': jun_27, 'Dia 179': jun_28, 'Dia 180': jun_29, 'Dia 181': jun_30, 'Dia 182': jul_01,
    'Dia 183': jul_02, 'Dia 184': jul_03, 'Dia 185': jul_04, 'Dia 186': jul_05, 'Dia 187': jul_06, 'Dia 188': jul_07, 'Dia 189': jul_08,
    'Dia 190': jul_09, 'Dia 191': jul_10, 'Dia 192': jul_11, 'Dia 193': jul_12, 'Dia 194': jul_13, 'Dia 195': jul_14, 'Dia 196': jul_15,
    'Dia 197': jul_16, 'Dia 198': jul_17, 'Dia 199': jul_18, 'Dia 200': jul_19, 'Dia 201': jul_20, 'Dia 202': jul_21, 'Dia 203': jul_22,
    'Dia 204': jul_23, 'Dia 205': jul_24, 'Dia 206': jul_25, 'Dia 207': jul_26, 'Dia 208': jul_27, 'Dia 209': jul_28, 'Dia 210': jul_29,
    'Dia 211': jul_30, 'Dia 212': jul_31, 'Dia 213': aug_01, 'Dia 214': aug_02, 'Dia 215': aug_03, 'Dia 216': aug_04, 'Dia 217': aug_05,
    'Dia 218': aug_06, 'Dia 219': aug_07, 'Dia 220': aug_08, 'Dia 221': aug_09, 'Dia 222': aug_10, 'Dia 223': aug_11, 'Dia 224': aug_12,
    'Dia 225': aug_13, 'Dia 226': aug_14, 'Dia 227': aug_15, 'Dia 228': aug_16, 'Dia 229': aug_17, 'Dia 230': aug_18, 'Dia 231': aug_19,
    'Dia 232': aug_20, 'Dia 233': aug_21, 'Dia 234': aug_22, 'Dia 235': aug_23, 'Dia 236': aug_24, 'Dia 237': aug_25, 'Dia 238': aug_26,
    'Dia 239': aug_27, 'Dia 240': aug_28, 'Dia 241': aug_29, 'Dia 242': aug_30, 'Dia 243': aug_31, 'Dia 244': sep_01, 'Dia 245': sep_02,
    'Dia 246': sep_03, 'Dia 247': sep_04, 'Dia 248': sep_05, 'Dia 249': sep_06, 'Dia 250': sep_07, 'Dia 251': sep_08, 'Dia 252': sep_09,
    'Dia 253': sep_10, 'Dia 254': sep_11, 'Dia 255': sep_12, 'Dia 256': sep_13, 'Dia 257': sep_14, 'Dia 258': sep_15, 'Dia 259': sep_16,
    'Dia 260': sep_17, 'Dia 261': sep_18, 'Dia 262': sep_19, 'Dia 263': sep_20, 'Dia 264': sep_21, 'Dia 265': sep_22, 'Dia 266': sep_23,
    'Dia 267': sep_24, 'Dia 268': sep_25, 'Dia 269': sep_26, 'Dia 270': sep_27, 'Dia 271': sep_28, 'Dia 272': sep_29, 'Dia 273': sep_30,
    'Dia 274': oct_01, 'Dia 275': oct_02, 'Dia 276': oct_03, 'Dia 277': oct_04, 'Dia 278': oct_05, 'Dia 279': oct_06, 'Dia 280': oct_07,
    'Dia 281': oct_08, 'Dia 282': oct_09, 'Dia 283': oct_10, 'Dia 284': oct_11, 'Dia 285': oct_12, 'Dia 286': oct_13, 'Dia 287': oct_14,
    'Dia 288': oct_15, 'Dia 289': oct_16, 'Dia 290': oct_17, 'Dia 291': oct_18, 'Dia 292': oct_19, 'Dia 293': oct_20, 'Dia 294': oct_21,
    'Dia 295': oct_22, 'Dia 296': oct_23, 'Dia 297': oct_24, 'Dia 298': oct_25, 'Dia 299': oct_26, 'Dia 300': oct_27, 'Dia 301': oct_28,
    'Dia 302': oct_29, 'Dia 303': oct_30, 'Dia 304': oct_31, 'Dia 305': nov_01, 'Dia 306': nov_02, 'Dia 307': nov_03, 'Dia 308': nov_04,
    'Dia 309': nov_05, 'Dia 310': nov_06, 'Dia 311': nov_07, 'Dia 312': nov_08, 'Dia 313': nov_09, 'Dia 314': nov_10, 'Dia 315': nov_11,
    'Dia 316': nov_12, 'Dia 317': nov_13, 'Dia 318': nov_14, 'Dia 319': nov_15, 'Dia 320': nov_16, 'Dia 321': nov_17, 'Dia 322': nov_18,
    'Dia 323': nov_19, 'Dia 324': nov_20, 'Dia 325': nov_21, 'Dia 326': nov_22, 'Dia 327': nov_23, 'Dia 328': nov_24, 'Dia 329': nov_25,
    'Dia 330': nov_26, 'Dia 331': nov_27, 'Dia 332': nov_28, 'Dia 333': nov_29, 'Dia 334': nov_30, 'Dia 335': dec_01, 'Dia 336': dec_02,
    'Dia 337': dec_03, 'Dia 338': dec_04, 'Dia 339': dec_05, 'Dia 340': dec_06, 'Dia 341': dec_07, 'Dia 342': dec_08, 'Dia 343': dec_09,
    'Dia 344': dec_10, 'Dia 345': dec_11, 'Dia 346': dec_12, 'Dia 347': dec_13, 'Dia 348': dec_14, 'Dia 349': dec_15, 'Dia 350': dec_16,
    'Dia 351': dec_17, 'Dia 352': dec_18, 'Dia 353': dec_19, 'Dia 354': dec_20, 'Dia 355': dec_21, 'Dia 356': dec_22, 'Dia 357': dec_23,
    'Dia 358': dec_24, 'Dia 359': dec_25, 'Dia 360': dec_26, 'Dia 361': dec_27, 'Dia 362': dec_28, 'Dia 363': dec_29, 'Dia 364': dec_30,
    'Dia 365': dec_31}

year_json = json.dumps(year_data)
