# Bayesian network for students
from pgmpy.models import BayesianModel
model = BayesianModel()
# Add nodes
model.add_nodes_from(['difficulty', 'intelligence', 'grade', 'sat', 'letter'])
print(model.nodes())
# Add edges
model.add_edges_from([('difficulty', 'grade'), ('intelligence', 'grade'), ('intelligence', 'sat'), ('grade', 'letter')])
print(model.edges())
