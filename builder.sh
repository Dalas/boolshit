#!/usr/bin/env bash


echo `date +%Y-%m-%d.%H:%M:%S`': Start deploy' >> bash-log.txt

# locale bug
export LC_ALL=C

echo `date +%Y-%m-%d.%H:%M:%S`': Install python requirements' >> bash-log.txt
pip3 install -r requirements.txt

echo `date +%Y-%m-%d.%H:%M:%S`': Finish deploy' >> bash-log.txt
echo '================================================' >> bash-log.txt

exit 0
