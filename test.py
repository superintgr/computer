"""
1. what possible kinds of error could be found?
2. how to position the nodes to capture enough data?
3. define the pipeline for potential error scene and what are they?


[plan out the basic form of interaction from end-to-end]
-1. find the available handlers for all changes to memory buffer
-0. bring top k handlers to the queue for buffer elements
+0. 
"""

#### 1- ####
"""Finding available handler while scanning for changes in memory blocks

list_of_handlers = [handler.py, runner.py, seeker.py, ..]
memory_blocks = [disk1, disk2, disk3, ...]
changes_since_scanned = [k%, n%, m%]
scanning_logs = {}

if change:
    disk = rank_regions(change)
    subclass = rank_domains(disk, change)
    locals = rank_ranges(subclass, disk, change)
    nodes = rank_neighbors(locals, subclass, disk, change)

    for node in nodes:
        antinode = node(change, memory_blocks)
        handler = list_of_handlers.index(antinode)
        session = rectify(handler)
        while True:
            q = session(antinode, node, change)
            if q:
                break
        change += q
    
[bringing top k agents]
 we have to define what kind of agency the system of agents and others will be maintaining.
 by maintain, I am referring to the core principles that would apply to every agents and all interactions.
 the interactions are between agents and everything else required for setting up the system protocols

 ## key points:
 1. agency and principled organization,
 2. system-wide flow and effect of organization,
 3. maintainence and [error corrections, this is new]

 [model of communication]
  there will be layered structures:
  . operating system tasks and retaining functional previleges,
  . basic computation substrate and memory usage,
  . scanning external inputs and preprocessing of bytes,
  . delivery mechanism and logging tools
  . parametrization and service discovery
  . broadcasting language and automatic publishing routines
  . error detection and redundancy
  

[operating system tasks and administrative previleges]
    import subprocess
    import node, antinode
    
    environments = {}
    workers = {}
    presets = {}

    regular = node.load_substrate(__file__)
    irregular = antinode.load_substrate(__file__)

    request = lambda environment, worker, preset=None: regular.prepare(environment, worker, preset)
    terminate = lambda process, callback: irregular.prepare(process, callback)


## comment ##

  all the subprocess related tasks could be handled through node/antinode protocols.

[basic computation substrate and memory usage]

    import node, antinode
    import os
    import psutils
    
    storage = lambda size, _node, _antinode: node.allocate(size, source=_node, target=_antinode)

[scanning external inputs and processing bytes]
    import node, antinode

    def sample(path, scanner, feedforward):
        substrate = node.unsqueeze(path)
        scope = antinode.squeeze(substrate, scanner)
        return feedforward(scope)

    def communicate(address, callback, shape, language):
        buffer = node.stream(address, shape)
        batch, decoder = antinode.encode(buffer, language)
        receipt = callback(batch)
        status = buffer(decoder(receipt)):
        buffer.close()
        return status


[solvers and adapters]

solvers = load_solvers()
spaces = load_spaces()
columns = zip(spaces, solvers)
adapters = []

for column in columns:
    x, z = column
    y = z(x)
    for solver in solvers:
        y += solver(y)
    adapters.append(zip(y, x))

A(t) := c[0] * I(t) + c[1] * X(t) + c[2] * Y(t) + c[3] * Z(t)

         y yyg  


        
"""Here is an idea:

[this is what i have at non-programming setting]
    . pattern generator and step sequencer
    . piano roll and graph features
    . playlist for placing tracks
    . automation clips
    . mixing console with N channels
    . channel functions and i/o
    . connection matrix and routing bus
    . slicing/quantizing/modifying etc.

[this is what i want]
    . describe computation in the playlist
    . compile audio runtime with N parallel processes
    . map dynamical parameters from track space to symbolic programming api
    . many more than haven't been discovered
"""











find fixed points of a pure tone of constant frequency
map the fixed points to a set of variables



low -> mid
mid -> center
center -> high
high -> low

For every input, transform the input through chain of processors
Each processor has a spectrum of possible outputs for a given input point
Combination of all spectral components produce the output spectrum
From the output spectrum, the linear transform of the model state produces the final output point
After the high frequency spectrum is calculated, the transform on the composite state encodes the chain of processing into the lower part of the spectrum.

Equivalently, the kinetic energy produced from the 
observed input state depends of the potential energy whose spectrum of possible transforms is the sum of all the frequency zones kinetic energies.
Once the high -> low layer produces the output, the final transform will be output / input i.e. the ratio between the kinetic and potential energy.




[Lingering Problem]

-1. what type of input
-0. what type of output
+0. what is the input state
+1. what is the target state
1-. type of the target/input state
0-. type of the input/output state
0+. function of the output/input state
1+. function of the input/output state
-1. input is a function of real numbers
-0. output is a function of real numbers
+0. input state is a function of integers
+1. output state is a function of integers

