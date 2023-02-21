# This program uses the random module to generate a different joke everytime its run
import random

jokes = [
    'why are fire trucks red',
    'why did the chicken cross the road ? to get to the other side',
    'who let the dogs out? woff',
    'why was the math book sad = because it had too many problems',
         ]

ran_joke = random.choice(jokes)
print(ran_joke)
