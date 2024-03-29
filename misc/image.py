from graphviz import Digraph

# Create a new Digraph
dot = Digraph()

# Add nodes (processes)
dot.node('A', 'Enter login credentials')
dot.node('B', 'Validate Credentials')
dot.node('C', 'Authenticate User')
dot.node('D', 'Select disease for prediction')
dot.node('E', 'Submit prediction request')
dot.node('F', 'Display prediction result')

# Add edges (data flows) with labels
dot.edge('A', 'B', label='Login credentials (username, password)')
dot.edge('B', 'C', label='Authentication request')
dot.edge('C', 'F', label='User authentication status')
dot.edge('D', 'E', label='Disease selection')
dot.edge('E', 'F', label='Prediction request (selected disease)')

# Render and display the flow diagram
dot.render('flow_diagram', format='png', cleanup=True)
