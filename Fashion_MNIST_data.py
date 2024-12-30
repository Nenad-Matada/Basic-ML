{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMJiHbgsgj5LbhuCEIgKpUN"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "ehrKgHC6gxIo",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d86b4732-536d-49ab-97e0-5dc71a4d9209"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 4ms/step - accuracy: 0.7882 - loss: 0.6196\n",
            "Epoch 2/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m10s\u001b[0m 4ms/step - accuracy: 0.8631 - loss: 0.3826\n",
            "Epoch 3/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m6s\u001b[0m 3ms/step - accuracy: 0.8758 - loss: 0.3404\n",
            "Epoch 4/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 4ms/step - accuracy: 0.8863 - loss: 0.3109\n",
            "Epoch 5/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 3ms/step - accuracy: 0.8918 - loss: 0.2928\n",
            "Epoch 6/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 4ms/step - accuracy: 0.8993 - loss: 0.2770\n",
            "Epoch 7/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m9s\u001b[0m 3ms/step - accuracy: 0.8981 - loss: 0.2738\n",
            "Epoch 8/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 4ms/step - accuracy: 0.9040 - loss: 0.2536\n",
            "Epoch 9/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m6s\u001b[0m 3ms/step - accuracy: 0.9083 - loss: 0.2437\n",
            "Epoch 10/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 4ms/step - accuracy: 0.9130 - loss: 0.2369\n",
            "Epoch 11/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m6s\u001b[0m 3ms/step - accuracy: 0.9174 - loss: 0.2224\n",
            "Epoch 12/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m10s\u001b[0m 3ms/step - accuracy: 0.9165 - loss: 0.2261\n",
            "Epoch 13/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m10s\u001b[0m 3ms/step - accuracy: 0.9198 - loss: 0.2142\n",
            "Epoch 14/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m12s\u001b[0m 4ms/step - accuracy: 0.9216 - loss: 0.2060\n",
            "Epoch 15/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m6s\u001b[0m 3ms/step - accuracy: 0.9247 - loss: 0.2023\n",
            "Epoch 16/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m10s\u001b[0m 3ms/step - accuracy: 0.9274 - loss: 0.1969\n",
            "Epoch 17/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 4ms/step - accuracy: 0.9279 - loss: 0.1882\n",
            "Epoch 18/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m6s\u001b[0m 3ms/step - accuracy: 0.9301 - loss: 0.1859\n",
            "Epoch 19/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m11s\u001b[0m 3ms/step - accuracy: 0.9349 - loss: 0.1788\n",
            "Epoch 20/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m11s\u001b[0m 4ms/step - accuracy: 0.9357 - loss: 0.1705\n",
            "Epoch 21/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m6s\u001b[0m 3ms/step - accuracy: 0.9362 - loss: 0.1717\n",
            "Epoch 22/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m10s\u001b[0m 3ms/step - accuracy: 0.9366 - loss: 0.1650\n",
            "Epoch 23/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 4ms/step - accuracy: 0.9384 - loss: 0.1645\n",
            "Epoch 24/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 3ms/step - accuracy: 0.9415 - loss: 0.1578\n",
            "Epoch 25/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m10s\u001b[0m 3ms/step - accuracy: 0.9410 - loss: 0.1549\n",
            "Epoch 26/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 4ms/step - accuracy: 0.9421 - loss: 0.1513\n",
            "Epoch 27/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m8s\u001b[0m 3ms/step - accuracy: 0.9468 - loss: 0.1415\n",
            "Epoch 28/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m7s\u001b[0m 4ms/step - accuracy: 0.9463 - loss: 0.1413\n",
            "Epoch 29/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m11s\u001b[0m 4ms/step - accuracy: 0.9465 - loss: 0.1409\n",
            "Epoch 30/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m6s\u001b[0m 3ms/step - accuracy: 0.9474 - loss: 0.1395\n",
            "Epoch 31/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m7s\u001b[0m 4ms/step - accuracy: 0.9481 - loss: 0.1356\n",
            "Epoch 32/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m6s\u001b[0m 3ms/step - accuracy: 0.9502 - loss: 0.1318\n",
            "Epoch 33/50\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m12s\u001b[0m 4ms/step - accuracy: 0.9498 - loss: 0.1308\n",
            "Epoch 34/50\n",
            "\u001b[1m1863/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m━\u001b[0m \u001b[1m0s\u001b[0m 3ms/step - accuracy: 0.9525 - loss: 0.1265\n",
            "Reached 95% accuracy so cancelling training!\n",
            "\u001b[1m1875/1875\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m6s\u001b[0m 3ms/step - accuracy: 0.9524 - loss: 0.1266\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<keras.src.callbacks.history.History at 0x7f835a9bb4c0>"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ],
      "source": [
        "import tensorflow as tf\n",
        "\n",
        "class myCallback(tf.keras.callbacks.Callback):\n",
        "  def on_epoch_end(self, epoch, logs={}):\n",
        "    if(logs.get('accuracy')>0.95):\n",
        "      print(\"\\nReached 95% accuracy so cancelling training!\")\n",
        "      self.model.stop_training = True\n",
        "\n",
        "callbacks = myCallback()\n",
        "mnist = tf.keras.datasets.fashion_mnist\n",
        "\n",
        "(training_images, training_labels), (test_images, test_labels) = mnist.load_data()\n",
        "\n",
        "training_images = training_images/255.0\n",
        "test_images = test_images/255.0\n",
        "\n",
        "model = tf.keras.models.Sequential([\n",
        "        tf.keras.layers.Flatten(),\n",
        "        tf.keras.layers.Dense(128, activation=tf.nn.relu),\n",
        "        tf.keras.layers.Dense(10, activation=tf.nn.softmax)\n",
        "])\n",
        "\n",
        "model.compile(optimizer='adam' ,\n",
        "              loss='sparse_categorical_crossentropy' ,\n",
        "              metrics=['accuracy'])\n",
        "\n",
        "model.fit(training_images, training_labels, epochs=50,\n",
        "          callbacks=[callbacks])\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "classifications= model.predict(test_images)\n",
        "print(classifications[189])\n",
        "print(test_labels[189])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NCrPCtIIgIPf",
        "outputId": "93fed4e8-a367-4056-c171-b695b2da00f5"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[1m313/313\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 2ms/step\n",
            "[2.0073478e-09 4.4998995e-14 5.7385561e-14 1.1207051e-11 7.2903895e-14\n",
            " 4.1413855e-06 9.7386644e-14 9.9999577e-01 1.4085530e-08 5.3480875e-10]\n",
            "7\n"
          ]
        }
      ]
    }
  ]
}