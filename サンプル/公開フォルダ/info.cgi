#!/usr/bin/mono RdrCGI.exe
パスは、要求から「path」という引数を取得したもの

応答として「<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS" />
</head>
<body>
<h1>情報</h1>
<table border="1">
	<tr><td>参照元</td><td>[要求の参照元]</td></tr>
	<tr><td>ユーザエージェント</td><td>[要求のユーザエージェント]</td></tr>
	<tr><td>IPアドレス</td><td>[要求のIPアドレス]</td></tr>
	<tr><td>ホスト名</td><td>[要求のホスト名]</td></tr>
	<tr><td>要求アドレス</td><td>[要求の要求アドレス]</td></tr>
	<tr><td>HTTPメソッド</td><td>[要求のHTTPメソッド]</td></tr>
	<tr><td>要求アドレス</td><td>[要求の要求アドレス]</td></tr>
	<tr><td>エンコード</td><td>[要求のエンコード]</td></tr>
</table>

<h1>ヘッダ</h1>
<table border="1">
」を送る
要求のヘッダ一覧のすべての要素について、それぞれ繰り返す
	「<tr><td>[要素]</td><td>[要求から要素というヘッダを取得]</td></tr>」を応答として送る
繰り返し終わり


応答として「
</table>

<h1>引数</h1>
<table border="1">
」を送る

要求の引数一覧のすべての要素について、それぞれ繰り返す
	「<tr><td>[要素]</td><td>[要求から要素という引数を取得]</td></tr>」を応答として送る
繰り返し終わり


応答として「
</table>
<h1>クッキー</h1>
<table border="1">
」を送る

要求のクッキー一覧のすべての要素について、それぞれ繰り返す
	「<tr><td>[要素]</td><td>[(要求から要素というクッキーを取得)の内容]</td></tr>」を応答として送る
繰り返し終わり

応答として「QUERY_STRING="[「QUERY_STRING」の環境変数]"」を送る


応答として「
</table>
</body></html>」を送る
