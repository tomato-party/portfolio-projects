# Real Estate Fraud Listing Classification

## Summary

부동산 매물 데이터를 활용해 허위매물 여부를 분류하는 Dacon 스타일 프로젝트입니다.

## Problem

매물 속성, 플랫폼, 중개사무소 등 다양한 피처를 활용해 허위매물을 사전에 식별합니다.

## Approach

결측치 처리, 인코딩, 피처 엔지니어링, XGBoost/LightGBM/RandomForest 비교

## Tech Stack

Python, pandas, scikit-learn, XGBoost, LightGBM

## Public Files
- $(Split-Path DF_겨울시즌_부동산허위매물_데이콘_한유승.ipynb -Leaf)`n- $(Split-Path 허위매물_lgbm.ipynb -Leaf)`n- $(Split-Path 23수정.ipynb -Leaf)`n
## Data Policy

Raw data is excluded from this public portfolio when it is large, competition-restricted, license-sensitive, or potentially private. Reproduction notes should use the official public data source where available.

## Interview Notes

- Explain why this problem matters.
- Walk through the preprocessing and modeling choices.
- Discuss evaluation metrics and what could be improved with more time.