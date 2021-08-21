'''
import 뒤에는 패키지나 모듈
from import 뒤에는 클래스 가능
'''

# import travel.thailland
# trip_to=travel.thailland.Thailland_package()
# trip_to.detail()

# from travel import thailland
# trip_to=thailland.Thailland_package()
# trip_to.detail()

# from travel.thailland import Thailland_package
# trip_to=Thailland_package()
# trip_to.detail()

from travel import*
import inspect
trip_to=vietnam.Vietnam_package()
trip_to.detail()

# 모듈 경로 찾기
print(inspect.getfile(vietnam))

'''
모듈 다운
pypi 로 검색
pip install로 다운
pip show 로 설명 보기
pip install --upgrade 로 업데이트
pip uninstall로 삭제
'''

'''
dir을 쓰면 객체가 사용할 수 있는 기능 리스트를 알려줌

'''
