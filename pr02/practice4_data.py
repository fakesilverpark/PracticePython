from typing import List, Union

from practice.pr02.practice4_model import Champion, RoleEnum

_champions = [
    Champion(
        id=2,
        name="Champion1",
        release_date="2025-03-22",
        role=RoleEnum.ASSASSIN
    ),
    Champion(
            id=1,
            name="Champion2",
            release_date="2025-03-22",
            role=RoleEnum.FIGHTER
    )
]

def get_all_champions() -> List[Champion]:
    return _champions

# 매개변수로 온 아이디가 리스트에 존재하면 해당 객체를 리턴
# 없으면 None
def get_champion(champion_id: int) -> Union[Champion, str]:
    # 구현하기1 : next()
    # 못찾으면 StopIteration 예외 발생
    # champion = next(champion for champion in _champions if champion.id == champion_id)
    # return champion

    # 하지만 이 코드는 없어도 예외가 발생하면 안됨!!
    # 예외방지를 위하여 기본값 설정가능
    # 구현하기2 : next() + 예외방지설정
    # champion = next((champion for champion in _champions if champion.id == champion_id), None)
    # if champion is None:
    #     return "Champion not found"
    # return champion

    # 구현하기3 : 리스트 컴프리핸션
    # 해당 id 가 존재하지 않는 경우 사용이 어려움
    champion = [champion for champion in _champions if champion.id == champion_id][0]
    return champion