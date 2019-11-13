#!/usr/bin/env bash

DATADIR='datasets' #location where data gets downloaded to

# get data
mkdir -p $DATADIR && cd $DATADIR
#wget https://www.dropbox.com/s/w16st84r6wc57u7/shrec_16.tar.gz
wget http://www.ipet.gr/~akoutsou/benchmark/dataset/3DPotteryDataset_v_1.zip

unzip 3DPotteryDataset_v_1.zip && rm 3DPotteryDataset_v_1.zip
echo "downloaded the data and putting it in: " $DATADIR
