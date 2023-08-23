import tensorflow as tf
import cv2

def ConfigureGPUs(memory_limit=None, gpu_indices=None, allow_growth=True, per_process_gpu_memory_fraction=None):
        """
            Configure the GPU Acceleration
        """
        print("Searching for GPUs")
        gpus = tf.config.experimental.list_physical_devices('GPU')

        if not gpu_indices:
            gpu_indices = list(range(len(gpus))) if gpus else []

        if gpus:
            print(f"{len(gpus)} GPUs found. Configuring...")
            try:
                for i in gpu_indices:
                    if i < len(gpus):
                        if allow_growth:
                            tf.config.experimental.set_memory_growth(gpus[i], True)
                        elif per_process_gpu_memory_fraction:
                            tf.config.experimental.set_virtual_device_configuration(
                                gpus[i], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=int(memory_limit*1024))]
                            )
                        else:
                            tf.config.experimental.set_virtual_device_configuration(
                                gpus[i], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=memory_limit)]
                            )
                        print(f"GPU {i} is configured.")
                    else:
                        print(f"GPU index {i} is out of range. Skipping configuration.")
            except RuntimeError as e:
                print("Error to configure GPU:")
                print(e)
        else:
            print("Can't find any GPU\nCheck if your computer has a video card and if so, the corresponding drivers must be installed")