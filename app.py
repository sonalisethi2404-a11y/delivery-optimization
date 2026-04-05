import streamlit as st
import heapq
import pandas as pd

st.title("🚚 E-commerce Delivery Optimization")

st.write("Find shortest delivery routes from Warehouse to Hubs")

# Graph input
graph = {
    'Warehouse': {'Hub1': 10, 'Hub2': 15, 'Hub3': 20},
    'Hub1': {'Warehouse': 10, 'Hub2': 5},
    'Hub2': {'Warehouse': 15, 'Hub1': 5, 'Hub3': 8},
    'Hub3': {'Warehouse': 20, 'Hub2': 8}
}

# Dijkstra Algorithm
def shortest_path(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Button to run model
if st.button("Calculate Shortest Routes"):
    result = shortest_path(graph, 'Warehouse')

    st.subheader("📊 Results")

    # Convert to DataFrame
    df = pd.DataFrame(list(result.items()), columns=["Location", "Distance (km)"])

    st.table(df)

    # Bar Chart
    st.subheader("📈 Distance Visualization")
    st.bar_chart(df.set_index("Location"))

st.markdown("---")
st.write("Developed using Streamlit for Mathematical Modelling Project")
