from dijsktra import Graph

map_edges_inter = [
    ('Vancouver', 'Boston', 561),
    ('Vancouver', 'New York', 683),
    ('Vancouver', 'Las Vegas', 327),
    ('Las Vegas', 'SLC',  69),
    ('Las Vegas', 'Los Angeles', 169),
    ('Las Vegas', 'New York', 617),
    ('Las Vegas', 'Chicago', 254),
    ('SLC', 'Los Angeles', 222),
    ('Las Vegas', "Ft Lauderdale", 99),
    ('Los Angeles', 'Ft Lauderdale', 676),
    ('Ft Lauderdale', 'Boston', 465),
    ('Ft Lauderdale', 'New York', 299),
    ('Boston', 'New York', 133),
    ('New York', 'Minneapolis', 237),
    ('Chicago', 'New York', 226),
]
    
def run_sample():
  edges = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'B', 3),
    ('A', 'D', 4),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('C', 'L', 2),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('G', 'H', 2),
    ('G', 'Y', 2),
    ('I', 'J', 6),
    ('I', 'K', 4),
    ('I', 'L', 4),
    ('J', 'L', 1),
    ('K', 'Y', 5),
  ]
  
  graph = Graph(edges)
  start = 'Y'
  stop = 'X'
  path = graph.dijsktra_shortest_path(start, stop)
  print (path)

def solve_dalg(edges, start, finish):
  graph = Graph(edges)
  path = graph.dijsktra_shortest_path(start, finish)
  print(f"The shortest path from {start} to {finish} is {path}")
  

def main():
  solve_dalg(map_edges_inter, "Los Angeles", "Chicago")
  solve_dalg(map_edges_inter, "Los Angeles", "Minneapolis")
  solve_dalg(map_edges_inter, "SLC", "Boston")

if __name__ == "__main__":
  main()
  