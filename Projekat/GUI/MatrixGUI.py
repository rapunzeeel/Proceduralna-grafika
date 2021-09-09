def create_edges_height_map():
    edges = ()
    list_unallowed_neighbour_vertices = []
    for i in range(59, 3540, 60):
        list_unallowed_neighbour_vertices.append(i)
    for i in range(0, 3540):
        if i not in list_unallowed_neighbour_vertices:
            edges += ((i, i + 1),)
            edges += ((i, i + 60),)
            edges += ((i + 1, i + 60),)
            edges += ((i + 60, i + 61),)
        else:
            edges += ((i, i + 60),)
    for i in range(3540, 3599):
        edges += ((i, i + 1),)
    return edges


def create_surfaces_height_map(list_of_point):
    surfaces = ()
    list_unallowed = []
    for i in range(59, 3600, 60):
        list_unallowed.append(i)
    for i in range(len(list_of_point) - 60):
        if i not in list_unallowed:
            surfaces += ((i, i + 1, i + 60),)

    list_unallowed1 = []
    for i in range(60, 3600, 60):
        list_unallowed1.append(i)
    for i in range(len(list_of_point) - 1, 60, -1):
        if i not in list_unallowed1:
            surfaces += ((i, i - 1, i - 60),)
    return surfaces


def create_edges():
    edges = ()
    list_unallowed_neighbour_vertices = []
    for i in range(39, 1560, 40):
        list_unallowed_neighbour_vertices.append(i)
    for i in range(0, 1560):
        if i not in list_unallowed_neighbour_vertices:
            edges += ((i, i + 1),)
            edges += ((i, i + 40),)
            edges += ((i + 1, i + 40),)
            edges += ((i + 40, i + 41),)
        else:
            edges += ((i, i + 40),)
    for i in range(1560, 1599):
        edges += ((i, i + 1),)
    return edges


def create_surfaces(list_of_point):
    surfaces = ()
    list_unallowed = []
    for i in range(39, 1600, 40):
        list_unallowed.append(i)
    for i in range(len(list_of_point) - 40):
        if i not in list_unallowed:
            surfaces += ((i, i + 1, i + 40),)

    list_unallowed1 = []
    for i in range(40, 1600, 40):
        list_unallowed1.append(i)
    for i in range(len(list_of_point) - 1, 40, -1):
        if i not in list_unallowed1:
            surfaces += ((i, i - 1, i - 40),)
    return surfaces
