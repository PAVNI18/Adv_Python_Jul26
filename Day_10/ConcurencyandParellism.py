# Bad use case
# 1. Heavy mathematical computation
# 2. CPU intensive data processing
    

    # Concurrency vs Parellelism
    # Multiple tasks make progress over time
    # Tasks are interleaved
    # Single CPU core is shared
    # Looks like they're running simultaneously

    # Parellelism: Mulitiple tasks execure simultaneously
    # Multiple CPU cores
    # Not possible in Python with threads (due to GIL)