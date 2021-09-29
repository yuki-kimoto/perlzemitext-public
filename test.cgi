<!DOCTYPE html>
<html>
  <head>
    <!-- meta -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0">
<link rel="stylesheet" type="text/css" href="/css/common.css">

<title>Title - Perlテキスト処理・正規表現入門 - テキスト処理・正規表現ならPerlゼミ</title>
<meta name="description" content="#!/usr/bin/env perl">
  </head>
  <body>
    <div class="container">
      <div class="header">
        <div class="header_main">
  <h1>
    <a href="/"><img src="/images/logo.png">Perlテキスト処理・正規表現入門</a>
  </h1>
  <div class="header_right">
    <a rel="nofollow" href="https://perlclub.net/account/create">会員登録</a>
  </div>
</div>

      </div>
      <div class="main">
        <div class="content">
          <div class="entry">
  <div class="top">
    <!-- top -->

  </div>
  <div class="middle">
    <p>
  #!/usr/bin/env perl
</p>
<p>
  use strict;
</p>
<p>
  use warnings;
</p>
<p>
  use utf8;
</p>
<p>
  use Encode 'encode';
</p>
<p>
  # Title mail form
</p>
<p>
  my $title = 'Mail form';
</p>
<p>
  # Content mail form
</p>
<p>
  my $content = <<"EOS";
</p>
<h2><a href="/test.cgi">Title</a></h2>
<div>
  Content
</div>
<p>
  EOS
</p>
<p>
  $content = build_html($title, $content);
</p>
<p>
  my $html = <<"EOS";
</p>
<p>
  Content-type: text/html; charset=UTF-8
</p>
<p>
  $content
</p>
<p>
  EOS
</p>
<p>
  print encode('UTF-8', $html);
</p>
<p>
  sub build_html {
</p>
  my ($title, $content) = @_;
  
  local $/;
  my $html = <DATA>;
  
  $html =~ s/\$TITLE/$title/;
  $html =~ s/\$CONTENT/$content/;
  
  return $html;
<p>
  }
</p>
<p>
  __DATA__
</p>

  </div>
  <div class="bottom">
    <!-- bottom -->

  </div>
</div>

        </div>
        <div class="side">
          <div class="side_list">
  <div class="side_list_title">
    Perlテキスト処理のエッセンス
  </div>
  <div class="side_list_body">
    <ul>
      <li>
        <div class="side_list_image">
          <a rel="nofollow" href="https://www.amazon.co.jp/gp/product/B097T6CBR6/ref=as_li_tl?ie=UTF8&tag=perlgenki-22&camp=247&creative=1211&linkCode=as2&creativeASIN=B097T6CBR6&linkId=e9078757396f4ceb239e325242bb830a"><img src="https://perlclub.net/images/book/perl_text_essence/perl_text_essence.jpg"></a>
        </div>
        <div class="side_list_description">
          <div >初級者向け・テキスト処理と正規表現の基本をマスター</div>
        </div>
      </li>
    </ul>
  </div>
</div>

<div class="side_list">
  <div class="side_list_title">
    業務に役立つPerl
  </div>
  <div class="side_list_body">
    <ul>
      <li>
        <div class="side_list_image">
          <a  rel="nofollow" href="https://perlclub.net/book/perl_gyoumu"><img src="https://perlclub.net/images/book/perl_gyoumu/perl_gyoumu.jpg"></a>
        </div>
        <div class="side_list_description">
          実務者向け・ログ解析など日本語を含むテキスト処理の実践!
        </div>
      </li>
    </ul>
  </div>
</div>

<div class="side_list">
  <div class="side_list_title">
    Perlクラブ
  </div>
  <div class="side_list_body">
    <ul>
      <li>
        <div class="side_list_image">
          <a rel="nofollow" href="https://perlclub.net/"><img style="width:130px" src="https://perlclub.net/images/perl_club_logo.png"></a>
        </div>
        <div class="side_list_description">
          仲間と出会い<br>ゆとりあるエンジニアライフを送る
        </div>
      </li>
    </ul>
  </div>
</div>

        </div>
      </div>
      <div class="footer">
        <div class="perlri_link">
  <a rel="nofollow" href="https://perlclub.net">Perlクラブ</a>
</div>

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4525414114581084"
     crossorigin="anonymous"></script>
     
      </div>
    </div>
  </body>
</html>
