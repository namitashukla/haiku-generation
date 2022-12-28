import nltk
nltk.download('punkt')

from GRUEN.greun import *

import pandas as pd
import numpy as np
from tqdm import tqdm
import sys

from phonemizer import phonemize
from phonemizer.separator import Separator

def get_phonemes(line,char="|"):
  '''
  Get Phonemes 

  Arguments:
    Input:
      line (str) - text for calculating phn
  '''
  try:
    phn = phonemize(line, language='en-us', backend='festival', with_stress=False,
        separator=Separator(phone=None, word=' ', syllable=char), strip=True)
  except:
    # 1 syllable
    phn = ""
  return phn


def syllable_count(sen, char = "|"):
  '''
  Get Phonemes 

  Arguments:
    Input:
      sen (str) - phonemized structure split by char
  '''
  return sum([len(ph.split(char)) for ph in sen.split(" ")])


def get_data_syllables(data):
  '''
  Get syllable count for each line of poem

  Arguments: 
    data = 
  '''
  phenoemes_data = np.apply_along_axis(func1d=get_phonemes,arr=np.array(list(data)), axis=0)
  return [syllable_count(sen) for sen in phenoemes_data]


def gruen_loop(data):
    '''
    GRUEN metric fails to run for large amounts of data - hence the loop
    '''
    gruen_score = []
    index = []
    for i in tqdm(range(0,len(data),10)):
        try:
            gruen_score.extend(get_gruen(data[i:i+10]))
            index.extend(list(range(i,i+10)))
        except:
            pass

    return gruen_score,index


if __name__ ==  "__main__":
    args = sys.argv[1:]
    path = args[0]

    data = pd.read_csv(path)
    data = data[['sent_1', 'sent_2', 'sent_3']].copy()

    '''GRUEN'''
    gruen_score,index = gruen_loop(pd.Series(list(data[['sent_1', 'sent_2', 'sent_3']].astype(str).values)).apply(lambda x: ' '.join(x)).to_list())
    print(pd.Series(gruen_score).describe())

    # Save the metrics
    # save_path = '/'.join(path.split('/')[:-1]) + str('/gruen_output.csv')
    # pd.DataFrame(pd.Series(gruen_score).describe(),columns=['gruen_score']).reset_index().to_csv(save_path,index=False)

    for i in tqdm(data.columns[:3]):
        data[str(i)+"_syllable"] = get_data_syllables(data[i])
        
    print(data[[col for col in data.columns if 'syllable' in col]].describe())

    # Save the metrics
    # save_path = '/'.join(path.split('/')[:-1]) + str('/syllable_output.csv')
    # pd.DataFrame(data[[col for col in data.columns if 'syllable' in col]].describe(),columns=['gruen_score']).reset_index().to_csv(save_path,index=False)
