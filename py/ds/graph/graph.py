from icecream import ic

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)            
            else:
                self.graph_dict[start] = [end]
            
        # print(self.graph_dict)
        
    def get_path(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        
        for node in self.graph_dict[start]:
            if node not in paths:
                new_paths = self.get_path(start=node,end=end, path=path)
                for p in new_paths:
                    paths.append(p)
                    
        return paths
        
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortest_path = None
        
        for nodes in self.graph_dict[start]:
            if nodes not in path:
                sp = self.get_shortest_path(start=nodes, end=end, path=path)
                if sp:
                    if shortest_path is None or len(shortest_path) > len(sp):
                        shortest_path = sp

        return shortest_path
            
routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

route_graph = Graph(routes)

start = "Mumbai"
end = "Bangaluru"

# ic(route_graph.get_path(start=start, end=end))
ic(route_graph.get_shortest_path(start=start, end=end))