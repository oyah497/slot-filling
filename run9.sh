#!/bin/bash

#export CUDA_VISIBLE_DEVICES=0,1,2,3
export CUDA_VISIBLE_DEVICES=9
#export HF_HOME=/home/yanyang20/plms/cache
export HF_HOME=/data/local/oya/cache
#export HF_HOME=/export/App/training_platform/PinoModel/cache
# tgt_domains: AddToPlaylist BookRestaurant GetWeather PlayMusic RateBook SearchCreativeWork SearchScreeningEvent atis

#27
# 2181708042
# 3759554702
# 217193175

for shot_num in 0 20 50; do
  for tgt_domain in RateBook AddToPlaylist BookRestaurant GetWeather PlayMusic SearchCreativeWork SearchScreeningEvent atis; do
    poetry run python3 main.py $tgt_domain \
      --seed 2181708042 \
      --model-name facebook/bart-large \
      --batch-size 16 \
      --num-epochs 100 \
      --lr 5e-6 \
      --query-max-seq-length 128 \
      --response-max-seq-length 64 \
      --num-beams 2 \
      --query-schema nosep_rcsf_ex2_ab_or_wo_q \
      --response-schema nosep_rcsf_ex2_ab_or_wo_q \
      --shot-num $shot_num \
      --patience 5 \
      --dir-num 135
  done
done
