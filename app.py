import streamlit as st
import heapq
import pandas as pd

st.title("🚚 Delivery Optimization Model")
st.write("Enter distances and calculate shortest routes")

# USER INPUTS
st.sidebar.header("Enter Distances (in km)")

w_h1 = st.sidebar.number_input("Warehouse → Hub1", min_value=1, value=10)
w_h2 = st.sidebar.number_input("Warehouse → Hub2", min_value=1, value=15)
w_h3 = st.sidebar.number_input("Warehouse → Hub3", min_value=1, value=20)

h1_h2 = st.sidebar.number_input("Hub1 → Hub2", min_value=1, value=5)
h2_h3 = st.sidebar.number_input("Hub2 → Hub3", min_value=1, value=8)

# GRAPH
graph = {
    'Warehouse': {'Hub1': w_h1, 'Hub2': w_h2, 'Hub3': w_h3},
    'Hub1': {'Warehouse': w_h1, 'Hub2': h1_h2},
    'Hub2': {'Warehouse': w_h2, 'Hub1': h1_h2, 'Hub3': h2_h3},
    'Hub3': {'Warehouse': w_h3, 'Hub2': h2_h3}
}

# DIJKSTRA
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

# BUTTON
if st.button("🚀 Calculate Shortest Routes"):
    result = shortest_path(graph, 'Warehouse')

    st.subheader("📊 Results")

    df = pd.DataFrame(list(result.items()), columns=["Location", "Distance (km)"])
    st.table(df)

    st.subheader("📈 Graph")
    st.bar_chart(df.set_index("Location"))

# EXTRA INFO
st.markdown("---")
st.write("💡 Change values from sidebar to see different results")
