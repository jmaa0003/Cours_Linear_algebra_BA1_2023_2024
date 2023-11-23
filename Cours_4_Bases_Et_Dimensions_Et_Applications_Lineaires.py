"""
Cours du chapitre 2 sur les bases et la dimension ainsi que les applications linéaires
"""
def Base(G):
    return 'partie génératrice et libre de V'

Exemples_de_bases = {'\{0\} : ensemble vide', 'R[X] : une des bases est la partie B = \{X^i | i ∈ N\} = \{1, X, X^2, ..., X^n, ...\}', \
                     'R^n : {\{les bases canoniques\}',  '\{les bases canoniques\} tq (1,1, 0, ...), (1,1,1, 0, ...)', \
                     'les matrices K^n*m : E_k,l = partout 0 comme composante sauf sur la k-ième ligne et la l-ième colonne, avec 1'}


def Applications_Lineaires(G_notre_fameux_espace_vectoriel):
    return 'f : V -> V\' admet que f(⋋v + μw) = ⋋f(v) + μf(w) avec pourt out v w des elem de V et mu et lambda des scalaires de K  '
    
monomorphisme, epimorphisme, isomorphisme = 'injective surjective bijective'.split(" ")

#Linéaire signifie combinaison linéaire, soit que l'on préserve une certaine proportion de grandeur.
#Edit: Soit on préserve la multiplication scalaire d'ume même base et on garde l'addition vectorielle dans l'espace vectoriel en question
#VOIR AUSSI NOTES BLOC SAMSUNG NOTES