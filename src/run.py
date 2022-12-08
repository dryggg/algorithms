from map_worker.map_visualization import MapVisualizator
from dijkstra import DijkstraAlgorithm
from a_star import AStarAlgorithm
from datetime import datetime
from map_worker.map import GraphMap
import cv2

if __name__ == "__main__":
    #* OPTIONS:
    #* IF YOU WANT TO CHANGE ALGORITHM - CHANGE SELECTED CLASS BELOW (AVAILABLE: AStarAlgorithm(), DijkstraAlgorithm())
    selected_algorithm = DijkstraAlgorithm()
    start_point=(7,5)
    target_point=(30,19)
    show_weights_flag = True
    map_path = "maps/map.txt"
    m = GraphMap(map_path=map_path)

    start_time = datetime.now()
    new_map: list = selected_algorithm.algorithm(m, start_point, target_point)
    finish_time = datetime.now()

    delta_time = finish_time - start_time
    print(f"Execution time: {delta_time.seconds}")

    viz = MapVisualizator(show_weights=show_weights_flag)
    frame = viz.generate_map_frame(new_map)

    cv2.imshow("Map", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()