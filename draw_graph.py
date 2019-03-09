
        with open('graph.csv', 'w', newline = '') as graph_csv:
            graph_csv_reader =  csv.writer(graph_csv, delimiter =',')
            for key, val in Vertex.graph.items():
                row = []
                row.append(key) #node
                for v in val:
                    row.append(v[0])
                graph_csv_reader.writerow(row) #write row

            # G = nx.read_adjlist(graph_csv, create_using = nx.DiGraph())
            # Load graph from CSV file with no header
        f = open('graph2.csv','rb')
        G = nx.read_adjlist(f, delimiter=',', nodetype=str)
        nx.draw(G, with_labels=True, node_size=200, node_color='c')
        # plt.show()
        plt.savefig('visualize_routes_10_p_nodes.png')
