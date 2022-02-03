import pandas as pd
import numpy as np

training = pd.read_csv('UNSW_NB15_training-set.csv')

#sbytes
sbytes = []
for i in range(82332):
    if training['sbytes'][i] >= 340000:
        sbytes.append(1)
    else:
        sbytes.append(0)

#sloss
sloss = []
for i in range(82332):
    if training['sloss'][i] >= 130:
        sloss.append(1)
    else:
        sloss.append(0)

#sttl
sttl = []
for i in range(82332):
    if training['sttl'][i] == 63255:
        sttl.append(1)
    else:
        sttl.append(0)

#trans_depth
trans = []
for i in range(82332):
    if training['trans_depth'][i] == 0 or training['trans_depth'][i] == 1:
        trans.append(0)
    else:
        trans.append(1)

#swin
swin = []
for i in range(82332):
    if training['swin'][i] == 0 or training['swin'][i] == 255:
        swin.append(1)
    else:
        swin.append(0)

#dwin
dwin = []
for i in range(82332):
    if training['dwin'][i] == 0 or training['dwin'][i] == 255:
        dwin.append(1)
    else:
        dwin.append(0)

#spkts
spkts = []
for i in range(82332):
    if 1 <= training['spkts'][i] <= 690:
        spkts.append(0)
    else:
        spkts.append(1)

#dpkts
dpkts = []
for i in range(82332):
    if 1 <= training['dpkts'][i] <= 1432:
        dpkts.append(0)
    else:
        dpkts.append(1)

#ct_src_dport_ltm
ct_src_dport_ltm = []
for i in range(82332):
    if training['ct_src_dport_ltm'][i] >= 5:
        ct_src_dport_ltm.append(1)
    else:
        ct_src_dport_ltm.append(0)

#ct_dst_sport_ltm
ct_dst_sport_ltm = []
for i in range(82332):
    if training['ct_dst_sport_ltm'][i] >= 5:
        ct_dst_sport_ltm.append(1)
    else:
        ct_dst_sport_ltm.append(0)

#ct_dst_src_ltm
ct_dst_src_ltm = []
for i in range(82332):
    if training['ct_dst_src_ltm'][i] >= 45:
        ct_dst_src_ltm.append(1)
    else:
        ct_dst_src_ltm.append(0)

#공격여부
label = []
for i in range(82332):
    label.append(training['label'][i])


#bitmap
bit = [sbytes, sloss, sttl, trans, swin, dwin, spkts, dpkts, ct_src_dport_ltm, ct_dst_sport_ltm, ct_dst_src_ltm, label]
bitmap = np.array(bit)

col = ['sbytes', 'sloss', 'sttl', 'trans_depth', 'swin', 'dwin', 'spkts', 'dpkts', 'ct_src_dport_ltm', 'ct_dst_sport_ltm', 'ct_dst_src_ltm', 'label']
bitmap_df = pd.DataFrame(bitmap.T, columns=col)

print(bitmap_df)
bitmap_df.to_csv("training_bitmap.csv", mode='w')
