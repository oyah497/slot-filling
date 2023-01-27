#!/bin/bash

#export CUDA_VISIBLE_DEVICES=0,1,2,3
export CUDA_VISIBLE_DEVICES=4
#export HF_HOME=/home/yanyang20/plms/cache
export HF_HOME=/data/local/oya/cache
#export HF_HOME=/export/App/training_platform/PinoModel/cache
# tgt_domains: AddToPlaylist BookRestaurant GetWeather PlayMusic RateBook SearchCreativeWork SearchScreeningEvent atis

# 4

# 2181708042
# 3759554702
# 217193175

for shot_num in 0; do
  for tgt_domain in PlayMusic RateBook SearchCreativeWork SearchScreeningEvent; do
    poetry run python3 main.py $tgt_domain \
      --seed 3759554702 \
      --model-name facebook/bart-large \
      --batch-size 16 \
      --num-epochs 100 \
      --lr 5e-6 \
      --query-max-seq-length 128 \
      --response-max-seq-length 64 \
      --num-beams 2 \
      --query-schema ablation4 \
      --response-schema ablation4 \
      --shot-num $shot_num \
      --patience 5 \
      --dir-num 193
  done
done
