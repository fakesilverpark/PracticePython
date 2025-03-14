from typing import List, Tuple, Dict, Optional, Union

# def function_name(value: type) -> return_type:

def add(a: int, b: int) -> int:
    return a + b

def process_number(numbers: List[int]) -> List[int]:
    new_numbers = [number * 2 for number in numbers]
    return new_numbers

def get_person_info() -> Tuple[str, int]:
    return ("Park", 18)

def get_student_score() -> Dict[str, float]:
    return { "gaeun" : "100.0" }

# Optional[type]은 type 또는 None을 가질 수 있는 타입
def find_user(user_id: int) -> Optional[str]:
    users = {1 : "a", 2 : "b", 3: "c"}
    return users.get(user_id)

# Union[type1, type2] type1 또는 type2 만 가능
# 둘 중 어디에도 해당하지 않는다면 TypeError 발생
def function(value: Union[str, int]) -> int:
    if (isinstance(value, int)):
        return value ** 2
    return len(value)

if __name__ == "__main__":
    print(add(1, 2))
    print(add("1", "2"))
    print(process_number([1, 2, 3]))
    print(get_person_info())
    print(get_student_score())
    print(find_user(1))
    print(find_user(8))
    print(function(2))
    print(function("hello world"))

# 3
# 12
# [2, 4, 6]
# ('Park', 18)
# {'gaeun': '100.0'}
# a
# None
# 4
# 11