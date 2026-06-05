from mlp import FastMLP

net = FastMLP(
    [2,4,1],
    learning_rate=0.3
)

dataset = [

    ([0,0],[0]),
    ([0,1],[1]),
    ([1,0],[1]),
    ([1,1],[0])

]

net.load("/xor.nn")

for x,y in dataset:

    print(
        x,
        net.predict(x)
    )