#!/bin/bash

echo "=== userprofile ==="

ROOT_DIR=/var/www/PhotoApp/iwphoto
RAILS_SERVE_STATIC_FILES=1
UNI_DIR=/home/ec2-user/.rbenv/shims/unicorn_rails
CMD=${UNI_DIR} -c config/unicorn.rb -E production -D

echo "=== unicorncommand ==="
cd $ROOT_DIR && $CMD

echo "=== mkdir ==="
cd $ROOT_DIR && mkdir sample

echo "=== log ==="
echo $(curl http://169.254.169.254/latest/meta-data/instance-id) >> /tmp/test