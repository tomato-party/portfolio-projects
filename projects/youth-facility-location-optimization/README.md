# Youth Facility Location Optimization

## Summary

청소년 수요와 후보 입지를 기반으로 MCLP(Maximal Covering Location Problem)를 구현한 공공데이터 최적화 프로젝트입니다.

## Problem

한정된 시설 수로 더 많은 수요 지점을 커버할 수 있는 후보지를 찾습니다.

## Approach

위경도 기반 거리 계산, 수요/후보지 정의, Gurobi 최적화, Haversine 거리

## Tech Stack

Python, pandas, Gurobi, shapely, haversine

## Public Files
- $(Split-Path 구산동_MCLP_가중치_계산.ipynb -Leaf)`n
## Data Policy

Raw data is excluded from this public portfolio when it is large, competition-restricted, license-sensitive, or potentially private. Reproduction notes should use the official public data source where available.

## Interview Notes

- Explain why this problem matters.
- Walk through the preprocessing and modeling choices.
- Discuss evaluation metrics and what could be improved with more time.