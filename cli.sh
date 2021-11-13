#!/bin/bash

if [ $1 = "build" ] && [ $2 = "wget" ]; then
    sh cli.sh test
    wget -k -K -E -r -l 10 -p -N -F --restrict-file-names=windows -nH http://127.0.0.1:5000/
elif [ $1 = "test" ]; then
    coverage run -m --source=. pytest test.py -v
    coverage html
    pipreqs --savepath requirements.txt
fi
