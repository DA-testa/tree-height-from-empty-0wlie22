import logging
import numpy as np
import sys
import threading


def get_height(nodes: np.array, height_array: np.array, node_index: int):
    current_node = nodes[node_index]
    current_height = height_array[node_index]

    if current_height != 0:
        return current_height
    if current_node == -1:
        height_array[node_index] = 1
    else:
        height_array[node_index] = get_height(nodes, height_array, nodes[node_index]) + 1

    return height_array[node_index]


def find_max_height(nodes: np.ndarray, node_count: int):
    height_array = np.zeros(node_count)

    for i in range(node_count):
        get_height(nodes, height_array, i)

    return int(max(height_array))


def main():
    method: str = input()[0]
    # method: str = "F"
    logger = logging.getLogger(__name__)
    match method:
        case "I":
            try:
                node_count = int(input())
                input_values: str = input()
                tree_values = list(map(input_values.split(" ")))
                if len(tree_values) != node_count:
                    raise ValueError("Error: node parent count does not match inputted node count")
            except ValueError as error:
                logger.error(error)
        case "F":
            file_name: str = input()

            # i: int = 1
            # while os.path.isfile(file_path + str(i).zfill(2)):
            #     with open(file_path + str(i).zfill(2), 'r') as file:
            #         node_count: int = int(file.readline())
            #         nodes: np.ndarray = np.array(list(map(int, file.readline().split(" "))))
            #         result: int = find_max_height(nodes, node_count)
            #     with open(file_path + str(i).zfill(2) + ".a", 'r') as file:
            #         answer: str = file.read().rstrip()
            #     if str(result) == str(answer):
            #         print(f"-> Test {i} passed!")
            #     else:
            #         print(f"-> Test {i} failed: expected '{answer}', got {result} instead")
            #
            #     i += 1
            if "a" in file_name:
                print("wrong file name: ")
            else:
                with open("test/" + file_name.zfill(2), 'r') as file:
                    node_count: int = int(file.readline())
                    nodes: np.ndarray = np.array(list(map(int, file.readline().split(" "))))
                    print(find_max_height(nodes, node_count))


sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start()
