> <big>**FactorioCalcBase/data/** 에 위치하는 일부 게임 데이터는 <b>[Official Factorio Wiki](https://wiki.factorio.com/)</b>의 정보를 가공한 것으로, <b>[CC-BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)</b>으로 배포됩니다.


# factorioCalcPy

<b>[HTTP API Demo](https://a.privatelaw.net/docs)</b>

<b>[Vue.js 기반 프론트엔드 Demo](https://fc.privatelaw.net)</b>

**Work In Progress**

**현재 개발중**

## 소개

게임 [Factorio](https://www.factorio.com/)의 자원, 생산품 의존성, 생산시설 비율 계산기입니다. 

## FactorioCalcBase
계산기의 본체입니다.

recipe를 기반으로 의존성 트리를 생성하고, 총 자원 필요량과 생산시설 필요량을 계산합니다.

[Plotly](https://github.com/plotly/plotly.py) 라이브러리를 이용하여 Sankey Diagram으로 자원의 흐름을 시각화할수 있습니다.

생산 시설의 종류와 생산량, 연구여부등의 변동 요소를 반영했습니다.

## FactorioCalcFastAPI
[FastAPI](https://fastapi.tiangolo.com/) 기반 http api입니다. 
