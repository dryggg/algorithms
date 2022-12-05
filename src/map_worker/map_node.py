class NodeType:
    empty_point: int = 0
    start_point: int = -1
    target_point: int = -2

class Node:
    x: int                              # Координата х
    y: int                              # Координата у
    value: int                          # Вес перемещения в узел (0 - узел не существует)
    vizited: bool                       # Флаг, говорящий о том, посещен ли узел
    is_part_of_path: bool               # Флаг, говорящий о том, является ли узел частью найденного пути
    is_start_point: bool                # Флаг, говорящий о том, является ли узел стартовым узлом
    is_target_point: bool               # Флаг, говорящий о том, является ли узел финальным узлом

    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}, value: {self.value}, vizited: {self.vizited}, is_part_of_path: {self.is_part_of_path}, is_start_point: {self.is_start_point}, is_target_point: {self.is_target_point}"

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}, value: {self.value}, vizited: {self.vizited}, is_part_of_path: {self.is_part_of_path}, is_start_point: {self.is_start_point}, is_target_point: {self.is_target_point}"
