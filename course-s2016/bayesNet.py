from pgmpy.models import BayesianModel
from pgmpy.factors import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianModel([
('I','L'),('I','F'),('F','G'),('L','G')
])

income_cpd = TabularCPD(variable='I',
variable_card=3,values=[[0.5, 0.3, 0.2]])

lifeExp_cpd = TabularCPD(
variable='L',variable_card=2,
values=[[0.7, 0.25, 0.1],[0.3, 0.75, 0.9]],
evidence=['I'],evidence_card=[3])

femaleSchool_cpd = TabularCPD(
variable='F',variable_card=2,
values=[[.8,.3,.2],[.2,.7,.8]],
evidence=['I'],evidence_card=[3])

govtCorr_cpd = TabularCPD(
variable='G', variable_card=2,
values=[[.05,.4,.55,.85],[.95,.6,.45,.15]],
evidence=['F','L'],evidence_card=[2,2])

model.add_cpds(income_cpd, lifeExp_cpd,
femaleSchool_cpd, govtCorr_cpd)

inference = VariableElimination(model)
prob_G = inference.query(variables='G',evidence=dict([('L',1)]))
print(prob_G['G'])
# +-----+----------+
# | G   |   phi(G) |
# |-----+----------|
# | G_0 |   0.7292 |
# | G_1 |   0.2708 |
# +-----+----------+
inference = VariableElimination(model)
prob_G = inference.query(variables='G',evidence=dict([('F',1)]))
print(prob_G['G'])
# +-----+----------+
# | G   |   phi(G) |
# |-----+----------|
# | G_0 |   0.7174 |
# | G_1 |   0.2826 |
# +-----+----------+

# [[ 0.35],[ 0.65]]
lifeM = lifeExp_cpd
lifeM.marginalize(['I'])
print("Life Marginalized")
print(lifeM.get_cpd())

# [[ 0.43333333],[ 0.56666667]]
femM = femaleSchool_cpd
femM.marginalize(['I'])
print("Female Equality Marginalized")
print(femM.get_cpd())

# [[ 0.225,  0.7  ],[ 0.775,  0.3  ]]
govtM_F = govtCorr_cpd
govtM_F.marginalize(['F'])
print("Govt-Female Marginalized")
print(govtM_F.get_cpd())

govtCorr_cpd = TabularCPD(
variable='G', variable_card=2,
values=[[.05,.4,.55,.85],[.95,.6,.45,.15]],
evidence=['F','L'],evidence_card=[2,2])

# [[ 0.3  ,  0.625],[ 0.7  ,  0.375]]
govtM_L = govtCorr_cpd
govtM_L.marginalize(['L'])
print("Govt-Life Marginalized")
print(govtM_L.get_cpd())

govtCorr_cpd = TabularCPD(
variable='G', variable_card=2,
values=[[.05,.4,.55,.85],[.95,.6,.45,.15]],
evidence=['F','L'],evidence_card=[2,2])

# [[ 0.4625],[ 0.5375]]
govtM_LF = govtCorr_cpd
govtM_LF.marginalize(['L','F'])
print("Govt-Life-Female Marginalized")
print(govtM_LF.get_cpd())
