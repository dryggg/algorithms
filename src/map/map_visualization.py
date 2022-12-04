from .map import GraphMap
import numpy as np
import cv2

class MapVisualizator:
    def __init__(self):
        self.max_window_width: int = 2000                           # Максимальная ширина окна
        self.max_window_height: int = 1200                          # Максимальная высота окна
        self.edge_indent: int = 25                                  # Отступ от края
        self.max_node_side_size: int = 40                           # Максимальный размер квадрата

        self.node_square_border_color: tuple = (0, 0, 0)            # Цвет границы квадрата, обозначающего узел
        self.node_square_border_thickness: int = 1                  # Толщина грани квадрата, обозначающего узел

        self.node_square_color: tuple = (220, 220, 220)             # Цвет квадрата, обозначающего узел
        self.visited_node_square_color: tuple = (179, 255, 251)     # Цвет квадрата, обозначающего посещенный узел
        self.path_node_square_color: tuple = (179, 179, 255)        # Цвет квадрата, обозначающего узел, являющийся частью найденного пути
        self.start_node_square_color: tuple = (111, 255, 0)         # Цвет квадрата, обозначающего стартовый узел
        self.target_node_square_color: tuple = (0, 0, 251)          # Цвет квадрата, обозначающего целевой узел

    def __find_window_size(self, map: GraphMap) -> list:
        """Функция для нахождения оптимального размера окна визуализации

        Args:
            map (GraphMap): Визуализируемая карта

        Returns:
            list: Массив, состоящий из ширины и высоты окна визуализации и длины стороны квадрата, визуализирующего узел
        """
        node_side_size = self.max_node_side_size
        while node_side_size != 0:
            if map.width*node_side_size + 2*self.edge_indent < self.max_window_width and map.height*node_side_size + 2*self.edge_indent < self.max_window_height:
                window_width: int = map.width*node_side_size + 2*self.edge_indent
                window_height: int = map.height*node_side_size + 2*self.edge_indent

                return window_width, window_height, node_side_size

            node_side_size -= 1
        
        assert False, "Too big map"

    def generate_map_frame(self, map: GraphMap) -> np.ndarray:
        """Функция для создания кадра визуализации на основании полученной карты

        Args:
            map (GraphMap): Карта для визуализации

        Returns:
            np.ndarray: Кадр для отображения
        """
        window_width, window_height, node_side_size = self.__find_window_size(map)

        frame: np.ndarray = np.zeros((window_height, window_width, 3), np.uint8)
        frame.fill(255)

        for line in map.map:
            for node in line:
                point1: tuple = (self.edge_indent + node_side_size*node.x, self.edge_indent + node_side_size*node.y)
                point2: tuple = (self.edge_indent + node_side_size*(node.x+1), self.edge_indent + node_side_size*(node.y+1))

                if node.value != 0:
                    # Заполненный кварат с цветом, соответствующим типу узла
                    if node.is_start_point:
                        cv2.rectangle(frame, point1, point2, self.start_node_square_color, -1)
                    elif node.is_target_point:
                        cv2.rectangle(frame, point1, point2, self.target_node_square_color, -1)
                    elif node.is_part_of_path:
                        cv2.rectangle(frame, point1, point2, self.path_node_square_color, -1)
                    elif node.vizited:
                        cv2.rectangle(frame, point1, point2, self.visited_node_square_color, -1)
                    else:
                        cv2.rectangle(frame, point1, point2, self.node_square_color, -1)
                    
                    # Граница квадрата
                    cv2.rectangle(frame, point1, point2, self.node_square_border_color, self.node_square_border_thickness)
                else:
                    cv2.rectangle(frame, point1, point2, self.node_square_border_color, -1)
        
        return frame