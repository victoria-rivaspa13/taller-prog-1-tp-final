#!/bin/bash
curl -o server_log.txt https://gist.githubusercontent.com/sebiglesias/ea2faa92f4b25a79f811104584e91efb/raw/02378f041ae64d3d021031efeb1572cbddfc2fc7/test-web-server-log.txt

grep " 200 " server-log.txt >> ok.txt

grep " 500 " server-log.txt >> errors.txt

echo "Archivos ok.txt y errors.txt generados."
