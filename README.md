# lightsout-solver-python
Python版LightsOutソルバー。

与えられたn x n のライト（on or offに切り変わる）に対して、「ライツアウト」の攻略法を計算するためのプログラムです。

このバージョンでは2x2より大きなサイズのライツアウトを対象にします。

オプションで最小タップ数でクリアできるパターンを求めるようにすることもできます。

# ライツアウトとは?
http://qiita.com/LyricalMaestro0/items/2bd9ef55cb49fe788179

# 動作環境
python2.7

# プログラムを試しに動かしてみる(ライツアウトをとく)
1. 本プロジェクトをダウンロード(git clone)する。
2. ダウンロードしたフォルダにターミナル(Windowsであればコマンドライン上に移動する)
3. `python -B solversample.py -s [ライツアウトのサイズ] -mat [ライトの初期の点灯状況を表す行列成分]` と実行すればOK.

# 解きたいライツアウトを指定する
プログラムの起動オプション「-s」「-l」を指定すればOK。たとえば、ライツアウト<BR>
□ □ ■<BR>
■ □ □<BR>
■ □ ■<BR>
<BR>
(■ : on, □ : off)

を指定したければ、起動オプションは 「-s 3 -mat 0,0,1,1,0,0,1,0,1」 とすればよい。

# 解いた結果の解釈
解析が終わると以下のようなレポートが標準出力に表示されます。（ライツアウトが解ける場合）

```
-------      OUTPUT LIGHTSOUT  --------
  □ □ ■
  □ ■ □
  □ ■ □
```
    
これは「上記の並びで■である場所を１回ずつタップすればクリアできる」ということを意味します。
（タップする順番は関係ありません。）

何回タップしてもクリアできない場合は

```
-------      OUTPUT LIGHTSOUT  --------
not solvable.
```

と表示されます。

# その他の機能
コンソール上で「指定したライツアウトのサイズがいかなるライトの点灯状態でも解くことができるか」を判定できます。
`python -B solvabletestsample.py -s [ライツアウトのサイズ]` 
と入力すればOKです。

# LICENSE

 Copyright 2017 LyricalMaestro(@maestro_L_jp)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
