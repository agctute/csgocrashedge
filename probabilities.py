# Charles Young
# 6/6/2020
# This file parses through input.txt, and analyzes (or tries to) the data scraped
from decimal import *
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


class Data:
    def __init__(self):
        # self.ls = []  # contains list of numbers to test
        self.lines = []  # contains list of data points
        self.num_elements = 0

    # plots data using instance variables
    def plot_data(self, option="t"):
        num_list = []
        for i in range(self.num_elements):
            num_list.append(self.num_elements - i)
        fig, ax = plt.subplots()
        ax.plot(num_list, self.lines)
        plt.show()

    # defines the different instance variables
    def generate_data(self, input_file, data_set=0):
        getcontext().prec = 4
        # creates range of outputs that I want
        # for i in range(start, stop):
        #     num = Decimal(i)*Decimal(stride) + Decimal(1)
        #     self.ls.append(num)

        # extracts data from input.txt into a list, removes first elem
        f = open(str(input_file), "r")
        self.lines = f.readlines()
        del self.lines[0]
        f.close()

        # converts data into list of floats rather than strings
        float_lines = []
        print(len(self.lines))
        for line in self.lines:
            if line == self.lines[len(self.lines) - 1]:
                continue
            float_lines.append(float(line.split(" ")[2].split("\n")[0]))
        self.lines = float_lines

        # chooses number of data points to use
        if data_set == 0:
            self.num_elements = len(self.lines)
        else:
            self.num_elements = data_set

    # returns two numpy arrays, X contains input, y whether or not the next value > 2
    def split_sequence(self, n_steps):
        sequence = self.lines
        X, y = [], []
        for i in range(len(sequence)):
            end_ix = i + n_steps
            if end_ix >= len(sequence):
                break

            seq_x = sequence[i:end_ix]
            if sequence[end_ix] > 2:
                seq_y = 1
            else:
                seq_y = 0

            X.append(seq_x)
            y.append(seq_y)
        return np.array(X), np.array(y)

    def split_data(self, x, y, split_point):
        test_x = x[:split_point]
        train_x = x[split_point:]
        test_y = y[:split_point]
        train_y = y[split_point:]
        return train_x, train_y, test_x, test_y

    def create_model(self, n_steps):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.LSTM(64, activation='relu', return_sequences=True, input_shape=(n_steps, 1)))
        # model.add(tf.keras.layers.LSTM(32, activation='relu', return_sequences=True, input_shape=(n_steps, 1)))
        model.add(tf.keras.layers.LSTM(32, activation='relu', input_shape=(n_steps, 1)))
        model.add(tf.keras.layers.Dense(1))
        model.compile(optimizer=tf.keras.optimizers.Adam(0.0008), loss=tf.keras.losses.BinaryCrossentropy(),
                      metrics=[tf.keras.metrics.Precision(thresholds=0.5, name="P"),
                                tf.keras.metrics.BinaryAccuracy(name='BP', threshold=0.5)
                               ])
        return model

    # opens output file and writes calculations
    def output_probabilities(self, output_file):
        f = open(str(output_file), "a")
        for j in self.ls:
            count = 0
            for line in range(self.num_elements):
                if self.lines[line] >= j:
                    count += 1
            out = count * j / self.num_elements
            f.write(str(j) + ": " + str(out) + "\n")




