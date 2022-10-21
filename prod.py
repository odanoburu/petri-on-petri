from snakes.nets import *
import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *

prod = PetriNet('Prod')
prod.add_place(Place('p1', [1]))
prod.add_place(Place('p2'))
prod.add_place(Place('p3'))
prod.add_place(Place('p4', ['empty']))
prod.add_transition(Transition('t1'))
prod.add_input('p1', 't1', Value(1))
prod.add_output('p1', 't1', Value(1))
prod.add_output('p3', 't1', Value(1))
prod.add_transition(Transition('t2'))
prod.add_input('p1', 't2', Value(1))
prod.add_output('p2', 't2', Value(1))
prod.add_transition(Transition('t3'))
prod.add_input('p2', 't3', Value(1))
prod.add_output('p1', 't3', Value(1))
prod.add_transition(Transition('t4'))
prod.add_input('p2', 't4', Value(1))
prod.add_input('p3', 't4', MultiArc([Value(1), Value(1), Value(1)]))
prod.add_input('p4', 't4', Value('empty')) # inhibitor
prod.add_output('p2', 't4', Value(1))
prod.add_output('p4', 't4', MultiArc([Value(1)]))

prod.draw("prod-net-before.png")

prod.transition('t1').fire(Substitution())
prod.transition('t1').fire(Substitution())
prod.transition('t1').fire(Substitution())
# print("New net state:", prod.get_marking())
prod.transition('t2').fire(Substitution())
print("Transition", prod.transition('t4').modes())
prod.transition('t4').fire(Substitution())
prod.draw("prod-net-after.png")
