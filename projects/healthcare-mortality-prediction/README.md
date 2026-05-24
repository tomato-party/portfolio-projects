# Healthcare 48-hour Mortality Prediction

## Summary

MIMIC-IV 기반 48시간 사망 위험 예측 프로젝트입니다. 제한 데이터는 업로드하지 않고, 모델링 설계와 해석 중심으로 공개 가능한 내용만 정리했습니다.

## Problem

중환자/입원 환자의 단기 사망 위험을 예측해 임상 의사결정 보조 가능성을 탐색합니다.

## Approach

이상치 처리, 결측치 보정, resampling, XGBoost/LightGBM/CatBoost/Optuna, SHAP 해석

## Tech Stack

Python, pandas, scikit-learn, XGBoost, LightGBM, CatBoost, Optuna, SHAP

## Public Files
- $(Split-Path mimic-iv-3.1\DF_보건의료 test.ipynb -Leaf)`n
## Data Policy

Raw data is excluded from this public portfolio when it is large, competition-restricted, license-sensitive, or potentially private. Reproduction notes should use the official public data source where available.

## Interview Notes

- Explain why this problem matters.
- Walk through the preprocessing and modeling choices.
- Discuss evaluation metrics and what could be improved with more time.