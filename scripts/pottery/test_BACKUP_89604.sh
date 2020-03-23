#!/usr/bin/env bash

## run the test and export collapses
#--pool_res 600 450 300 180 \
python test.py \
--dataroot datasets/pottery5 \
--name pottery \
--ncf 64 128 256 256 \
<<<<<<< HEAD
--pool_res 750 600 450 230 \
=======
--pool_res 750 600 450 200 \
>>>>>>> 75f0c39aab9de7f56073ae9660215551d8ffef45
--norm group \
--resblocks 1 \
--export_folder meshes \
