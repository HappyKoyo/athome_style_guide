# 本パッケージ作成の目的  
　本パッケージ作成の目的は、プロジェクト内でのプログラムの受け渡しなどがスムーズにできるようにスタイルを統一することです。ここに書いていないことや、不都合があった場合はその都度更新してアップロードし直すようにおねがいします。  
　また、以下の規則に従ったソースコードの例が本パッケージ内のscriptsディレクトリの中に有ります。参考にしてください。

# 1.命名規則  
## 1.1ディレクトリ・ファイル名  
名詞で定義すること。記法はスネーク  
例：object_recognizer.py  

## 1.2クラス名  
名詞で定義すること。記法はアッパーキャメル  
例：ObjectRecognizer

## 1.3関数名
動詞(+名詞)で定義すること。記法はローワーキャメル  
例：getLaserRangeCB()

## 1.4変数名
名詞で定義すること。記法はスネーク  
例：table_name

## 1.5定数名
名詞で定義すること。大文字とアンダースコアのみ使用する。  
例：BATCH_SIZE

## 1.6その他補足
CB(CallBack)やavg(average)など、誰もがわかる略称以外は使わない。これについて、個人の感覚によって変わるため、はじめのうちはそこまで気にしなくても大丈夫です。  
悪い例：ks(kernel size)

# 2.コード規則  
## 1.1 Pythonのimportについて  
どこのモジュールからインポートしたものか分かりづらくなるため、アスタリスク*を用いない。  
悪い例：from cv2 import *
