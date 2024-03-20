# Standard monthly remunerention OCR

- [Standard monthly remunerention OCR](#standard-monthly-remunerention-ocr)
  - [概要](#概要)
  - [準備](#準備)
  - [実行](#実行)
  - [参考](#参考)

## 概要

標準月額報酬のPDF（実際には切り取って画像にした）をtsvに変換を試みた。  
結果は失敗。

## 準備

``` bash
sudo apt -y update
sudo apt -y install tesseract-ocr tesseract-ocr-jpn libtesseract-dev libleptonica-dev tesseract-ocr-script-jpan tesseract-ocr-script-jpan-vert 

python -m venv venv
source venv/bin/activate
pip install -r app/requirements/requirements.txt
```

## 実行

``` bash
bash start_venv.sh dev
```

## 参考

- [標準月額報酬PDF](https://www.kyoukaikenpo.or.jp/~/media/Files/shared/hokenryouritu/r6/ippan/r60212chiba.pdf)
- [Tesseract OCR のインストール（Ubuntu 上）:金子邦彦研究室](https://www.kkaneko.jp/ai/ubuntu/tesseract.html)