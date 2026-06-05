# Universidad CENFOTEC
# Tomás de Camino Beck

#Ejemplo sencillo de perceptrón multicapa

from ulab import numpy as np
import math
import random


class FastMLP:

    def __init__(self, layers, learning_rate=0.05):

        self.layers = layers
        self.learning_rate = learning_rate

        self.weights = []
        self.biases = []

        for i in range(len(layers) - 1):

            rows = layers[i + 1]
            cols = layers[i]

            W = np.array([
                [random.uniform(-1.0, 1.0) for _ in range(cols)]
                for _ in range(rows)
            ])

            b = np.array([
                random.uniform(-1.0, 1.0)
                for _ in range(rows)
            ])

            self.weights.append(W)
            self.biases.append(b)

    # ==================================================
    # ACTIVACION
    # ==================================================

    def sigmoid(self, x):

        result = np.zeros(len(x))

        for i in range(len(x)):

            v = x[i]

            if v > 20:
                result[i] = 1.0

            elif v < -20:
                result[i] = 0.0

            else:
                result[i] = 1.0 / (1.0 + math.exp(-v))

        return result

    def dsigmoid(self, y):

        result = np.zeros(len(y))

        for i in range(len(y)):
            result[i] = y[i] * (1.0 - y[i])

        return result

    # ==================================================
    # FORWARD
    # ==================================================

    def forward(self, x):

        activations = [x]

        a = x

        for layer in range(len(self.weights)):

            W = self.weights[layer]
            b = self.biases[layer]

            z = np.dot(W, a) + b

            a = self.sigmoid(z)

            activations.append(a)

        return activations

    # ==================================================
    # PREDICCION
    # ==================================================

    def predict(self, inputs):

        x = np.array(inputs)

        activations = self.forward(x)

        return activations[-1]

    # ==================================================
    # ENTRENAMIENTO
    # ==================================================

    def train(self, inputs, targets):

        x = np.array(inputs)
        y = np.array(targets)

        activations = self.forward(x)

        deltas = [None] * len(self.weights)

        # ----------------------------------------------
        # DELTA SALIDA
        # ----------------------------------------------

        output = activations[-1]

        error = y - output

        delta_out = np.zeros(len(output))

        for i in range(len(output)):

            delta_out[i] = (
                error[i]
                * output[i]
                * (1.0 - output[i])
            )

        deltas[-1] = delta_out

        # ----------------------------------------------
        # DELTAS OCULTAS
        # ----------------------------------------------

        for layer in range(len(self.weights) - 2, -1, -1):

            W_next = self.weights[layer + 1]
            delta_next = deltas[layer + 1]

            a = activations[layer + 1]

            propagated = np.zeros(len(a))

            for i in range(len(a)):

                s = 0.0

                for j in range(len(delta_next)):
                    s += W_next[j][i] * delta_next[j]

                propagated[i] = s

            delta = np.zeros(len(a))

            for i in range(len(a)):
                delta[i] = (
                    propagated[i]
                    * a[i]
                    * (1.0 - a[i])
                )

            deltas[layer] = delta

        # ----------------------------------------------
        # ACTUALIZAR PESOS
        # ----------------------------------------------

        for layer in range(len(self.weights)):

            a_prev = activations[layer]

            delta = deltas[layer]

            for neuron in range(len(delta)):

                for k in range(len(a_prev)):

                    self.weights[layer][neuron][k] += (
                        self.learning_rate
                        * delta[neuron]
                        * a_prev[k]
                    )

                self.biases[layer][neuron] += (
                    self.learning_rate
                    * delta[neuron]
                )

    # ==================================================
    # ARGMAX
    # ==================================================

    def argmax(self, vector):

        idx = 0
        best = vector[0]

        for i in range(1, len(vector)):

            if vector[i] > best:
                best = vector[i]
                idx = i

        return idx

    # ==================================================
    # GUARDAR
    # ==================================================

    def save(self, filename):

        with open(filename, "w") as f:

            f.write(str(len(self.weights)))
            f.write("\n")

            for W in self.weights:

                rows = []

                for r in range(len(W)):

                    row = []

                    for c in range(len(W[r])):
                        row.append(float(W[r][c]))

                    rows.append(row)

                f.write(str(rows))
                f.write("\n")

            f.write("BIAS\n")

            for b in self.biases:

                row = []

                for i in range(len(b)):
                    row.append(float(b[i]))

                f.write(str(row))
                f.write("\n")

    # ==================================================
    # CARGAR
    # ==================================================

    def load(self, filename):

        with open(filename, "r") as f:
            lines = f.readlines()

        idx = lines.index("BIAS\n")

        self.weights = []

        for line in lines[1:idx]:

            self.weights.append(
                np.array(eval(line.strip()))
            )

        self.biases = []

        for line in lines[idx + 1:]:

            self.biases.append(
                np.array(eval(line.strip()))
            )