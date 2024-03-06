class Transformer(object):
    """
    Transformer circuit model.

    primary : input gate
    secondary : output gate
    source : inductor node
    target : resistor node
    transfer : ratio between impedences
    """
   def __init__(self):
       pass


class Object:
    """
    A possible objective existence.

    If true, the object would be consisting of the following attributes:
    - set of possible positions
    - set of possible momentums
    - set of possible images
    - set of possible corrections
    - set of possible criterions

    With the state description containing the information:
    - where could the images of the trajectory in the set of all images that
        constructs a picture of the universe where the object is viable by
        the properties which enables transformations of variable physical
        quantities must specify the identity of the function?
    - if any non-viable image may be imposed on the motion, what could bring
        viability of the objective state such that the motion satisfy both
        the initial and terminal condition until next change into other states?
    - whenever any other events deter the computation from being realized,
        what protection does the policy of constructive interference support
        must cover in order to bring current all the operations?

    The properties would include:
    1. error detection
    2. headroom optimization
    3. status indicator
    """
    
    def __init__(self, positions, momentums):
        self.positions = positions
        self.momentums = momentums
        self.images = {positions : not(positions), not(positions) : positions}
        # The images should contain logs of the trajectory addresses without directly asserting sharp positions
        self.corrections = {}
        # The corrective state before propagating onto the next antinode should be added via methods mapping possible images to itself and transformed state back to image
        self.criterions = {}
        # The criteriona are only applied whenever corrections are not necessary and should also provide the resuming of state from the transformations caused to lossless image compatible with the path.
        self.errors = {}
        # Contains the data whenever any state lost information onto the next image.
        self.status = True
        self.terminal = not(self)
        # Terminating node should be different for every realizable pictures.

    def set_terminal(self, other):
        self.terminal = other
