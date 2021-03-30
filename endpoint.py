from cnvrg import Endpoint
def predict(*args):
    e = Endpoint()
    res = args[0]*2
    print("got {}".format(res))
    e.log_metric("accuracy", res)
    return res
