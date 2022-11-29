import pandas as pd

test_pptx_DEMON = pd.read_csv('test.pptx.DEMON-from_FileFinderResult.csv')
test_txt_DEMON = pd.read_csv('test.txt.DEMON-from_FileFinderResult.csv')
RAASNet_py = pd.read_csv('RAASNet.py-from_FileFinderResult.csv')
payload = pd.read_csv('payload-from_FileFinderResult.csv')
cwd = pd.read_csv('cwd-from_Process.csv')
ip_port = pd.read_csv('IP&PORT-from_Process.csv')

bitmap = [3,4,5,6,7]

#규칙 3
# test_pptx_DEMON.loc[0][41] #st_mtime
# test_pptx_DEMON.loc[0][42] #st_ctime

if test_pptx_DEMON.loc[0][41] == test_pptx_DEMON.loc[0][42] == test_txt_DEMON.loc[0][41] == test_txt_DEMON.loc[0][42]:
    bitmap[0] = 1
else:
    bitmap[0] = 0

#규칙 4
# RAASNet_py.loc[0][40] #st_atime

payload = payload.loc[0][40]
RAASNet = RAASNet_py.loc[0][40]

payload_hour = int(payload[12])
RAASNet_hour = int(RAASNet[12])

payload_min = int(payload[14]+payload[15])
RAASNet_min = int(RAASNet[14]+RAASNet[15])

payload_sec = int(payload[17]+payload[18])
RAASNet_sec = int(payload[17]+payload[18])

#RAASNET이 더 작으면 1
if payload_hour > RAASNet_hour or payload_min > RAASNet_min or payload_sec > RAASNet_sec:
    bitmap[1] = 1
else:
    bitmap[1] = 0

#규칙 5
test_pptx_demon = test_pptx_DEMON.loc[0][41]

test_pptx_demon_sec = int(test_pptx_demon[17]+test_pptx_demon[18])
payload_sec = int(payload[17]+payload[18])

if payload_sec <= test_pptx_demon_sec + 2:
    bitmap[2] = 1
else:
    bitmap[2] = 0

#규칙 6
#cwd.loc[142][47] #cwd 컬럼. loc의 앞부분은 결과 길이에 따라 다름

for i in range(143):
    if cwd.loc[i][47] == '/home/client2/RAASNet':
        bitmap[3] = 1
        break
    else:
        bitmap[3] = 0

#규칙 7
#ip_port.loc[0][33] : ip
#ip_port.loc[0][34] : port

for i in range(11):
    ip = ip_port.loc[i][33]
    port = ip_port.loc[i][34]

    if ip == '127.0.0.1' and port == '8080':
        bitmap[4] = 1
        break
    else:
        bitmap[4] = 0

#결과 비트맵
print(bitmap)
