#!/bin/bash

for ((i=0; i<$2; i++)) ; do
    wget -r -N $1 &
done