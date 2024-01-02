from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, created_directories
from cnnClassifier.entity.config_entity import (
    DataIngestionConfig,
    PrepareBaseModelConfig,
    PrepareCallbacksConfig,
    EvaluationConfig,
)
import os
from cnnClassifier.entity.config_entity import TrainingConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        # creating directoeries

        created_directories([self.config.artifacts_root])

        # data ingestion configuration

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        created_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )
        return data_ingestion_config

    # for traaining od the model
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        created_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES,
        )
        return prepare_base_model_config

    # for callback function


class ConfigurationCallbacksManager:
    def __init__(
        self,
        config_filepth=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
    ):
        self.config = read_yaml(config_filepth)

        self.params = read_yaml(params_filepath)

        created_directories([self.config.artifacts_root])

    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks

        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)

        # creating dir
        created_directories(
            [Path(model_ckpt_dir), Path(config.tensorboard_root_log_dir)]
        )

        prepare_callbacks_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath),
        )

        return prepare_callbacks_config


# for configuration
class ConfigurationTrainingManager:
    def __init__(
        self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        created_directories([self.config.artifacts_root])

    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)

        created_directories(
            [Path(model_ckpt_dir), Path(config.tensorboard_root_log_dir)]
        )

        prepare_callback_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath),
        )
        return prepare_callback_config

    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(
            self.config.data_ingestion.unzip_dir, "Chicken-fecal-images"
        )
        created_directories([Path(training.root_dir)])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.get("EPOCH"),
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
        )

        return training_config


# for evaluation
class ConfigurationEvaluationManager:
    def __init__(
        self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        created_directories([self.config.artifacts_root])

    def get_validation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model="artifacts/training/model.h5",
            training_data="artifacts/data_ingestion/Chicken-fecal-images",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE,
        )

        return eval_config
