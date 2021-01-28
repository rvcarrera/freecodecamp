import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for times in range(v):
                self.contents.append(k)
    def draw(self, n):
        remove = []
        if n > len(self.contents):
            return self.contents
        for times in range(n):
            remove.append(self.contents.pop(random.randint(0, (len(self.contents)-1))))
        return remove

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls_drawn = new_hat.draw(num_balls_drawn)
        new_dict = dict()
        for k, v in expected_balls.items():
            count = balls_drawn.count(k)
            if count >= v:
                new_dict[k] = v
        if new_dict == expected_balls:
            m += 1
    return m/num_experiments

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)

print(probability)