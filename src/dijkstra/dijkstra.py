from map_worker.map_node import Node
from map_worker.map import GraphMap
from copy import copy
import numpy as np

class DijkstraNode:
    node: Node
    summ_weight: int
    path: list
    visited: bool

    def __init__(self, node: Node, summ_weight: int, path: list):
        self.node = node
        self.summ_weight = summ_weight
        self.path = path
        self.visited = False
    
    def add_to_path(self, node: Node) -> None:
        self.path.append(node)

    def __repr__(self) -> str:
        # return f"node: {self.node}, path: {self.path}"
        return str(self.summ_weight)

    def __str__(self) -> str:
        # return f"node: {self.node}, path: {self.path}"
        return str(self.path)

class DijkstraAlgorithm:
    def __init__(self):
        self.start_max_weight = 100000

    def dijkstra_algorithm(self, map: GraphMap, start_point: tuple, target_point: tuple) -> list:
        """Реализация поиска кратчайшего пути в графе по алгоритму Дейкстры

        Args:
            map (GraphMap): Карта в виде графа
            start_point (tuple): Координаты стартовой точки
            target_point (tuple): Координаты целевой точки

        Returns:
            list: Путь от стартовой к целевой точке
        """
        points_array: list = []

        # Словарь соответствия id ноды ее экземпляру
        correspondence_dict: dict = {}
        # Словарь соответствия экземпляра ноды ее id
        inverted_correspondence_dict: dict = {}

        counter: int = 0
        for line in map.map:
            for node in line:
                if node.value != 0:
                    correspondence_dict[counter] = node
                    inverted_correspondence_dict[node] = counter
                    counter += 1
        
        for i in range(len(map.map)):
            for j in range(len(map.map[i])):
                if map.map[i][j].value != 0:
                    points_array.append(DijkstraNode(map.map[i][j], self.start_max_weight, []))
        
        start_point_node: Node = map.get_node_by_coord(start_point[0], start_point[1])
        start_point_node_number: int = inverted_correspondence_dict[start_point_node]
        points_array[start_point_node_number] = DijkstraNode(start_point_node, 0, [start_point_node])
        
        current_node: Node = start_point_node

        # Флаг, говорящий о том, есть ли еще непосещенные узлы
        unvisited_node_found_flag = True

        while unvisited_node_found_flag:
            current_node_id: int = inverted_correspondence_dict[current_node]
            neighbors: list = map.get_all_neighbors(current_node)
            for neighbor in neighbors:
                neighbor_id: int = inverted_correspondence_dict[neighbor]
                if points_array[neighbor_id].summ_weight > neighbor.value + points_array[current_node_id].summ_weight:
                    points_array[neighbor_id].summ_weight = neighbor.value + points_array[current_node_id].summ_weight
                    points_array[neighbor_id].path = copy(points_array[current_node_id].path)
                    points_array[neighbor_id].add_to_path(neighbor)

                points_array[current_node_id].visited = True
            sorted_array = self.__sort_dijkstra_nodes_array(points_array)
            unvisited_node_found_flag = False
            for dijkstra_node in sorted_array:
                if not dijkstra_node.visited:
                    current_node = dijkstra_node.node
                    unvisited_node_found_flag = True
                    break

        target_node: Node = map.get_node_by_coord(target_point[0], target_point[1])
        target_node_id: int = inverted_correspondence_dict[target_node]

        return points_array[target_node_id].path

    def __sort_dijkstra_nodes_array(self, dijkstra_node_array: list) -> list:
        """Функция для сортировки массива из объектов DijkstraNode по суммарному весу

        Args:
            dijkstra_node_array (list(DijkstraNode)): Массив из объектов DijkstraNode

        Returns:
            list(DijkstraNode): Отсортированный массив из объектов DijkstraNode
        """
        new_array: list = []
        for elem in dijkstra_node_array:
            if not elem.visited and elem.summ_weight < self.start_max_weight:
                new_array.append(elem)

        for i in range(len(new_array)-1):
            for j in range(len(new_array)-i-1):
                if new_array[j].summ_weight > new_array[j+1].summ_weight:
                    new_array[j], new_array[j+1] = new_array[j+1], new_array[j]
        return new_array