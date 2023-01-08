"""Gardien de phare."""

def hauteurParcourue(nb, h) :
    print("Pour { :d} marches de { :d} cm, il parcourt { :.2f} m par semaine !"
         .format(nb, h, nb*h*2*5*7/100.0))

hauteurParcourue(20,5 )