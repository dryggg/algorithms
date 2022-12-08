from map_worker.map_visualization import MapVisualizator
from dijkstra.dijkstra import DijkstraAlgorithm
from datetime import datetime
from map_worker.map import GraphMap
import cv2

if __name__ == "__main__":
    start_point=(7,5)
    target_point=(30,19)

    show_weights_flag = True

    m = GraphMap(map_path="maps/map.txt")
    d = DijkstraAlgorithm()

    start_time = datetime.now()
    new_map: list = d.dijkstra_algorithm(m, start_point, target_point)
    finish_time = datetime.now()

    delta_time = finish_time - start_time
    print(delta_time.seconds)

    viz = MapVisualizator(show_weights=show_weights_flag)
    frame = viz.generate_map_frame(new_map)

    cv2.imshow("Map", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()