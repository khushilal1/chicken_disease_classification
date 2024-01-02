import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model  # Add this import
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig
from pathlib import Path


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
        self.model = None
        self.full_model = None
        self.base_model = None

    def get_base_model(self):
        if self.config is not None:
            self.model = tf.keras.applications.vgg16.VGG16(
                input_shape=self.config.params_image_size,
                weights=self.config.params_weights,
                include_top=self.config.params_include_top,
            )

        # saving the model

        self.save_model(path=self.config.base_model_path, model=self.model)

    @staticmethod
    def prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        # checkig the layer

        if freeze_all:
            for layer in model.layers:
                model.trainable = False

        elif (freeze_till is not None) and (freeze_till) > 0:
            for layer in model.layers:
                model.trainable = True

        # flatten layer

        flatten_in = tf.keras.layers.Flatten()(model.output)
        # last layer
        predicton = tf.keras.layers.Dense(units=classes, activation="softmax")(
            flatten_in
        )

        full_model = Model(model.input, outputs=predicton)
        # compiling the model
        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"],
        )

        full_model.summary()
        return full_model

    def update_base_model(self):
        if self.model is not None:
            print("Model in update_base_model:", self.model)

            self.full_model = self.prepare_full_model(
                model=self.model,
                classes=self.config.params_classes,
                freeze_all=True,
                freeze_till=None,
                learning_rate=self.config.params_learning_rate,
            )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
