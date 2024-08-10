DATA = {'graph': None}

class Constants:
    lambda_ = None
    K = None

def initialize(graph):
    DATA['graph'] = graph

    Constants.lambda_ = sum(w for _, _, w in DATA['graph'].edges)
