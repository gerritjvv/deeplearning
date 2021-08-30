#!/usr/bin/env bash


if [ ! -f "train-images-idx3-ubyte" ]; then

  curl -O http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
  curl -O http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz

  gunzip t*-ubyte.gz

fi