import translators as ts
import random

#list containing all google translate lang codes
langs_map = ['af',
    'sq',
    'am',
    'ar',
    'hy',
    'az',
    'eu',
    'be',
    'bn',
    'bs',
    'bg',
    'ca',
    'ceb',
    'zh-CN',
    'zh-TW',
    'co',
    'hr',
    'cs',
    'da',
    'nl',
    'en',
    'eo',
    'et',
    'fi',
    'fr',
    'fy',
    'gl',
    'ka',
    'de',
    'el',
    'gu',
    'ht',
    'ha',
    'haw',
    'hi',
    'hmn',
    'hu',
    'is',
    'ig',
    'id',
    'ga',
    'it',
    'ja',
    'kn',
    'kk',
    'km',
    'rw',
    'ko',
    'ku',
    'ky',
    'lo',
    'la',
    'lv',
    'lt',
    'lb',
    'mk',
    'mg',
    'ms',
    'ml',
    'mt',
    'mi',
    'mr',
    'mn',
    'my',
    'ne',
    'no',
    'ny',
    'or',
    'ps',
    'fa',
    'pl',
    'pt',
    'pa',
    'ro',
    'ru',
    'sm',
    'gd',
    'sr',
    'st',
    'sn',
    'sd',
    'si',
    'sk',
    'sl',
    'so',
    'es',
    'su',
    'sw',
    'sv',
    'tl',
    'tg',
    'ta',
    'tt',
    'te',
    'th',
    'tr',
    'tk',
    'uk',
    'ur',
    'ug',
    'uz',
    'vi',
    'cy',
    'xh',
    'yi',
    'yo',
    'zu']
    

def bulk_trans(text:str, num_trans:int=4):
  """
  Will translate str into num_trans different languages and then back into original language

  :param text: str, must
  :param num_trans: int, default 4

  :return: str
  """
  curr=text
  curr=ts.google(curr, to_language='zh-CN', sleep_seconds=0.051)
  for x in range(num_trans):
    #generate random language
    to_lang=langs_map[random.randint(0, 106)]
    curr=ts.google(curr, to_language=to_lang, sleep_seconds=0.051)
    print(to_lang)
  curr=ts.google(curr, to_language='en', sleep_seconds=0.051)
  print(curr)
  return curr