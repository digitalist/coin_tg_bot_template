#!/bin/bash
cd $PWD
#sudo apt install dante-client
SOCKS5_SERVER=host:port SOCKS_USERNAME=example SOCKS_PASSWORD=password socksify python app.py
