import matplotlib.pyplot as plt
import numpy as np

object = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos= np.arange(len(object))
performance=[10,8,6,4,2,1]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, object)
plt.ylabel('usage')
plt.title('Programming Language usage')
plt.show()