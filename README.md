# factorioCalcPy

C 깔짝, VB.net 깔짝, Java 깔짝 건드려보고 수년이 지난 초보가 맨땅에 헤딩하는 식으로 진행하는 프로젝트입니다.

제대로 코딩을 해본건 이게 처음입니다.

깨달음을 얻을 때 마다 코드 구조가 뒤바뀝니다.

다른 사람이 이미 만들어놓은 코드 베끼지 않고 혼자 힘으로 완성하는게 목표입니다.

https://gall.dcinside.com/mgallery/board/view/?id=factorio&no=36503

2021년 6월 말경 시작

<h2>FactorioCalcBase</h2>
계산기의 본체입니다.

recipe를 기반으로 의존성 트리를 생성하고, 총 자원 필요량과 생산시설 필요량을 계산합니다.

생산 속도와 생산량, 연구여부에 따른 변동 요소를 반영했습니다.

<h2>FactorioCalcFastAPI</h2>
[**FastAPI**](https://fastapi.tiangolo.com/) 기반 API입니다.
Vue.js 기반 프론트엔드와 결합할 예정입니다.