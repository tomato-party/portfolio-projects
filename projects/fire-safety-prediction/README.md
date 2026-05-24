# Fire Safety Prediction

## Summary

화재 출동 데이터를 활용해 재산 피해 규모를 등급화하고, LightGBM 기반 예측 모델로 소방 안전 의사결정을 지원하는 프로젝트입니다.

## Problem

화재 발생 후 피해 규모를 빠르게 예측해 자원 배치와 대응 우선순위 판단에 도움을 줍니다.

## Approach

피해액 분위수 기반 A/B/C 등급화, 결측치 대체, 범주형 처리, LightGBM, RandomizedSearchCV

## Tech Stack

Python, pandas, LightGBM, scikit-learn

## Public Files
- $(Split-Path fire_predict.py -Leaf)`n
## Data Policy

Raw data is excluded from this public portfolio when it is large, competition-restricted, license-sensitive, or potentially private. Reproduction notes should use the official public data source where available.

## Interview Notes

- Explain why this problem matters.
- Walk through the preprocessing and modeling choices.
- Discuss evaluation metrics and what could be improved with more time.