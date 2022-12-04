from map.map_visualization import MapVisualizator
from dijkstra.dijkstra import DijkstraAlgorithm
from map.map import GraphMap
import cv2

if __name__ == "__main__":
    start_point=(7,5)
    target_point=(0,0)
    m = GraphMap()
    d = DijkstraAlgorithm()
    target_path: list = d.dijkstra_algorithm(m, start_point, target_point)

    for node in target_path:
        node.is_part_of_path = True
        m.update_node(node)
    
    node = m.get_node_by_coord(start_point[0], start_point[1])
    node.is_start_point = True
    m.update_node(node)

    node = m.get_node_by_coord(target_point[0], target_point[1])
    node.is_target_point = True
    m.update_node(node)

    viz = MapVisualizator()
    frame = viz.generate_map_frame(m)
    print(type(frame))

    cv2.imshow("Map", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    