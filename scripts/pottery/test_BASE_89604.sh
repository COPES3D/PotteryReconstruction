#!/usr/bin/env bash

## run the test and export collapses
#--pool_res 600 450 300 180 \
python test.py \
--dataroot datasets/pottery7 \
--name pottery \
--ncf 64 128 256 256 \
--pool_res 750 600 450 250 \
--norm group \
--resblocks 1 \
--export_folder meshes \