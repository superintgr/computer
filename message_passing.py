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
