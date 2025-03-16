from typing import List

from practice.pr02.practice4_model import Champion, RoleEnum

_champions = [
    Champion(
        id=1,
        name="Champion1",
        release_date="2025-03-22",
        role=RoleEnum.ASSASSIN
    ),
    Champion(
            id=2,
            name="Champion2",
            release_date="2025-03-22",
            role=RoleEnum.FIGHTER
    )
]

def get_champion() -> List[Champion]:
    return _champions