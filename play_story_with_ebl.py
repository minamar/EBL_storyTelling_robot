import naoqi
import time
from settings import *
import os
import pandas as pd
import re
from anim_utils import *
from story_dicts import *
from sent_dict import *
import argparse

"""
Load a df of postures and display on the robot, person='child' or 'adult'
"""


def story_tell(person='child'):
    # parser = argparse.ArgumentParser(description='Process some integers.')
    # parser.add_argument('person', type=str, default='child', help='child or adult?')
    #
    #
    # args = parser.parse_args()
    # person = args.person
    script_dir = os.path.dirname(__file__)

    strIP = '10.0.206.62'
    nPort = 9559
    # Connect to robot (for virtual only give port, for real only give IP string)
    session = connect(strIP, nPort)
    # Load naoqi modules
    motion_ses, aplayer_ses, posture_ses, leds_ses, alife_ses = load_modules(session)
    # Resting state
    init_rest(leds_ses, alife_ses, posture_ses)

    # Start text to speech
    tts_ses = session.service("ALTextToSpeech")
    tts_ses.setParameter('speed', 85)

    if person == 'child':
        # Directory with sampled anims for the fairy tale
        rel_path = 'anims'
        path_to_folder = os.path.join(script_dir, rel_path)

        for k in sent_keys:
            # k='a38'
            ds = sent_anim[k]

            print('........')
            print(ds)

            gen_dir = os.path.join(path_to_folder, ds)
            df = pd.read_csv(gen_dir, index_col=0, skipinitialspace=True)

            df['KneePitch'] = -1.49414
            motion_ses.setStiffnesses("WholeBody", 1)

            tts_fut = tts_ses.say(sent[k], _async=True)
            # Play animation
            start = time.time()
            for i in range(df.shape[0]):
                if tts_fut.isRunning():
                    angle_list = df.loc[i, joints_names].tolist()
                    leds_list = df.loc[i, leds_keys].tolist()
                    rgb_chunks = [leds_list[x * 3:(x + 1) * 3] for x in range((len(leds_list) + 3 - 1) // 3)]

                    # LEDs
                    for l in range(16):
                        leds_ses.fadeRGB(leds_short[l], rgb_chunks[l][0], rgb_chunks[l][1], rgb_chunks[l][2], 0,
                                         _async=True)

                    # Motion
                    motion_ses.setAngles(joints_names, angle_list, 0.05)

            print('Duration: ' + str(time.time() - start))
            motion_ses.setAngles(joints_names, standInit, 0.05, _async=True)
            leds_ses.reset('FaceLeds')
            time.sleep(2.5)

    else:
        radius = 3
        rel_path = 'l3'
        path_to_folder = os.path.join(script_dir, rel_path)

        phrase = sent['a39']

        # Anims
        re1 = r'\w+(dec)+\w+(r' + str(radius) + ')+\w+(Neu.csv)'
        re2 = r'\w+(_dec)+\w+Neu.csv'

        datasets = [f for f in os.listdir(path_to_folder) if re.match(re2, f)]

        tts_fut = tts_ses.say(phrase, _async=True)
        for ds in datasets:
            print(ds)
            gen_dir = os.path.join(path_to_folder, ds)
            df = pd.read_csv(gen_dir, index_col=0, skipinitialspace=True)

            df['KneePitch'] = -1.49414
            motion_ses.setStiffnesses("WholeBody", 1)

            # Play animation
            start = time.time()
            for i in range(df.shape[0]):
                if tts_fut.isRunning():
                    angle_list = df.loc[i, joints_names].tolist()
                    leds_list = df.loc[i, leds_keys].tolist()
                    rgb_chunks = [leds_list[x * 3:(x + 1) * 3] for x in range((len(leds_list) + 3 - 1) // 3)]

                    # LEDs
                    for l in range(16):
                        leds_ses.fadeRGB(leds_short[l], rgb_chunks[l][0], rgb_chunks[l][1], rgb_chunks[l][2], 0,
                                         _async=True)

                    # Motion
                    motion_ses.setAngles(joints_names, angle_list, 0.05)
                else:
                    break

        print('Duration: ' + str(time.time() - start))
        motion_ses.setAngles(joints_names, standInit, 0.05, _async=True)
        leds_ses.reset('FaceLeds')
        time.sleep(2.5)
