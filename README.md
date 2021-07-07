# factorioCalcPy
Factorio calculator

recipe.lua - 일부 수정한 lua 테이블 형식 팩토리오 레시피 데이터\n
luarecipeconvert.py - recipe.lua를 파이썬 딕셔너리로 변환\n
writerecipepy.py - luarecipeconvert.py로 변환된 딕셔너리를 json 포맷과 유사한 파이썬 딕셔너리 형식 파일로 저장. 편리한 열람, 수정과 추후 웹기반 구현 편의를 위함\n
recipe.py - 결과물, 의존성 추적, 재료 계산의 바탕이 됨.\n
\n

dependencydictbuilder.py - 딕셔너리 형식으로 의존성 트리와 재료 계산을 구현하려던 시도, 현재 중단\n
\n
factorioItemClass.py - factorioItem이라는 클래스 생성, makeChild() 메소드를 포함한 객체로 의존성 트리 생성을 간소화, 현재 개발중\n
\n

main.py - 테스트 목적\n
