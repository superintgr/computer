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
    


"""


class Test:
    ..


func = some_parametric_function(prep_batch)
out, in, err = func(next(cases))
corr, out = gunc(err, in)

rational = []

for e in cases:
    rational.appendfout / in * err / out * corr / in * out / err)
