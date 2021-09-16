<big>**FactorioCalcBase/data/** 에 위치하는 일부 게임 데이터는 **Wube Software**의 지적 재산입니다. 
  
이를 제외한 나머지는 MIT License에 따라 배포됩니다.</big>


# factorioCalcPy

<b>[HTTP API Demo](https://a.privatelaw.net/docs)</b>

<b>[Vue.js 기반 프론트엔드 Demo](https://fc.privatelaw.net)</b>

**Work In Progress**

**현재 개발중**

## 소개

게임 [Factorio](https://www.factorio.com/)의 자원, 생산품 의존성, 생산시설 비율 계산기입니다. 

C 깔짝, VB.net 깔짝, Java 깔짝 건드려보고 수년이 지난 초보가 맨땅에 헤딩하는 식으로 진행하는 프로젝트입니다.

깨달음을 얻을 때 마다 코드 구조가 뒤바뀝니다.

다른 사람이 이미 만들어놓은 코드 베끼지 않고 혼자 힘으로 완성하는게 목표입니다.

2021년 6월 말경 시작

## FactorioCalcBase
계산기의 본체입니다.

recipe를 기반으로 의존성 트리를 생성하고, 총 자원 필요량과 생산시설 필요량을 계산합니다.

[Plotly](https://github.com/plotly/plotly.py) 라이브러리를 이용하여 Sankey Diagram으로 자원의 흐름을 시각화할수 있습니다.

생산 시설의 종류와 생산량, 연구여부등의 변동 요소를 반영했습니다.

## FactorioCalcFastAPI
[FastAPI](https://fastapi.tiangolo.com/) 기반 http api입니다. 
