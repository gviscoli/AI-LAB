import tensorflow as tf
import sys
import os


def check_gpu_resources() -> None:
    print(f"GPUs : {tf.config.list_physical_devices('GPU')}")


def check_tensorflow_resources() -> None:
    print(f"TF Version : {tf.__version__}")


def check_python_version()->None:
    print(f"Python Version : {sys.version}")

if __name__ == "__main__":
    
    os.system('cls')

    check_python_version()
    check_tensorflow_resources()
    check_gpu_resources()
    
    print(hasattr(tf, 'keras'))

