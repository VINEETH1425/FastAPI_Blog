from typing import List,Tuple,Dict

# price: List[int]=[12,23,4,5]
# price: Tuple[int,int,int]=(1,2,4)
# price: Dict[str,int]={
#     "item1": 23,
#     "item2":4,
# }

# # in the above we have to import List,Tuple,Dict
# # but in the version 3.10 there is no necessary

# price: list[int]=[12,23,4,5]
# price: tuple[int,int,int]=(1,2,4)
# price: dict[str,int]={
#     "item1": 23,
#     "item2":4,
# }


from typing import Union,List
x : List[int | float] = [1.2,3,5.3]


from typing import Optional
from typing import List

class Job:
    def __init__(self, title: str, description: Optional[str]) -> None:
        self.title = title
        self.description = description

    def __repr__(self):
        return self.title

job1 = Job(title="Team Lead", description="Sdfdk")
job2 = Job(title="Senior Manager", description="jfdj")

jobs: List[Job] = [job1, job2]

from typing import List

Image = List[List[int]]

def flatten_image(pic: Image) -> List[int]:  # custom type Image
    flat_list = []
    for sublist in pic:
        for item in sublist:
            flat_list.append(item)
    return flat_list

image = [[1, 2, 3], [4, 5, 6]]


from typing import Callable

def smart_divide(func: Callable[[int, int], float]):
    def inner(a, b):
        if b == 0:
            print("Whoops! Division by 0")
            return None
        return func(a, b)
    return inner

# @smart_divide
def divide(a, b):
    print(a / b)

divide(9, 0)

