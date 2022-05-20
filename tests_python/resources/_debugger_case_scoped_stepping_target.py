# Note that await in the top-level isn't valid in general, but we compile
# it specifically accepting it, so, that's ok.
import asyncio

await asyncio.sleep(.01)
a = 1  # Break here
print(a)
await asyncio.sleep(.01)
b = 2
print(b)
await asyncio.sleep(.01)
