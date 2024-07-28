DATA = {'graph': None, 'Pi': None}

class Constants:
    lambda_ = None
    K = None

def initialize(graph, Pi):
    DATA['graph'] = graph
    DATA['Pi'] = Pi

    Constants.lambda_ = sum(w for _, _, w in DATA['graph'].edges)
    Constants.K = len(DATA['Pi'])
