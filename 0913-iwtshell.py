#!/bin/sh
#アプリまで移動する
cd /var/www/PhotoApp/iwphoto
#移動後マリアDBの起動
sudo systemctl start mariadb
sleep 20
#ユニコーンの起動
RAILS_SERVE_STATIC_FILES=1 unicorn_rails -c config/unicorn.rb -E production -D