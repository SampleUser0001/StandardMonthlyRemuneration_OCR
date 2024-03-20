# -*- coding: utf-8 -*-
from logging import getLogger, config, DEBUG
import os

# import sys
from logutil import LogUtil
from importenv import ImportEnvKeyEnum

from util.sample import Util
from controller import SampleController

import pytesseract
from PIL import Image
import pandas as pd

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
LOG_CONFIG_FILE = ['config', 'log_config.json']

logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(os.path.join(PYTHON_APP_HOME, *LOG_CONFIG_FILE))
config.dictConfig(log_conf)
logger.setLevel(DEBUG)
logger.propagate = False

def convert_to_tsv():
    
    # Open the image file
    import_path = os.path.join(PYTHON_APP_HOME, 'import', 'clipboarded.png')
    logger.info(f'import_path : {import_path}')
    img = Image.open(import_path)

    # Use tesseract to do OCR on the image
    # Tesseractの日本語の言語パックがインストールされていることを確認してください
    text = pytesseract.image_to_string(img, lang='jpn')

    # The expected format is a TSV, so we need to process the string into lines and columns
    lines = text.split('\\n')
    rows = [line.split() for line in lines if line.strip()]  # 空白で区切られた各行をリストに変換

    # Create a DataFrame
    df = pd.DataFrame(rows)

    # Save to a TSV file
    tsv_path = os.path.join(PYTHON_APP_HOME, 'export', 'standard_monthly_remunerantion.tsv')  # 出力するTSVファイルのパスに変更してください
    logger.info(f'tsv_path : {tsv_path}')
    df.to_csv(tsv_path, sep='\t', index=False, header=False)

if __name__ == '__main__':
    # 起動引数の取得
    # args = sys.argv
    # args[0]はpythonのファイル名。
    # 実際の引数はargs[1]から。
    
    logger.info('Start')
    logger.info('Convert to TSV')
    convert_to_tsv()
    logger.info('Finish')