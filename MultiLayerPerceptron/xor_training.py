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

for epoch in range(5000):

    for x,y in dataset:
        net.train(x,y)
    
    print(epoch)

for x,y in dataset:

    print(
        x,
        net.predict(x)
    )
net.save("/xor.nn")
print("grabado")