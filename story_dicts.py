import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sent_dict import sent
from anim_utils import *

# # Get valences per sentence from EVAL scripts and normalize
# rates = pd.read_csv('/home/mina/Dropbox/APRIL-MINA/EXP3_Generation/storyTelling/Eval/Eval/Anders_Cebron_Grimm.txt', sep=' ', header=None)
# and_v = rates.iloc[0:38, :]
# v_keys = and_v.iloc[:, 0]
# v_val = and_v.iloc[:, 1:]
#
# v_val = v_val.convert_objects(convert_numeric=True)
#
# scaler = MinMaxScaler(feature_range=(0., 1.))
# scaler = scaler.fit(v_val)
# normalized = scaler.transform(v_val)
#
# v_mean =np.nanmean(normalized, axis=1)
#
# sent_vnan = {}
# for i in range(38):
#     sent_vnan[v_keys[i]] = round(v_mean[i], 2)

# Sentece valence
sent_v = {'a20': 0.94, 'a21': 0.38, 'a22': 0.22, 'a23': 0.78, 'a24': 0.85, 'a25': 0.16, 'a26': 0.58, 'a27': 0.88,
          'a28': 0.23, 'a29': 0.71, 'a31': 0.86, 'a30': 0.53, 'a37': 0.15, 'a36': 0.25, 'a33': 0.76, 'a35': 0.87,
          'a34': 0.8, 'a32': 0.62, 'a15': 0.65, 'a14': 0.07, 'a17': 0.82, 'a16': 0.62, 'a11': 0.65, 'a10': 0.56,
          'a13': 0.07, 'a12': 0.47, 'a38': 0.64, 'a19': 0.91, 'a18': 0.83, 'a1': 0.26, 'a3': 0.16, 'a2': 0.03,
          'a5': 0.03, 'a4': 0.22, 'a7': 0.18, 'a6': 0.44, 'a9': 0.08, 'a8': 0.11}

sent_keys = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16',
             'a17', 'a18', 'a19', 'a20', 'a21', 'a22', 'a23', 'a24', 'a25', 'a26', 'a27', 'a28', 'a29', 'a30', 'a31',
             'a32', 'a33', 'a34', 'a35', 'a36', 'a37', 'a38']

sent_anim = {'a1': 'l1_168_dec_long0_r4_Neg.csv', 'a2': 'l3_138_dec_long6_r3_Neg.csv',
             'a3': 'l3_171_dec_long1_r4_Neg.csv', 'a4': 'l1_120_dec_long0_r3_Neg.csv',
             'a5': 'l3_132_dec_long4_r3_Neg.csv', 'a6': 'l2_127_dec_long2_r3_Neu.csv',
             'a7': 'l2_129_dec_long3_r3_Neg.csv', 'a8': 'l1_141_dec_long7_r3_Neg.csv',
             'a9': 'l2_177_dec_long3_r4_Neg.csv', 'a10': 'l2_184_dec_long5_r4_Neu.csv',
             'a11': 'l1_190_dec_long7_r4_Neu.csv', 'a12': 'l3_139_dec_long6_r3_Neu.csv',
             'a13': 'l1_237_dec_long7_r5_Neg.csv', 'a14': 'l3_141_dec_long7_r3_Neg.csv',
             'a15': 'l1_136_dec_long5_r3_Neu.csv', 'a16': 'l2_85_dec_long4_r2_Neu.csv',
             'a17': 'l1_95_dec_long7_r2_Pos.csv', 'a18': 'l2_182_dec_long4_r4_Pos.csv',
             'a19': 'l1_191_dec_long7_r4_Pos.csv', 'a20': 'l2_131_dec_long3_r3_Pos.csv',
             'a21': 'l1_187_dec_long6_r4_Neu.csv', 'a22': 'l1_183_dec_long5_r4_Neg.csv',
             'a23': 'l2_224_dec_long2_r5_Pos.csv', 'a24': 'l1_236_dec_long6_r5_Pos.csv',
             'a25': 'l2_132_dec_long4_r3_Neg.csv', 'a26': 'l1_88_dec_long5_r2_Neu.csv',
             'a27': 'l1_233_dec_long5_r5_Pos.csv', 'a28': 'l3_120_dec_long0_r3_Neg.csv',
             'a29': 'l3_185_dec_long5_r4_Pos.csv', 'a30': 'l2_229_dec_long4_r5_Neu.csv',
             'a31': 'l3_176_dec_long2_r4_Pos.csv', 'a32': 'l2_232_dec_long5_r5_Neu.csv',
             'a33': 'l1_185_dec_long5_r4_Pos.csv', 'a34': 'l3_134_dec_long4_r3_Pos.csv',
             'a35': 'l3_230_dec_long4_r5_Pos.csv', 'a36': 'l2_180_dec_long4_r4_Neg.csv',
             'a37': 'l3_189_dec_long7_r4_Neg.csv', 'a38': 'l2_172_dec_long1_r4_Neu.csv'}


# Speech duration of each sentence
sent_dur = {'a20': 3.870327949523926, 'a21': 7.092369079589844, 'a22': 7.196001052856445, 'a23': 8.889841079711914,
            'a24': 24.38889193534851, 'a25': 5.624668121337891, 'a26': 1.701089859008789, 'a27': 19.688267946243286,
            'a28': 4.542748928070068, 'a29': 8.832337856292725, 'a31': 9.671294927597046, 'a30': 13.543401956558228,
            'a37': 9.267218112945557, 'a36': 9.35027289390564, 'a33': 6.841655969619751, 'a35': 14.343612909317017,
            'a34': 5.253765106201172, 'a32': 16.578226804733276, 'a15': 4.732501029968262, 'a14': 3.498615026473999,
            'a17': 2.7546050548553467, 'a16': 2.15486216545105, 'a11': 11.661909103393555, 'a10': 8.820856094360352,
            'a13': 21.524309158325195, 'a12': 4.0792951583862305, 'a38': 7.69760799407959, 'a19': 7.405091047286987,
            'a18': 8.0204439163208, 'a1': 7.39878511428833, 'a3': 16.18538784980774, 'a2': 7.4052557945251465,
            'a5': 5.281320810317993, 'a4': 6.7420220375061035, 'a7': 3.63273286819458, 'a6': 7.312089920043945,
            'a9': 6.458831787109375, 'a8': 3.002556085586548}

# # Measure spoken sentence duration
# strIP = '10.0.206.62'
# nPort = 9559
# # Connect to robot (for virtual only give port, for real only give IP string)
# session = connect(strIP, nPort)
# # Load naoqi modules
# motion_ses, aplayer_ses, posture_ses, leds_ses, alife_ses = load_modules(session)
# # Resting state
# init_rest(leds_ses, alife_ses, posture_ses)
#
# tts_ses = session.service("ALTextToSpeech")
# tts_ses.setParameter('speed', 85)
#
# for k in ['a39']:
#     phrase = sent[k]
#     # raw_input("Press Enter to continue...")
#     print(k)
#     print(phrase)
#     print('........')
#     start = time.time()
#     tts_ses.say(phrase)
#     end = time.time() - start
#     sent_dur[k] = end
#     print(" Duration: ", str(end))
#
# k = None
