import asyncio

async def countdown():
    numbers = []
    for i in range(101):
        numbers.append(i)
        await asyncio.sleep(0.01)
    return numbers

# To run and test the function:
asyncio.run(countdown())  # Uncomment this line to run the function if needed

# range(101) gives numbers from 0 to 100 inclusive.

# await asyncio.sleep(0.01) makes the function pause asynchronously for 0.01 seconds.

# The numbers list collects each number in the countdown.

# asyncio.run(countdown()) is used to run the async function from a synchronous context (like a script).