#!/bin/bash

#export CUDA_VISIBLE_DEVICES=0,1,2,3
export CUDA_VISIBLE_DEVICES=9
#export HF_HOME=/home/yanyang20/plms/cache
export HF_HOME=/data/local/oya/cache
#export HF_HOME=/export/App/training_platform/PinoModel/cache
# tgt_domains: AddToPlaylist BookRestaurant GetWeather PlayMusic RateBook SearchCreativeWork SearchScreeningEvent atis

for shot_num in 0 20 50; do
  for tgt_domain in AddToPlaylist BookRestaurant GetWeather PlayMusic RateBook SearchCreativeWork SearchScreeningEvent; do
    poetry run python3 main.py $tgt_domain \
      --seed 0 \
      --model-name facebook/bart-base \
      --batch-size 16 \
      --num-epochs 100 \
      --lr 6e-6 \
      --query-max-seq-length 128 \
      --response-max-seq-length 64 \
      --num-beams 2 \
      --query-schema without_example \
      --response-schema each_slot_dummy \
      --shot-num $shot_num \
      --patience 5
  done
done
