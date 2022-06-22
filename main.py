# Charles Young
# 6/7/2020
# This file will execute the program, getting data and
# extracting information from it
import webScrape
import probabilities
import numpy as np
import tensorflow as tf
log = webScrape.WTFLogin()
log.login()
log.get_data(5000)
# TIME_STEPS = 20
#
# data = probabilities.Data()
# data.generate_data("input.txt")
# X, Y = data.split_sequence(TIME_STEPS)
# train_x, train_y, test_x, test_y = data.split_data(X, Y, 100000)
# train_x = train_x.reshape((train_x.shape[0], train_x.shape[1], 1))
# test_x = test_x.reshape((test_x.shape[0], test_x.shape[1], 1))
# model = data.create_model(TIME_STEPS)
# callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)
# model.fit(train_x, train_y, epochs=30, verbose=1, callbacks=[callback])
# model.save("LSTM_Model")
#
# model.evaluate(test_x, test_y)

# x_input = np.array([5.26, 9.01, 1.76, 3.19, 2.08, 7.68, 1.24, 1.6,  2.06, 5.3])
# # 1
# x_input = x_input.reshape((1, 10, 1))
# yhat = model.predict(x_input, verbose=1)
# print(yhat)

# data.plot_data()