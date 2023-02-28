# This problem was asked by Snapchat.

#Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.

#For example, given [(30, 75), (0, 50), (60, 150)], you should return 2

import heapq  # importamos el módulo heapq para utilizar un heap


def min_rooms(intervals):
    if not intervals:  # si no hay intervalos, no necesitamos salones
        return 0

    intervals.sort(key=lambda x: x[0])  # ordenamos los intervalos por su tiempo de inicio
    heap = [intervals[0][1]]  # creamos un heap inicial con el tiempo de finalización del primer intervalo

    for interval in intervals[1:]:  # iteramos a través de los intervalos restantes
        if interval[0] >= heap[0]:  # si el tiempo de inicio del intervalo actual es mayor o igual que el menor
            # tiempo de finalización en el heap, podemos usar la misma sala
            heapq.heappop(heap)  # eliminamos el menor tiempo de finalización en el heap
        heapq.heappush(heap, interval[1])  # agregamos el tiempo de finalización del intervalo actual al heap

    return len(heap)  # devolvemos el número de salones necesarios (el tamaño del heap)

intervals = [(30, 75), (0, 50), (60, 150)]
num_rooms = min_rooms(intervals)
print(num_rooms)