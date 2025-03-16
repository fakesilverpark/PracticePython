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
    # champion = [champion for champion in _champions if champion.id == champion_id][0]
    # return champion

    # 구현하기4 : 리스트 컴프리핸션 + 오류 방지
    # 내가 원하는 아이디를 가진 Champion 이 리스트에 없으면 빈리스트가 반환됨
    # 위에건 빈리스트가 반환되었는데 0 번째 값을 찾으려고 해서 index error 가 발생했다
    # champion = [champion for champion in _champions if champion.id == champion_id]
    # if champion != []:
    #     return champion
    # else:
    #     return "Champion not found"

    # 구현하기5 : filter()
    # 해당 id 가 존재하지 않는 경우 사용이 어려움
    # champion_test = filter(lambda champion: champion.id == champion_id, _champions)
    # print(champion_test)

    # 구현하기6 : filter() + 오류 방지1
    # 내가 원하는 아이디를 가진 Champion 이 리스트에 없으면
    # 빈 필터 객체가 생성되고 이걸 리스트로 형변환하면 빈 리스트가 생긴다
    # 이걸 이용해서 위에 리스트 컴프리핸션 오류 해결 하듯이 오류 해결!
    # champion = list(filter(lambda champion: champion.id == champion_id, _champions))
    # if champion != []:
    #     return champion
    # else:
    #     return "Champion not found"
    # -> 하지만 이 코드는 비효율적
    # 쓸데없이 리스트로 형변환을 해야함!

    # 구현하기7 : filter() + 오류 방지2 (next())
    champion = next(filter(lambda champion: champion.id == champion_id, _champions), None)
    if champion:
        return champion
    return "Champion not found"

    # 기타1 : for 문을 이용
    # for champion in _champions:
    #     if champion.id == champion_id:
    #         return champion
    # return "Champion not found"

    # 기타2 : 딕셔너리 자료형 이용
    # _champions 가 매우 크면 O(1) 로 구할 수 있어서 더 좋을 수 있음
    # champions_dict = {champion.id: champion for champion in _champions}
    #
    # champion = champions_dict.get(champion_id, None)
    # if champion:
    #     return champion
    # return "Champion not found"
