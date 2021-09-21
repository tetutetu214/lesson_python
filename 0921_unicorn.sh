#!/bin/bash

#環境変数
RUBY_BIN=/home/ec2-user/.rbenv/shims/ruby
UNICORN_RAILS_BIN=/home/ec2-user/.rbenv/shims/unicorn_rails
MY_RAILS_ROOT=/var/www/PhotoApp/iwphoto
MY_UNICORN_CONFIG=config/unicorn.rb
MY_RAILS_ENV=production
RAILS_SERVE_STATIC_FILES=1

#コマンド
pushd $MY_RAILS_ROOT
$UNICORN_RAILS_BIN -c $MY_UNICORN_CONFIG -E $MY_RAILS_ENV -D