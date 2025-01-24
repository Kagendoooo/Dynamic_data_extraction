import pygraphviz as pgv

# Create a new directed graph
graph = pgv.AGraph(strict=False, directed=True, bgcolor='#2B2B2B')

# Define table attributes for each node
def add_table_node(graph, table_name, fields, fillcolor, header_color):
    updated_fields = [f"🔑 {field}" if "(PK)" in field else field for field in fields]
    label = f"{table_name}\n" + "\n".join([f"{field}" for field in updated_fields])
    graph.add_node(
        table_name,
        shape='box',
        style='filled',
        fillcolor=fillcolor,
        fontname='Helvetica',
        fontsize=10,
        fontcolor='white',
        label=label,
    )

# Add nodes (representing tables)
add_table_node(
    graph,
    'Source',
    fields=[
        "id (PK)",
        "name",
        "base_url"
    ],
    fillcolor='#4A90E2',
    header_color='#003366'
)

add_table_node(
    graph,
    'Download',
    fields=[
        "id (PK)",
        "source_id (FK -> Source.id)",
        "url"
    ],
    fillcolor='#50E3C2',
    header_color='#00544E'
)

add_table_node(
    graph,
    'Document',
    fields=[
        "id (PK)",
        "title",
        "content",
        "download_id (FK -> Download.id)"
    ],
    fillcolor='#F5A623',
    header_color='#946200'
)

add_table_node(
    graph,
    'Chunk',
    fields=[
        "id (PK)",
        "content",
        "document_id (FK -> Document.id)",
        "start_position",
        "end_position"
    ],
    fillcolor='#D0021B',
    header_color='#660000'
)

# Add edges (representing relationships) with labels and styles
# Source to Download (one-to-many)
graph.add_edge('Source', 'Download', label='1:N', color='white', fontname='Helvetica', fontsize=10)

# Download to Document (one-to-many)
graph.add_edge('Download', 'Document', label='1:N', color='white', fontname='Helvetica', fontsize=10)

# Document to Chunk (one-to-many)
graph.add_edge('Document', 'Chunk', label='1:N', color='white', fontname='Helvetica', fontsize=10)

# Customize graph layout and attributes
graph.graph_attr.update(rankdir='LR', fontname='Helvetica', fontsize=12)
graph.node_attr.update(fontname='Helvetica', fontsize=10)
graph.edge_attr.update(fontname='Helvetica', fontsize=10)

# Render the graph to a file (e.g., PNG, PDF)
graph.layout(prog='dot')  # Use the 'dot' layout engine
graph.draw('Database_diagram.png')

print("Database diagram generated as 'Database_diagram.png'")
