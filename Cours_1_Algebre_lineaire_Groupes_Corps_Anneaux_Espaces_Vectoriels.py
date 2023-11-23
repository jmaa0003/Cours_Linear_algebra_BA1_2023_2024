"""
Mabhouma Joshua
Algèbre linéaire
08/11/2011
Révision Cours 1 : Groupes, Corps et Espaces Vectoriels
"""

def isGroupe(G):
    return True if loi_de_composition_binaire == loi_interne ==\
       '* : G x G -> G, (x,y) |-> x*y' and\
       isAssociative(G)\
       and HasElementNeutre(G)\
           and isInversible(G) else False

def isgroupecommutatif_or_abelien(G):
    return True if isGroupe(G) and isCommutative(G)

preuve_unicité_element_neutre_groupe =\
'Soit e, f deux elements supposés neutre pour la\
multiplication de groupes et qui appartiennent à G,\
alors cela implique que ∀a ∈ G, a*e = a*f donc\
que f*e = e et\
e*f = f. Limitons nous a un groupe non abelien. Etant donne\
que la multiplication est non commutative ici, alors\
lorsque on remplace f par e et e par f, étant donné qu\'\
on obtient le même resultat, e=f donc ∃! e ∈ G tq ∀a ∈ G,\
e*a = a'

preuve_unicité_inverse_element_groupe =\
'dans le même ordre que preuve_unicité_element_neutre_groupe'

groupes_abeliens = set('Z,+', 'Q,+', 'R,+', 'C,+', 'Q0, .',\
                       'R0, .', 'C0, .')
not_a_group = 'les naturels positifs avec l\'add n'
#car pas d'inverse pour n > 0
is_groupe = {'les Z modulo m ∈ Z'}

C_1 =\
    'addition associative'
C_2 =\
    'K possède un element neutre pour l\'addition'
C_3 =\
    'inverse additif'
C_4 =\
    'addition commutative'
C_5 =\
    'multiplication associative'
C_6 =\
    'K possède un neutre multiplicatif soit ∃ 1 ∈ K tq a*1 = a = 1*a\
    ∀ a ∈ K'
C_7 =\
    'multiplication distributive pour l\'addition soit  ∀ a,b,c ∈ K tq\
    a*(b+c) = a*b + a*c et par commutativité de la multiplication\
    = (b+c)*a = b*a + c*a'
C_8 =\
    'multiplication commutative soit  ∀ a,b ∈ K tq a*b = b*a ∈ K'
C_9 =\
    'inverse multiplicatif soit ∀ a ∈ K ∃ a^-1 ∈ K tq a*a^-1 = 1\
    = a^-1 * a ∈ K (par commutativité de la multiplication)'

def isAnneau(A):
    return True if C_1 and C_2 and C_3 and C_4 and C_5 and C_6 and C_7\
           else False

isAnneauCommutatif = lambda AC : True if isAnneau(AC) and C_8 else False
isCorps 		   = lambda C : True if is Anneau(C) and C_9 else False

def isChamp(Ch):
    return True if isAnneauCommutif(Ch) and isCorps(Ch) else False




                



    
    