# Now here Pavan has explained how to access methods from two different module if class is there

# Approach1
import aclass, bclass

abj1 = aclass.Animal()
abj1.display()

bj1 = bclass.Bird()
bj1.display()

print('**********************# Approach2******************')

# Approach2
from aclass import Animal
from bclass import Bird

fr1 = Animal()
fr1.display()

fr2 = Bird()
fr2.display()
