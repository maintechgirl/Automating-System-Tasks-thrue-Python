#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
        echo "Everything is OK!"
else
        echo "ERROR! 127.0.0.1 is not en /etc/hosts"
fi
    

