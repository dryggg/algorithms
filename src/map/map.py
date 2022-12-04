import numpy as np
import map_node

class Map:
    map: np.ndarray
    weight: int
    height: int

    def __init__(self):
        txt_map: np.ndarray = self.__read_txt_map(file_path="map.txt")      
        self.map = self.__generate_graph_map(txt_map)                       # Сама карта с узлами
        self.height = len(self.map)                                         # Высота карты
        self.weight = len(self.map[0])                                      # Ширина карты

    def __read_txt_map(self, file_path: str) -> np.ndarray:
        """Функция для чтения конфигурации карты из файла .txt и перевода ее в массив numpy

        Args:
            file_path (str): Путь к файлу с конфигурацией карты

        Returns:
            np.ndarray: Двумерный массив numpy, содержащий конфигурацию карты
        """
        array: list = []
        with open(file_path, "r") as map:
            for line in map:
                if "\n" in line:
                    line: str = line[:len(line) - len("\n")]
                array.append(line.split(" "))
        
        return np.array(array)

    def __generate_graph_map(self, txt_map: np.ndarray) -> np.ndarray:
        """Функция для генерации карты, состоящей из узлов графа

        Args:
            txt_map (np.ndarray): Массив, содержащий карту, считанную из конфигуровочного .txt файла

        Returns:
            np.ndarray: Массив, содержащий карту в виде ущлов графа
        """
        graph_map: list = []
        for i in range(len(txt_map)):
            graph_map.append([])
            for j in range(len(txt_map[i])):
                new_node: map_node.Node = map_node.Node()
                new_node.x = j
                new_node.y = i
                new_node.value = int(txt_map[i][j])

                graph_map[-1].append(new_node)
        
        return np.array(graph_map)

    def check_if_node_inside_map(self, x: int, y: int) -> bool:
        """Функция для проверки попадания координат узла в границы карты

        Args:
            x (int): x координата узла
            y (int): y координата узла

        Returns:
            bool: Флаг попадания координат узла в границы карты
        """
        if x >= 0 and x <= self.weight - 1 and y >= 0 and y <= self.height - 1:
            return True
        return False

    def check_if_node_exists(self, x: int, y: int) -> bool:
        """Функция для проверки существования узла

        Args:
            x (int): x координата узла
            y (int): y координата узла

        Returns:
            bool: Флаг существования узла
        """
        if self.check_if_node_inside_map(x, y):
            if self.map[y][x].value != 0:
                return True
        return False

    def get_node_by_coord(self, x: int, y: int) -> map_node.Node:
        """Функция для получения узла по его координатам

        Args:
            x (int): x координата узла
            y (int): y координата узла

        Returns:
            map_node.Node: Экземпляр узла или None, в случае его отсутствия
        """
        if self.check_if_node_exists(x, y):
            return self.map[y][x]
        return None

    def get_node_neighbor(self, node: map_node.Node, neighbor_type: str) -> map_node.Node:
        """Функция для получения узла-соседа

        Args:
            node (map_node.Node): Узел, для которого ищется сосед
            neighbor_type (str): Тип соседа (left, right, top, bottom)

        Returns:
            map_node.Node: Узел-сосед или None, в случае его отсутствия
        """
        assert type(node) == map_node.Node, "Node object can't be None type"

        if neighbor_type == "left":
            return self.get_node_by_coord(x=node.x-1, y=node.y)
        elif neighbor_type == "right":
            return self.get_node_by_coord(x=node.x+1, y=node.y)
        elif neighbor_type == "top":
            return self.get_node_by_coord(x=node.x, y=node.y-1)
        elif neighbor_type == "bottom":
            return self.get_node_by_coord(x=node.x, y=node.y+1)

        return None

if __name__ == "__main__":
    m = Map()
    print(m.get_node_neighbor(node=m.get_node_by_coord(35,20), neighbor_type="bottom"))
