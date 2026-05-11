import matplotlib.pyplot as plt
import numpy as np

object = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos= np.arange(len(object))
performance=[10,8,6,4,2,1]
plt.barh(y_pos, performance, align='center', alpha=1, color='green')
plt.yticks(y_pos, object)
plt.xlabel('usage')
plt.title('Programming Language usage')
plt.show()