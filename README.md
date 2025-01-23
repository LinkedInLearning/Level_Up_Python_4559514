# レベルアップ：Python
LinkedInラーニングの「レベルアップ：Python」コース用のリポジトリです。このコースは[LinkedInラーニング][lil-course-url]で視聴できます。

![course-name-alt-text][lil-thumbnail-url] 

Pythonに限らずプログラミングのおもしろいところは、同じことをするのに複数の方法があることです。地道だけどわかやすく確実そうなコードや、記号だらけの呪文めいたコードなどいろいろなコードを書くことができます。このコースはクイズにチャレンジしながらPythonの特徴やメリットを学んでいくコースです。簡単な計算や関数の作り方に触れるところから始め、スライス操作やリスト内包表記、セットやディクショナリーの独自の機能、クラスの特殊メソッドの書き方とだんだんレベルアップしていきます。このコースを終えれば、Pythonらしいコードを書ける人になっていることでしょう。

## リポジトリの使い方
このリポジトリには必要に応じてブランチが設けられています。ブランチのポップアップメニューを使用して、使用するブランチに切り替えたあとにコースを視聴してください。またURLに`「/tree/ブランチ名」`を追加することで、アクセスしたいブランチに移動することも可能です。

## ブランチ
ブランチはレッスンごとに作成されている場合があります。その場合はブランチ名に`「章番号_レッスン番号」`が付けられています。例えば`「02_03」`という名前のブランチは、2章の上から3番目のレッスン用のブランチとなります。

レッスン前と後のコードを格納しているブランチもあります。該当ブランチには「開始時」（beginning）を表す`「b」`と、「終了時」（ending）を表す`「e」` がブランチ名についています。`「b」`のブランチにはレッスン開始時点のコードが、`「e」`のブランチにはレッスン終了時点のコードが格納されています。また「main」のブランチにはコードの最終形が格納されています。

ファイルに変更を加えた後に、エクササイズファイルのブランチを次のブランチに切り替えたさい、次のようなメッセージが表示されることがあります。

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

この問題を解決するには：
	
    次のコマンドで変更を加えます：git add .
	次のコマンドで変更をコミットします：git commit -m "some message"
 
 ## GitHub Codespacesについて
プログラミング言語を学ぶ最良の方法は、実際にそれを使用することです。それがこのコースがGitHub Codespacesと統合されている理由です。GitHub Codespacesは、あなたが普段使っているIDEのすべての機能を提供するクラウド上の手軽な開発環境です。ローカルマシンのセットアップも必要ありません。 GitHub Codespacesを使えば、あなたが職場で使っている他のツールを使用しながら、どのパソコンからでもいつでもプログラミングの実践的な練習ができます。

### インストラクター

金宏和實
                            
株式会社イーザー副社長、テクニカルライター

[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/level-up-python-24008939
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4D0DAQGJ1cbhURopgA/learning-public-crop_675_1200/learning-public-crop_675_1200/0/1729189178785?e=2147483647&v=beta&t=3h-uT37OMcP-fKsPe-WUIoCaYBFDWxYoPlXnw9NFwNk

