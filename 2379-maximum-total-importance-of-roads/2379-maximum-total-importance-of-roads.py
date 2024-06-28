class Solution(object):
    def maximumImportance(self, n, roads):
        city_connections = defaultdict(int)
        for a, b in roads:
            city_connections[a] += 1
            city_connections[b] += 1
        sorted_cities = sorted(city_connections.items(), key=lambda x: -x[1])
        value_assignment = {}
        current_value = n
        for city, _ in sorted_cities:
            value_assignment[city] = current_value
            current_value -= 1
        total_importance = 0
        for a, b in roads:
            total_importance += value_assignment[a] + value_assignment[b]
        return total_importance
solution = Solution()
print(solution.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
print(solution.maximumImportance(5, [[0,3],[2,4],[1,3]]))  