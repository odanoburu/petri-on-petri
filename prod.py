from snakes.nets import *
import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *

prod = PetriNet('Prod')

# places
prod.add_place(Place('p1', [1]))
prod.add_place(Place('p2'))
prod.add_place(Place('p3'))
prod.add_place(Place('p4'))
prod.add_place(Place('sink'))

# t1
prod.add_transition(Transition('t1'))
prod.add_input('p1', 't1', Value(1))
prod.add_output('p1', 't1', Value(1))
prod.add_output('p3', 't1', Value(1))

# t2
prod.add_transition(Transition('t2'))
prod.add_input('p1', 't2', Value(1))
prod.add_output('p2', 't2', Value(1))

# t3
prod.add_transition(Transition('t3'))
prod.add_input('p2', 't3', Value(1))
# this throws an error:
#prod.add_input('p4', 't3', Inhibitor(Variable('y')))
prod.add_output('p1', 't3', Value(1))

# t4
prod.add_transition(Transition('t4'))
prod.add_input('p2', 't4', Value(1))
prod.add_input('p3', 't4', MultiArc([Value(1), Value(1), Value(1)]))
prod.add_input('p4', 't4', Inhibitor(Variable('x')))
prod.add_output('p2', 't4', Value(1))
prod.add_output('p4', 't4', Value(1))

# tsink
prod.add_transition(Transition('tsink'))
prod.add_input('p4', 'tsink', Value(1))
prod.add_output('sink', 'tsink', Value(1))

def step():
    prod.transition('t1').fire(Substitution())
    prod.transition('t1').fire(Substitution())
    prod.transition('t1').fire(Substitution())
    print("After thrice t1:", prod.get_marking())

    prod.transition('t2').fire(Substitution())
    print("After t2:", prod.get_marking())

    # show possible substitutions enabling the transition
    print("Transition", prod.transition('t4').modes())
    # choose the substitution we will use to enable the transition
    ## NOTE: in this case there's only one option of substitution, but
    ## we may want to choose when there are several
    prod.transition('t4').fire(Substitution(x=0))
    print("After t4:", prod.get_marking())

    prod.transition('t3').fire(Substitution())
    print("After t3:", prod.get_marking())

    prod.transition('tsink').fire(Substitution())
    print("After tsink:", prod.get_marking())

prod.draw("prod-net-before.png")
step()
step()
