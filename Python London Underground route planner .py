import sys
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):

        # Allows the graph to become symetrical with edges going in both directions with the same time
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if finder(node, adjacent_node):
                    pass
                else:
                    if graph[adjacent_node].get(node, False) == False:
                        graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        # returns nodes
        return self.nodes

    def get_outgoing_edges(self, node):
        # returns neighbours of given node
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
    shortest_path = {}

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}

    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0

    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + \
                graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def finder(a, b):
    n = 0
    all_keys = list(init_graph.keys())
    while len(all_keys)-1 > n:
        if (all_keys[n] == a and all_keys[n+1] == b) or (all_keys[n] == b and all_keys[n-1] == a) or (all_keys[n] == b and all_keys[n+1] == a) or (all_keys[n] == a and all_keys[n-1] == b):
            return True
        n = n+1
    return False


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start_node)

    print("The total journey time is {} minutes.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


# *** ALL STATIONS ***
nodes = \
    [  # BAKERLOO
        "Harrow & Wealdstone", "Kenton", "South Kenton", "North Wembley", "Wembley Central", "Stonebridge Park", "Harlesden",
        "Willesden Junction", "Kensal Green", "Queen's Park", "Kilburn Park", "Maida Vale", "Warwick Avenue", "Paddington",
        "Edgware Road", "Marylebone", "Baker Street", "Regent's Park", "Oxford Circus", "Piccadilly Circus",
        "Charing Cross B", "Embankment", "Waterloo", "Lambeth North", "Elephant & Castle",
        # CENTRAL
        "Epping", "Theydon Bois", "Debden", "Loughton ", "Buckhurst Hill", "Woodford", "South Woodford", "Snaresbrook ",
        "Roding Valley", "Chigwell", "Grange Hill", "Hainault", "Fairlop", "Barkingside", "Newbury Park", "Gants Hill",
        "Redbridge", "Wanstead", "Leytonstone", "Leyton", "Stratford", "Mile End", "Bethnal Green", "Liverpool Street", "Bank",
        "St. Paul's", "Chancery Lane", "Holborn", "Tottenham Court Road", "Oxford Circus", "Bond Street", "Marble Arch",
        "Lancaster Gate", "Queensway", "Notting Hill Gate", "Holland Park", "Shepherd's Bush", "White City", "East Acton",
        "North Acton", "West Acton", "Ealing Broadway", "Hanger Lane ", "Perivale", "Greenford", "Northolt ", "South Ruislip",
        "Ruislip Gardens", "West Ruislip",

        # CIRCLE
        "Edgware Road ", "Paddington", "Bayswater", "Notting Hill Gate", "High Street Kensington", "Gloucester Road",
        "South Kensington", "Sloane Square", "Victoria", "St. James's Park", "Westminster", "Embankment", "Temple", "Blackfriars",
        "Mansion House", "Cannon Street", "Monument", "Tower Hill", "Aldgate", "Liverpool Street", "Moorgate", "Barbican",
        "Farringdon", "King's Cross St. Pancras", "Euston Square", "Great Portland Street", "Baker Street", "Royal Oak ",
        "Westbourne Park ", "Ladbroke Grove ", "Latimer Road ", "Wood Lane ", "Shepherd's Bush Market ", "Goldhawk Road ",
        "Hammersmith ",

        # DISTRICT
        "Upminster", "Upminster Bridge", "Hornchurch", "Elm Park", "Dagenham East", "Dagenham Heathway", "Becontree", "Upney",
        "Barking", "East Ham", "Upton Park", "Plaistow", "West Ham", "Bromley-by-Bow", "Bow Road", "Mile End", "Stepney Green",
        "Whitechapel", "Aldgate East", "Tower Hill", "Monument", "Cannon Street", "Mansion House", "Blackfriars", "Temple",
        "Embankment", "Westminster", "St. James's Park", "Victoria", "Sloane Square", "South Kensington", "Gloucester Road",
        "Earl's Court", "Kensington (Olympia)", "High Street Kensington", "Notting Hill Gate", "Bayswater", "Paddington",
        "Edgware Road", "West Brompton", "Fulham Broadway", "Parsons Green", "Putney Bridge", "East Putney", "Southfields",
        "Wimbledon Park", "Wimbledon", "West Kensington", "Barons Court", "Hammersmith", "Ravenscourt Park", "Stamford Brook",
        "Turnham Green", "Gunnersbury", "Kew Gardens", "Richmond ", "Chiswick Park", "Acton Town", "Ealing Common",
        "Ealing Broadway",

        #HAMMERSMITH & CITY
        "Barking", "East Ham", "Upton Park", "Plaistow", "West Ham", "Bromley-by-Bow", "Bow Road", "Mile End", "Stepney Green",
        "Whitechapel", "Aldgate East", "Liverpool Street", "Moorgate", "Barbican", "Farringdon", "King's Cross St. Pancras",
        "Euston Square", "Great Portland Street", "Baker Street", "Edgware Road", "Paddington", "Royal Oak", "Westbourne Park",
        "Ladbroke Grove", "Latimer Road", "Wood Lane", "Shepherd's Bush Market", "Goldhawk Road", "Hammersmith",

        # JUBILEE
        "Stanmore", "Canons Park", "Queensbury", "Kingsbury", "Wembley Park", "Neasden", "Dollis Hill", "Willesden Green",
        "Kilburn", "West Hampstead", "Finchley Road", "Swiss Cottage", "St. John's Wood", "Baker Street", "Bond Street",
        "Green Park", "Westminster", "Waterloo", "Southwark", "London Bridge", "Bermondsey", "Canada Water", "Canary Wharf",
        "North Greenwich", "Canning Town", "West Ham", "Stratford",

        # METROPOLITAN
        "Amersham", "Chesham", "Chalfont & Latimer", "Chorleywood", "Rickmansworth", "Watford", "Croxley", "Uxbridge", "Hillingdon",
        "Ickenham", "Ruislip", "Ruislip Manor", "Eastcote", "Rayners Lane", "West Harrow", "Harrow-on-the-Hill", "North Harrow",
        "Pinner", "Northwood Hills", "Northwood", "Moor Park", "Northwick Park", "Preston Road", "Wembley Park", "Finchley Road",
        "Baker Street", "Great Portland Street", "Euston Square", "King's Cross St. Pancras", "Farringdon", "Barbican",
        "Moorgate", "Liverpool Street", "Aldgate",

        # NORTHERN
        "High Barnet", "Totteridge & Whetstone", "Woodside Park", "West Finchley", "Mill Hill East", "Finchley Central",
        "East Finchley", "Highgate", "Archway", "Tufnell Park", "Kentish Town", "Edgware", "Burnt Oak", "Colindale",
        "Hendon Central", "Brent Cross", "Golders Green", "Hampstead", "Belsize Park", "Chalk Farm", "Camden Town",
        "Mornington Crescent", "Warren Street", "Goodge Street", "Tottenham Court Road", "Leicester Square", "Charing Cross N",
        "Embankment", "Waterloo", "Euston", "King's Cross St. Pancras", "Angel", "Old Street", "Moorgate", "Bank", "London Bridge",
        "Borough", "Elephant & Castle", "Kennington", "Oval", "Stockwell", "Clapham North", "Clapham Common", "Clapham South",
        "Balham", "Tooting Bec", "Tooting Broadway", "Colliers Wood", "South Wimbledon", "Morden ",

        # PICCADILLY
        "Cockfosters", "Oakwood", "Southgate", "Arnos Grove", "Bounds Green", "Wood Green", "Turnpike Lane", "Manor House",
        "Finsbury Park Victoria", "Arsenal", "Holloway Road", "Caledonian Road", "King's Cross St. Pancras", "Russell Square",
        "Holborn Central", "Covent Garden", "Leicester Square", "Piccadilly Circus", "Green Park", "Hyde Park Corner",
        "Knightsbridge", "South Kensington", "Gloucester Road", "Earl's Court", "Barons Court", "Hammersmith", "Turnham Green",
        "Acton Town", "South Ealing", "Northfields", "Boston Manor", "Osterley", "Hounslow East", "Hounslow Central",
        "Hounslow West", "Hatton Cross", "Heathrow Terminals 1, 2, 3", "Heathrow Terminal 5", "Heathrow Terminal 4",
        "Ealing Common", "North Ealing", "Park Royal", "Alperton", "Sudbury Town", "Sudbury Hill", "South Harrow", "Rayners Lane",
        "Eastcote", "Ruislip Manor", "Ruislip", "Ickenham", "Hillingdon", "Uxbridge",

        # VICTORIA
        "Walthamstow Central", "Blackhorse Road", "Tottenham Hale", "Seven Sisters", "Finsbury Park", "Highbury & Islington",
        "King's Cross St. Pancras", "Euston", "Warren Street", "Oxford Circus", "Green Park", "Victoria", "Pimlico", "Vauxhall",
        "Stockwell", "Brixton",


        #WATERLOO & CITY
        "Bank", "Waterloo", ]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

# *** ALL STATION CONNECTIONS***
# BAKERLOO
init_graph["Harrow & Wealdstone"]["Kenton"] = 2
init_graph["Kenton"]["South Kenton"] = 2
init_graph["South Kenton"]["North Wembley"] = 2
init_graph["North Wembley"]["Wembley Central"] = 2
init_graph["Wembley Central"]["Stonebridge Park"] = 2
init_graph["Stonebridge Park"]["Harlesden"] = 2
init_graph["Harlesden"]["Willesden Junction"] = 2
init_graph["Willesden Junction"]["Kensal Green"] = 3
init_graph["Kensal Green"]["Queen's Park"] = 2
init_graph["Queen's Park"]["Kilburn Park"] = 2
init_graph["Kilburn Park"]["Maida Vale"] = 2
init_graph["Maida Vale"]["Warwick Avenue"] = 1
init_graph["Warwick Avenue"]["Paddington"] = 2
init_graph["Paddington"]["Edgware Road"] = 2
init_graph["Edgware Road"]["Marylebone"] = 1
init_graph["Marylebone"]["Baker Street"] = 2
init_graph["Baker Street"]["Regent's Park"] = 2
init_graph["Regent's Park"]["Oxford Circus"] = 2
init_graph["Oxford Circus"]["Piccadilly Circus"] = 2
init_graph["Piccadilly Circus"]["Charing Cross B"] = 2
init_graph["Charing Cross B"]["Embankment"] = 1
init_graph["Embankment"]["Waterloo"] = 2
init_graph["Waterloo"]["Lambeth North"] = 2
init_graph["Lambeth North"]["Elephant & Castle"] = 3

# CENTRAL
init_graph["Epping"]["Theydon Bois"] = 3
init_graph["Theydon Bois"]["Debden"] = 3
init_graph["Debden"]["Loughton "] = 2
init_graph["Loughton "]["Buckhurst Hill"] = 3
init_graph["Buckhurst Hill"]["Woodford"] = 2
init_graph["Woodford"]["South Woodford"] = 3
init_graph["South Woodford"]["Snaresbrook "] = 2
init_graph["Snaresbrook "]["Leytonstone"] = 2
init_graph["Roding Valley"]["Woodford"] = 4
init_graph["Roding Valley"]["Chigwell"] = 3
init_graph["Chigwell"]["Grange Hill"] = 2
init_graph["Grange Hill"]["Hainault"] = 5
init_graph["Hainault"]["Fairlop"] = 2
init_graph["Fairlop"]["Barkingside"] = 2
init_graph["Barkingside"]["Newbury Park"] = 2
init_graph["Newbury Park"]["Gants Hill"] = 3
init_graph["Gants Hill"]["Redbridge"] = 2
init_graph["Redbridge"]["Wanstead"] = 2
init_graph["Wanstead"]["Leytonstone"] = 2
init_graph["Leytonstone"]["Leyton"] = 2
init_graph["Leyton"]["Stratford"] = 3
init_graph["Stratford"]["Mile End"] = 4
init_graph["Mile End"]["Bethnal Green"] = 2
init_graph["Bethnal Green"]["Liverpool Street"] = 3
init_graph["Liverpool Street"]["Bank"] = 2
init_graph["Bank"]["St. Paul's"] = 2
init_graph["St. Paul's"]["Chancery Lane"] = 2
init_graph["Chancery Lane"]["Holborn"] = 1
init_graph["Holborn"]["Tottenham Court Road"] = 2
init_graph["Tottenham Court Road"]["Oxford Circus"] = 1
init_graph["Oxford Circus"]["Bond Street"] = 2
init_graph["Bond Street"]["Marble Arch"] = 2
init_graph["Marble Arch"]["Lancaster Gate"] = 3
init_graph["Lancaster Gate"]["Queensway"] = 2
init_graph["Queensway"]["Notting Hill Gate"] = 2
init_graph["Notting Hill Gate"]["Holland Park"] = 1
init_graph["Holland Park"]["Shepherd's Bush"] = 2
init_graph["Shepherd's Bush"]["White City"] = 3
init_graph["White City"]["East Acton"] = 3
init_graph["East Acton"]["North Acton"] = 2
init_graph["North Acton"]["Hanger Lane "] = 3
init_graph["North Acton"]["West Acton"] = 2
init_graph["West Acton"]["Ealing Broadway"] = 3
init_graph["Hanger Lane "]["Perivale"] = 3
init_graph["Perivale"]["Greenford"] = 2
init_graph["Greenford"]["Northolt "] = 2
init_graph["Northolt "]["South Ruislip"] = 3
init_graph["South Ruislip"]["Ruislip Gardens"] = 2
init_graph["Ruislip Gardens"]["West Ruislip"] = 2

# CIRCLE
init_graph["Edgware Road "]["Paddington"] = 3
init_graph["Paddington"]["Bayswater"] = 2
init_graph["Bayswater"]["Notting Hill Gate"] = 2
init_graph["Notting Hill Gate"]["High Street Kensington"] = 2
init_graph["High Street Kensington"]["Gloucester Road"] = 3
init_graph["Gloucester Road"]["South Kensington"] = 3
init_graph["South Kensington"]["Sloane Square"] = 2
init_graph["Sloane Square"]["Victoria"] = 2
init_graph["Victoria"]["St. James's Park"] = 2
init_graph["St. James's Park"]["Westminster"] = 2
init_graph["Westminster"]["Embankment"] = 1
init_graph["Embankment"]["Temple"] = 2
init_graph["Temple"]["Blackfriars"] = 1
init_graph["Blackfriars"]["Mansion House"] = 2
init_graph["Mansion House"]["Cannon Street"] = 2
init_graph["Cannon Street"]["Monument"] = 1
init_graph["Monument"]["Tower Hill"] = 2
init_graph["Tower Hill"]["Aldgate"] = 2
init_graph["Aldgate"]["Liverpool Street"] = 3
init_graph["Liverpool Street"]["Moorgate"] = 2
init_graph["Moorgate"]["Barbican"] = 2
init_graph["Barbican"]["Farringdon"] = 1
init_graph["Farringdon"]["King's Cross St. Pancras"] = 4
init_graph["King's Cross St. Pancras"]["Euston Square"] = 2
init_graph["Euston Square"]["Great Portland Street"] = 2
init_graph["Great Portland Street"]["Baker Street"] = 2
init_graph["Baker Street"]["Edgware Road "] = 3
init_graph["Paddington"]["Royal Oak "] = 2
init_graph["Royal Oak "]["Westbourne Park "] = 2
init_graph["Westbourne Park "]["Ladbroke Grove "] = 2
init_graph["Ladbroke Grove "]["Latimer Road "] = 2
init_graph["Latimer Road "]["Wood Lane "] = 2
init_graph["Wood Lane "]["Shepherd's Bush Market "] = 2
init_graph["Shepherd's Bush Market "]["Goldhawk Road "] = 1
init_graph["Goldhawk Road "]["Hammersmith "] = 2

# DISTRICT
init_graph["Upminster"]["Upminster Bridge"] = 2
init_graph["Upminster Bridge"]["Hornchurch"] = 2
init_graph["Hornchurch"]["Elm Park"] = 2
init_graph["Elm Park"]["Dagenham East"] = 3
init_graph["Dagenham East"]["Dagenham Heathway"] = 2
init_graph["Dagenham Heathway"]["Becontree"] = 3
init_graph["Becontree"]["Upney"] = 2
init_graph["Upney"]["Barking"] = 3
init_graph["Barking"]["East Ham"] = 4
init_graph["East Ham"]["Upton Park"] = 2
init_graph["Upton Park"]["Plaistow"] = 2
init_graph["Plaistow"]["West Ham"] = 2
init_graph["West Ham"]["Bromley-by-Bow"] = 2
init_graph["Bromley-by-Bow"]["Bow Road"] = 2
init_graph["Bow Road"]["Mile End"] = 2
init_graph["Mile End"]["Stepney Green"] = 2
init_graph["Stepney Green"]["Whitechapel"] = 3
init_graph["Whitechapel"]["Aldgate East"] = 2
init_graph["Aldgate East"]["Tower Hill"] = 3
init_graph["Tower Hill"]["Monument"] = 2
init_graph["Monument"]["Cannon Street"] = 1
init_graph["Cannon Street"]["Mansion House"] = 2
init_graph["Mansion House"]["Blackfriars"] = 2
init_graph["Blackfriars"]["Temple"] = 1
init_graph["Temple"]["Embankment"] = 2
init_graph["Embankment"]["Westminster"] = 1
init_graph["Westminster"]["St. James's Park"] = 2
init_graph["St. James's Park"]["Victoria"] = 2
init_graph["Victoria"]["Sloane Square"] = 2
init_graph["Sloane Square"]["South Kensington"] = 2
init_graph["South Kensington"]["Gloucester Road"] = 3
init_graph["Gloucester Road"]["Earl's Court"] = 2
init_graph["Earl's Court"]["Kensington (Olympia)"] = 3
init_graph["Earl's Court"]["High Street Kensington"] = 5
init_graph["High Street Kensington"]["Notting Hill Gate"] = 2
init_graph["Notting Hill Gate"]["Bayswater"] = 2
init_graph["Bayswater"]["Paddington"] = 2
init_graph["Paddington"]["Edgware Road"] = 3
init_graph["Earl's Court"]["West Brompton"] = 2
init_graph["West Brompton"]["Fulham Broadway"] = 2
init_graph["Fulham Broadway"]["Parsons Green"] = 2
init_graph["Parsons Green"]["Putney Bridge"] = 3
init_graph["Putney Bridge"]["East Putney"] = 3
init_graph["East Putney"]["Southfields"] = 2
init_graph["Southfields"]["Wimbledon Park"] = 2
init_graph["Wimbledon Park"]["Wimbledon"] = 4
init_graph["Earl's Court"]["West Kensington"] = 2
init_graph["West Kensington"]["Barons Court"] = 2
init_graph["Barons Court"]["Hammersmith"] = 3
init_graph["Hammersmith"]["Ravenscourt Park"] = 2
init_graph["Ravenscourt Park"]["Stamford Brook"] = 2
init_graph["Stamford Brook"]["Turnham Green"] = 1
init_graph["Turnham Green"]["Gunnersbury"] = 3
init_graph["Gunnersbury"]["Kew Gardens"] = 2
init_graph["Kew Gardens"]["Richmond "] = 4
init_graph["Turnham Green"]["Chiswick Park"] = 2
init_graph["Chiswick Park"]["Acton Town"] = 2
init_graph["Acton Town"]["Ealing Common"] = 2
init_graph["Ealing Common"]["Ealing Broadway"] = 5

#HAMMERSMITH & CITY
init_graph["Barking"]["East Ham"] = 4
init_graph["East Ham"]["Upton Park"] = 2
init_graph["Upton Park"]["Plaistow"] = 2
init_graph["Plaistow"]["West Ham"] = 2
init_graph["West Ham"]["Bromley-by-Bow"] = 2
init_graph["Bromley-by-Bow"]["Bow Road"] = 2
init_graph["Bow Road"]["Mile End"] = 2
init_graph["Mile End"]["Stepney Green"] = 2
init_graph["Stepney Green"]["Whitechapel"] = 3
init_graph["Whitechapel"]["Aldgate East"] = 2
init_graph["Aldgate East"]["Liverpool Street"] = 3
init_graph["Liverpool Street"]["Moorgate"] = 2
init_graph["Moorgate"]["Barbican"] = 2
init_graph["Barbican"]["Farringdon"] = 1
init_graph["Farringdon"]["King's Cross St. Pancras"] = 4
init_graph["King's Cross St. Pancras"]["Euston Square"] = 2
init_graph["Euston Square"]["Great Portland Street"] = 2
init_graph["Great Portland Street"]["Baker Street"] = 2
init_graph["Baker Street"]["Edgware Road"] = 3
init_graph["Edgware Road"]["Paddington"] = 3
init_graph["Paddington"]["Royal Oak"] = 2
init_graph["Royal Oak"]["Westbourne Park"] = 2
init_graph["Westbourne Park"]["Ladbroke Grove"] = 2
init_graph["Ladbroke Grove"]["Latimer Road"] = 2
init_graph["Latimer Road"]["Wood Lane"] = 2
init_graph["Wood Lane"]["Shepherd's Bush Market"] = 2
init_graph["Shepherd's Bush Market"]["Goldhawk Road"] = 1
init_graph["Goldhawk Road"]["Hammersmith"] = 2

# JUBILEE
init_graph["Stanmore"]["Canons Park"] = 4
init_graph["Canons Park"]["Queensbury"] = 3
init_graph["Queensbury"]["Kingsbury"] = 2
init_graph["Kingsbury"]["Wembley Park"] = 3
init_graph["Wembley Park"]["Neasden"] = 4
init_graph["Neasden"]["Dollis Hill"] = 2
init_graph["Dollis Hill"]["Willesden Green"] = 2
init_graph["Willesden Green"]["Kilburn"] = 2
init_graph["Kilburn"]["West Hampstead"] = 2
init_graph["West Hampstead"]["Finchley Road"] = 1
init_graph["Finchley Road"]["Swiss Cottage"] = 2
init_graph["Swiss Cottage"]["St. John's Wood"] = 2
init_graph["St. John's Wood"]["Baker Street"] = 3
init_graph["Baker Street"]["Bond Street"] = 2
init_graph["Bond Street"]["Green Park"] = 2
init_graph["Green Park"]["Westminster"] = 2
init_graph["Westminster"]["Waterloo"] = 2
init_graph["Waterloo"]["Southwark"] = 2
init_graph["Southwark"]["London Bridge"] = 2
init_graph["London Bridge"]["Bermondsey"] = 2
init_graph["Bermondsey"]["Canada Water"] = 2
init_graph["Canada Water"]["Canary Wharf"] = 3
init_graph["Canary Wharf"]["North Greenwich"] = 3
init_graph["North Greenwich"]["Canning Town"] = 3
init_graph["Canning Town"]["West Ham"] = 3
init_graph["West Ham"]["Stratford"] = 2

# METROPOLITAN
init_graph["Amersham"]["Chalfont & Latimer"] = 4
init_graph["Chesham"]["Chalfont & Latimer"] = 9
init_graph["Chalfont & Latimer"]["Chorleywood"] = 4
init_graph["Chorleywood"]["Rickmansworth"] = 4
init_graph["Rickmansworth"]["Moor Park"] = 5
init_graph["Watford"]["Croxley"] = 4
init_graph["Croxley"]["Moor Park"] = 4
init_graph["Uxbridge"]["Hillingdon"] = 4
init_graph["Hillingdon"]["Ickenham"] = 2
init_graph["Ickenham"]["Ruislip"] = 2
init_graph["Ruislip"]["Ruislip Manor"] = 2
init_graph["Ruislip Manor"]["Eastcote"] = 2
init_graph["Eastcote"]["Rayners Lane"] = 2
init_graph["Rayners Lane"]["West Harrow"] = 3
init_graph["West Harrow"]["Harrow-on-the-Hill"] = 2
init_graph["Harrow-on-the-Hill"]["North Harrow"] = 3
init_graph["North Harrow"]["Pinner"] = 2
init_graph["Pinner"]["Northwood Hills"] = 3
init_graph["Northwood Hills"]["Northwood"] = 3
init_graph["Northwood"]["Moor Park"] = 3
init_graph["Moor Park"]["Harrow-on-the-Hill"] = 14
init_graph["Harrow-on-the-Hill"]["Finchley Road"] = 16
init_graph["Harrow-on-the-Hill"]["Wembley Park"] = 9
init_graph["Harrow-on-the-Hill"]["Northwick Park"] = 3
init_graph["Northwick Park"]["Preston Road"] = 3
init_graph["Preston Road"]["Wembley Park"] = 3
init_graph["Wembley Park"]["Finchley Road"] = 7
init_graph["Finchley Road"]["Baker Street"] = 5
init_graph["Baker Street"]["Great Portland Street"] = 2
init_graph["Great Portland Street"]["Euston Square"] = 2
init_graph["Euston Square"]["King's Cross St. Pancras"] = 2
init_graph["King's Cross St. Pancras"]["Farringdon"] = 2
init_graph["Farringdon"]["Barbican"] = 4
init_graph["Barbican"]["Moorgate"] = 2
init_graph["Moorgate"]["Liverpool Street"] = 2
init_graph["Liverpool Street"]["Aldgate"] = 3

# NORTHERN
init_graph["High Barnet"]["Totteridge & Whetstone"] = 4
init_graph["Totteridge & Whetstone"]["Woodside Park"] = 2
init_graph["Woodside Park"]["West Finchley"] = 2
init_graph["West Finchley"]["Finchley Central"] = 2
init_graph["Mill Hill East"]["Finchley Central"] = 4
init_graph["Finchley Central"]["East Finchley"] = 4
init_graph["East Finchley"]["Highgate"] = 3
init_graph["Highgate"]["Archway"] = 3
init_graph["Archway"]["Tufnell Park"] = 2
init_graph["Tufnell Park"]["Kentish Town"] = 1
init_graph["Kentish Town"]["Camden Town"] = 2
init_graph["Edgware"]["Burnt Oak"] = 4
init_graph["Burnt Oak"]["Colindale"] = 2
init_graph["Colindale"]["Hendon Central"] = 3
init_graph["Hendon Central"]["Brent Cross"] = 2
init_graph["Brent Cross"]["Golders Green"] = 3
init_graph["Golders Green"]["Hampstead"] = 4
init_graph["Hampstead"]["Belsize Park"] = 3
init_graph["Belsize Park"]["Chalk Farm"] = 2
init_graph["Chalk Farm"]["Camden Town"] = 1
init_graph["Camden Town"]["Mornington Crescent"] = 2
init_graph["Mornington Crescent"]["Euston"] = 2
init_graph["Warren Street"]["Euston"] = 1
init_graph["Warren Street"]["Goodge Street"] = 2
init_graph["Goodge Street"]["Tottenham Court Road"] = 1
init_graph["Tottenham Court Road"]["Leicester Square"] = 2
init_graph["Leicester Square"]["Charing Cross N"] = 1
init_graph["Charing Cross N"]["Embankment"] = 1
init_graph["Embankment"]["Waterloo"] = 2
init_graph["Waterloo"]["Kennington"] = 3
init_graph["Euston"]["Camden Town"] = 4
init_graph["Euston"]["King's Cross St. Pancras"] = 2
init_graph["King's Cross St. Pancras"]["Angel"] = 3
init_graph["Angel"]["Old Street"] = 3
init_graph["Old Street"]["Moorgate"] = 2
init_graph["Moorgate"]["Bank"] = 2
init_graph["Bank"]["London Bridge"] = 2
init_graph["London Bridge"]["Borough"] = 2
init_graph["Borough"]["Elephant & Castle"] = 2
init_graph["Elephant & Castle"]["Kennington"] = 2
init_graph["Kennington"]["Oval"] = 3
init_graph["Oval"]["Stockwell"] = 2
init_graph["Stockwell"]["Clapham North"] = 2
init_graph["Clapham North"]["Clapham Common"] = 2
init_graph["Clapham Common"]["Clapham South"] = 2
init_graph["Clapham South"]["Balham"] = 2
init_graph["Balham"]["Tooting Bec"] = 2
init_graph["Tooting Bec"]["Tooting Broadway"] = 2
init_graph["Tooting Broadway"]["Colliers Wood"] = 2
init_graph["Colliers Wood"]["South Wimbledon"] = 2
init_graph["South Wimbledon"]["Morden "] = 3

# PICCADILLY
init_graph["Cockfosters"]["Oakwood"] = 2
init_graph["Oakwood"]["Southgate"] = 3
init_graph["Southgate"]["Arnos Grove"] = 4
init_graph["Arnos Grove"]["Bounds Green"] = 2
init_graph["Bounds Green"]["Wood Green"] = 3
init_graph["Wood Green"]["Turnpike Lane"] = 2
init_graph["Turnpike Lane"]["Manor House"] = 4
init_graph["Manor House"]["Finsbury Park Victoria"] = 2
init_graph["Finsbury Park Victoria"]["Arsenal"] = 1
init_graph["Arsenal"]["Holloway Road"] = 2
init_graph["Holloway Road"]["Caledonian Road"] = 2
init_graph["Caledonian Road"]["King's Cross St. Pancras"] = 4
init_graph["King's Cross St. Pancras"]["Russell Square"] = 2
init_graph["Russell Square"]["Holborn Central"] = 2
init_graph["Holborn Central"]["Covent Garden"] = 2
init_graph["Covent Garden"]["Leicester Square"] = 1
init_graph["Leicester Square"]["Piccadilly Circus"] = 1
init_graph["Piccadilly Circus"]["Green Park"] = 2
init_graph["Green Park"]["Hyde Park Corner"] = 2
init_graph["Hyde Park Corner"]["Knightsbridge"] = 2
init_graph["Knightsbridge"]["South Kensington"] = 2
init_graph["South Kensington"]["Gloucester Road"] = 2
init_graph["Gloucester Road"]["Earl's Court"] = 2
init_graph["Earl's Court"]["Barons Court"] = 3
init_graph["Barons Court"]["Hammersmith"] = 3
init_graph["Hammersmith"]["Acton Town"] = 8
init_graph["Hammersmith"]["Turnham Green"] = 4
init_graph["Turnham Green"]["Acton Town"] = 4
init_graph["Acton Town"]["South Ealing"] = 3
init_graph["South Ealing"]["Northfields"] = 1
init_graph["Northfields"]["Boston Manor"] = 2
init_graph["Boston Manor"]["Osterley"] = 3
init_graph["Osterley"]["Hounslow East"] = 2
init_graph["Hounslow East"]["Hounslow Central"] = 1
init_graph["Hounslow Central"]["Hounslow West"] = 3
init_graph["Hounslow West"]["Hatton Cross"] = 4
init_graph["Hatton Cross"]["Heathrow Terminals 1, 2, 3"] = 4
init_graph["Heathrow Terminals 1, 2, 3"]["Heathrow Terminal 5"] = 4
init_graph["Hatton Cross"]["Heathrow Terminal 4"] = 3
init_graph["Acton Town"]["Ealing Common"] = 2
init_graph["Ealing Common"]["North Ealing"] = 2
init_graph["North Ealing"]["Park Royal"] = 2
init_graph["Park Royal"]["Alperton"] = 2
init_graph["Alperton"]["Sudbury Town"] = 3
init_graph["Sudbury Town"]["Sudbury Hill"] = 2
init_graph["Sudbury Hill"]["South Harrow"] = 3
init_graph["South Harrow"]["Rayners Lane"] = 5
init_graph["Rayners Lane"]["Eastcote"] = 2
init_graph["Eastcote"]["Ruislip Manor"] = 2
init_graph["Ruislip Manor"]["Ruislip"] = 2
init_graph["Ruislip"]["Ickenham"] = 4
init_graph["Ickenham"]["Hillingdon"] = 2
init_graph["Hillingdon"]["Uxbridge"] = 4

# VICTORIA
init_graph["Walthamstow Central"]["Blackhorse Road"] = 3
init_graph["Blackhorse Road"]["Tottenham Hale"] = 3
init_graph["Tottenham Hale"]["Seven Sisters"] = 2
init_graph["Seven Sisters"]["Finsbury Park"] = 5
init_graph["Finsbury Park"]["Highbury & Islington"] = 2
init_graph["Highbury & Islington"]["King's Cross St. Pancras"] = 3
init_graph["King's Cross St. Pancras"]["Euston"] = 2
init_graph["Euston"]["Warren Street"] = 2
init_graph["Warren Street"]["Oxford Circus"] = 2
init_graph["Oxford Circus"]["Green Park"] = 2
init_graph["Green Park"]["Victoria"] = 2
init_graph["Victoria"]["Pimlico"] = 2
init_graph["Pimlico"]["Vauxhall"] = 2
init_graph["Vauxhall"]["Stockwell"] = 3
init_graph["Stockwell"]["Brixton"] = 2

#WATERLOO & CITY
init_graph["Bank"]["Waterloo"] = 5


graph = Graph(nodes, init_graph)
def match_node(name):
    for n in nodes:
        if n.strip().lower() == name.strip().lower():
            return n
    return name

depart = match_node(input("Enter Departue Station:"))
arrival = match_node(input("Enter Arrival Station:"))
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=depart)
try:

    print_result(previous_nodes, shortest_path,
                 start_node=depart, target_node=arrival)
except:
    print("No Alternate route present!")
