import chapter5_Optimazation.optimization
from chapter5_Optimazation import optimization, dorm,socialnetwork

# domain = [(0,9)]*(len(optimization.people)*2)
sol = optimization.geneticoptimize(socialnetwork.domain, socialnetwork.crosscount)
socialnetwork.drawnetwork(sol)
