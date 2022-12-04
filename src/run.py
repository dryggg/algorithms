from map.map_visualization import MapVisualizator
from map.map import GraphMap
import cv2

if __name__ == "__main__":
    m = GraphMap()
    
    node = m.get_node_by_coord(3,6)
    node.is_start_point = True
    m.update_node(node)

    node = m.get_node_by_coord(32,15)
    node.is_target_point = True
    m.update_node(node)

    viz = MapVisualizator()
    frame = viz.generate_map_frame(m)
    print(type(frame))

    cv2.imshow("Map", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()