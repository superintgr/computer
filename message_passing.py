network = {}

def new_graph(label, capacity, volume):
    """
    Creates a labeled graph with maximum capacity and differentiable volume amount.

    Args:
    - label : string containing ascii characters.
    - capacity : maximum sampling rate.
    - volume : block size per step.

    Returns: A channel for driving the node and the object structure for integrating information.
    """
    channel = create_device(capacity, volume)
    record = {
        "network" : label,
        "object"  : channel,
        "capacity" : capacity,
        "volume" : volume
    }
    return record, channel

def new_line(shape, balanced=False):
    """
    Create a parametrized line object.

    Args:
    - shape : dimensionality of the flow process.
    - balanced : if phase inverted transport required.

    Returns: Line object parametrized randomly.
    """
    line = create_linear(shape, balanced)
    return line
    
def setup_transmission(source, substrate, sink):
    """
    Creates transmission graph dual to the substrate.

    Args:
    - source : identity node within the subsystem.
    - substrate : graph structure composed of channels of information flow.
    - sink : conjugate node within the subsystem.

    Returns: New channel with lines setup between possible pathways.
    """
    pass
    








"""
**Message Passing Module**

. messages are sent by one object to another object
. sender object puts message data to a common object
. common object puts message data to receiver object
. receiver-sender connection is via the common object

- start with the common object
- set the attributes contained in the properties defined for the common mode messaging
- create a pair of sender-receiver objects
- if message from any object to common object is possible, then another message for collecting an information variable as message from the associated other object

[object1 and object2 are both sender and receiver]
[object3 can receive message from both objects]

"""



modules = [information, computation, measurement, construction]

class Construction:
    output : state dict
    input  : state repr
    task   : input -> output

"""
***Construction tasks***

Tasks are defiened as:
    required state of the substrate  : input attribute
    output property of the substrate : target attribute

    where a constructor would transform the input attributes (if found in that state)
    to the desired final state while remaining capable for the task again.

If the input attributes are not readily available, the construction of that substrate
. with the desired properties or turning the existing one to converge onto the given
. properties is a possible task.

Chaining tasks look like:
    [serial composition] is the task performing on one substrate, depending on the
    . output of another one while doing one after another in succession.

    [parallel composition] is the task of performing in two disjoint substrates
    . in parallel and combining their individual transformations together using
    . additive operation inside another substrate.

Transformation that remains valid:
    [transposition] *** elaborate on that more!
"""


class Information:
    generic  : random samples
    basis    : selected samples
    task     : basis, generic   -> basis, basis

class Computation:
    operator : permutation
    iterator : variable
    requires : (at least) two state
    computes : unitary state
    task     : union of all variable pairs in substrate where (element -> permutation of element) for all variable in unit pair

"""
**Computation**

Given some substrate such as memory elements from a volume contained in storage disk, the computation is the permutation operation
. performed on each memory elements of the substrate such their unity is possible whenever one of the ways of variable elements in
. disk volume could change into having a distinct other ways, with no less than two distinguishable attributes of the elements in
. substrate being present, one of them commutes with the other while the computation (being reversible) asserts that their dynamical
. variables map back to one of the other elements in that same set.

The union operation is there to ensure that the computation variables that participated in the transformation keeps in existence
. for subsequent transformations.


**Information**

It is a property of a substrate where it is able to copy certain attributes from interacting with other objects while retaining the
. counterfactual information parameters become useful.

For some substrate that is reversible information processing media could use generic naturally occuring resources to construct new
. media for computation or any other information processing task.
"""



def construct_memory(required_volume, volatile_block, storage_volume):
    information = []
    computation = []
    measurement = []
    
    for block in required_volume:
        for space in volatile_block:
            for bin in storage_volume:
                x, y, z = (block, space), (space, bin), (bin, block)
                information.append(x)
                computation.append(y)
                measurement.append(z)
            orders = permutations(zip(block, space))
            yield orders
        tasks = permutations(block, zip(information, computation, measurement))
        yield tasks
    return information, computation, measurement


# Naturally ocurring substrates are necessary for finding the gap constructor.
# Suppose there is a task on other substrates and the task is setup on this
# new substrate as coming from constructions of the output states towards
# the output state of this substrate where it first comes the input state of
# the current substrate. This kind of chaining and composing rules would work
# as expected but I really don't have (this) substrate nor do I have an
# expected output state on which it would have consisted their mappingz


"""
[cartesian product] of two substrates is pair-wise distinguishable.
If the combination of two substrates are distinguishable then the cartesian product of the two is also distinguishable.
If the two substrates have attributes that are information variables, their cartesian product is also an information variable.
If y can be distinguished from x, then x is also distinguishable.

[generic resource] from naturally occuring sources could be used to construct unlimited number of information processing substrates.
If g is a generic resource and the task G => {g -> C[G]} with side effect being possible where C[G] is the constructor for G,
. then G is implicated in the effect of G having been possible <=> existence of one (h)(G * {g -> h}) being possible also.
. NOTE: * refers to the cartesian product

[sampling resource]
One idea is to record the pressure waves from empty spaces and other acoustic environments to collect acoustic energy to tranduce into some regular networks of constructors.
. Every regular networks of tasks are possible tasks.

What form should the standard mining algorithm be programmed in considerations with?
. whatever form the data may take, information substrate would enable interoperability property in the chain anyway.

[composite midside] If two channels Z and T, each have some information variable that could be combined together, then the combination of the two variables would construct a new substrate (Y) whose attributes X would contain the cartesian products of Z and T.  
"""

                                                                                                                      
class Generic:
    source : empty space
    criterion : possibility/impossibilty
    








class Measurement:
    observable : computation
    attribute  : variable
    substrate  : wave
    task       : disjoint attribute from computation -> physical variable with sharp observable or locally inaccessible for pertubation


"""
**Measurement**

Computing the union of all {x -> psi[x]} for some observable X with x in it, the measurement is going to be a non-perturbating one. In short, all we care about is whether the transformation is possible or not which implies the possibility of being able to measure with arbitrary accuracy or find no regularity for learning such attribute at all.
. For observables that are possibly be a physical variable that could have sharp observables or perhaps not for some perticular transformation, but nevertheless that alone should not prohibit any measurement of that variable with arbitrary accuracy since we can always learn about the outcome through requiring the variable to be factoring into some other computation task and whose net construction from that additive state would make the measurement exact.

All we are going to consider in terms of dynmical evolution of those subtrates consists of permutations and cloning operations that are made to preserve logical reversibility during all processing of information across the entire stack.
"""
