combinaison_lineaire = '/sum_{i=1}^r 𝞴_{i} \vec{v}_{i}' #en LaTeX
exemple_combili = 'cos 2x = cos2 x − sin2 x'
print(('le vecteur est une combili de vecteurs si ce vecteur represente {} ').format(combinaison_lineaire))

partie_generatrice = lambda pg : 'Un sous-ensemble A ⊆ V est une partie génératrice de V si tout \
vecteur de V une est combili de vecteurs de A. Autrement dit, si Vect(A) = V'
exemple_partie_generatrice = 'Dans l’espace réel R[X],  la somme pour k=0 jusqu\'à i des X^k | i ∈ N'

partie_libre = lambda pl : 'Un sous-ensemble A ⊆ V est une partie libre de V si aucun vecteur\
de A n’est combili d’autres vecteurs de A. On dit alors que les vecteurs de A sont\
linéairement indépendants. Sinon, on dit qu’ils sont linéairement dépendants'
autre_condition_partie_libre =  'libre ssi λ1⃗v1 + . . . + λm⃗vm = ⃗0 ⇒ λ1 = λ2 = . . . = λm = 0'