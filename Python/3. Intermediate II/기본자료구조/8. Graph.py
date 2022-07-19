from collections import deque
import heapq

# 그래프

# 1. 사용
# 연결관계가 있는 데이터

# 2. 용어 정리
# 노드 엣지 경로 인접 거리 싸이클 차수

# 3. 종류
# 무방향 그래프, 방향 그래프, 가중치 그래프

# 순회
# 1. dfs
# 2. bfs

# 최단거리
# 1. 임의의 어떤 두 노드 사이의 최단 거리를 모두 구할 때: 플로이드 워셜
# 2. 특정 노드에서 나머지 모든 임의의 노드로의 최단 거리를 구할때: 다익스트라(그래프를 인접 리스트로 만들고 푸는게 편리하다)
# 3. 특정 노드에서 특정 노드까지의 최단 거리를 구할 때: 에이스타(시험에 나오지 않는다)

# 우선 그래프를 만들어야 뭐라도 한다
# 1. 모든 노드를 배열에 넣으면 => 노드를 인덱스, 숫자로 생각할 수 있다
# => 1-1. 엣지 정보를 인접 행렬 방식으로 만들기
# => 1-2. 엣지 정보를 인접 리스트 방식으로 만들기

# 2. 모든 노드를 사전에 넣으면 => 노드를 숫자로 생각할 수 없다
# => 엣지 정보를 노드 안에 인접 노드 배열을 저장하는 방식으로 만들기(인접 리스트 방식과 동일하다)
####################################################################################################
# 1-1. 모든 노드를 배열에 넣으면 => 노드를 인덱스, 숫자로 생각할 수 있다
# => 엣지 정보를 인접 행렬 방식으로 만들기
INF = 1e9
graph = [
    [None, None, None, None],
    [None, 0, 1, 1],
    [None, 1, 0, INF],
    [None, 1, INF, 0]
]


def dfs(graph, visited, current_node):
    visited[current_node] = True
    print(current_node, end=' ')
    for i in range(len(graph[current_node])):
        if graph[current_node][i] != 1:
            continue
        if visited[i]:
            continue
        dfs(graph, visited, i)


def bfs(graph, visited, start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True

    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')
        for i in range(len(graph[current_node])):
            if graph[current_node][i] != 1:
                continue
            if visited[i]:
                continue
            queue.append(i)
            visited[i] = True


# visited = [False] * 4
# dfs(graph, visited, 1)
# visited = [False] * 4
# bfs(graph, visited, 1)
#################################################################################################################
# 1-2. 모든 노드를 배열에 넣으면 => 노드를 인덱스, 숫자로 생각할 수 있다
# => 엣지 정보를 인접 리스트 방식으로 만들기
graph = [
    None,
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]


def dfs(graph, visited, current_node):
    visited[current_node] = True
    print(current_node, end=' ')
    for next_node in graph[current_node]:
        if visited[next_node]:
            continue
        dfs(graph, visited, next_node)


def bfs(graph, visited, start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True

    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')
        for next_node in graph[current_node]:
            if visited[next_node]:
                continue
            queue.append(next_node)
            visited[next_node] = True


# visited = [False] * 9
# dfs(graph, visited, 1)
# visited = [False] * 9
# bfs(graph, visited, 1)
#################################################################################################################
# 2. 모든 노드를 사전에 넣으면 => 노드를 숫자로 생각할 수 없다
# => 엣지 정보를 노드 안에 인접 노드 배열을 저장하는 방식으로 만들기(인접 리스트 방식과 동잏하다)
class StationNode:
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []  # 인접 리스트 방식

    def __str__(self):
        result = self.station_name
        for adjacent_station in self.adjacent_stations:
            result += f"-{adjacent_station.station_name}"
        return result

    def add_connection(self, other_station):
        if other_station not in self.adjacent_stations:
            self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)


def create_station_graph(input_file):
    reader = open(input_file, mode="r", encoding="utf8")
    lines = reader.readlines()

    node_dictionary = {}
    for line in lines:
        line = line.strip().split("-")
        for i in range(len(line)):
            line[i] = line[i].strip()

        node_dictionary[line[0]] = StationNode(line[0])
        for i in range(1, len(line)):
            if line[i] not in node_dictionary.keys():
                new_station = StationNode(line[i])
                new_station.add_connection(node_dictionary[line[i - 1]])
                node_dictionary[line[i]] = new_station
            else:
                node_dictionary[line[i]].add_connection(node_dictionary[line[i - 1]])

    return node_dictionary



def dfs(graph, visited_dictionary, current_node):
    visited_dictionary[current_node.station_name] = True
    print(current_node.station_name, end=' ')
    for next_node in current_node.adjacent_stations:
        if visited_dictionary[next_node.station_name] == True:
            continue
        dfs(graph, visited_dictionary, next_node)


def bfs(graph, visited_dictionary, start_node):
    queue = deque()
    queue.append(start_node)
    visited_dictionary[start_node.station_name] = True
    while queue:
        current_node = queue.popleft()
        print(current_node.station_name, end=' ')
        for next_node in current_node.adjacent_stations:
            if visited_dictionary[next_node.station_name] == True:
                continue
            queue.append(next_node)
            visited_dictionary[next_node.station_name] = True


def dijkstra(graph, min_distance_dictionary, start_node):
    q = []
    heapq.heappush(q, [0, start_node.station_name])
    min_distance_dictionary[start_node.station_name] = 0

    while q:
        [dist, current_node_name] = heapq.heappop(q)
        if min_distance_dictionary[current_node_name] < dist:
            continue
        for next_node in graph[current_node_name].adjacent_stations:
            cost = min_distance_dictionary[current_node_name] + 1
            if cost < min_distance_dictionary[next_node.station_name]:
                min_distance_dictionary[next_node.station_name] = cost
                heapq.heappush(q, [cost, next_node.station_name])


graph = create_station_graph("../data/subway.txt")
# visited_dictionary = {}
# for key in graph:
#     visited_dictionary[key] = False
# dfs(graph, visited_dictionary, graph["선릉"])
# bfs(graph, visited_dictionary, graph["선릉"])
min_distance_dictionary = {}
INF = 1e9
for key in graph:
    min_distance_dictionary[key] = INF
dijkstra(graph, min_distance_dictionary, graph["선릉"])
print(min_distance_dictionary)
#################################################################################################################
# 1-2. 모든 노드를 배열에 넣으면 => 노드를 인덱스, 숫자로 생각할 수 있다
# => 엣지 정보를 인접 리스트 방식으로 만들기
# => 임의의 노드로부터 모든 노드까지의 모든 최단 거리를 구해보자 => 다익스트라 알고리즘 => 주로 인접 리스트 방식으로 구현한다

graph = [
    None,
    [[2, 2], [3, 5], [4, 1]],
    [[3, 3], [4, 2]],
    [[2, 3], [6, 5]],
    [[3, 3], [5, 1]],
    [[3, 1], [6, 2]],
    [],
]


def get_smallest_node(min_distances, visited):
    min_value = 1e9
    node_number = 1
    for i in range(1, len(min_distances)):
        if min_distances[i] < min_value and not visited[i]:
            min_value = min_distances[i]
            node_number = i

    return node_number


def dijkstra_slow_ver(graph, visited, min_distances, start_node):
    # 출발 노드를 처리한다
    min_distances[start_node] = 0
    visited[start_node] = True
    for next_node in graph[start_node]:
        min_distances[next_node[0]] = next_node[1]

    # 출발 노드를 제외한 나머지 모든 노드에 대해서 아래의 과정을 반복한다
    # 시간 복잡도 O(n^2)으로 느리다 => 우선순위 큐를 쓰면 O(n 로그 n)으로 개선할 수 있다
    for _ in range(len(min_distances) - 2):
        # 1. 아직 방문하지 않은 노드중에서 출발지로부터 최단거리인 노드를 방문한다
        current_node = get_smallest_node(min_distances, visited)
        visited[current_node] = True
        # 2. 현재 방문한 노드를 거쳐서 다른 노드로 가는 비용을 계산하여 최단 거리 배열을 갱신한다
        for next_node in graph[current_node]:
            cost = min_distances[current_node] + next_node[1]
            if cost < min_distances[next_node[0]]:
                min_distances[next_node[0]] = cost


def dijkstra_fast_ver(graph, min_distances, start_node):
    q = []
    heapq.heappush(q, [0, start_node])
    min_distances[start_node] = 0

    while q:
        [dist, current_node] = heapq.heappop(q)
        if min_distances[current_node] < dist:
            continue
        for next_node in graph[current_node]:
            cost = min_distances[current_node] + next_node[1]
            if cost < min_distances[next_node[0]]:
                min_distances[next_node[0]] = cost
                heapq.heappush(q, [cost, next_node[0]])


# INF = 1e9
# min_distances = [INF] * 7
# visited = [False] * 7
# dijkstra_slow_ver(graph, visited, min_distances, 1)
# print(min_distances)
#
# min_distances = [INF] * 7
# visited = [False] * 7
# dijkstra_fast_ver(graph, min_distances, 1)
# print(min_distances)

if __name__ == "__main__":
    pass