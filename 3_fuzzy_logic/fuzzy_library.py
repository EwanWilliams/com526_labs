import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

time = ctrl.Antecedent(np.arange(0, 31, 1), 'time')
complexity = ctrl.Antecedent(np.arange(0, 11, 1), 'complexity')
study_hours = ctrl.Consequent(np.arange(0, 51, 1), 'study_hours')

time['short'] = fuzz.zmf(time.universe, 7, 14)
time['medium'] = fuzz.trapmf(time.universe, [10, 13, 18, 23])
time['long'] = fuzz.smf(time.universe, 20, 26)

complexity['easy'] = fuzz.zmf(complexity.universe, 0, 4)
complexity['medium'] = fuzz.trapmf(complexity.universe, [3, 5, 7, 8])
complexity['hard'] = fuzz.smf(complexity.universe, 7, 9)

study_hours['low'] = fuzz.zmf(study_hours.universe, 4, 15)
study_hours['medium'] = fuzz.trapmf(study_hours.universe, [10, 18, 27, 34])
study_hours['high'] = fuzz.smf(study_hours.universe, 30, 38)

rule1 = ctrl.Rule(time['short'] | complexity['hard'], study_hours['high'])
rule2 = ctrl.Rule(complexity['medium'], study_hours['medium'])
rule3 = ctrl.Rule(time['long'] & complexity['easy'], study_hours['low'])

study_hours_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
study_sim = ctrl.ControlSystemSimulation(study_hours_ctrl)

study_sim.input['time'] = 10
study_sim.input['complexity'] = 6

study_sim.compute()

print(f"Study hours required: {study_sim.output['study_hours']}")
