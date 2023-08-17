class Assembly:
    def __init__(self, prefab):
        self.prefab = prefab

    def Set(self, attr, value):
        if attr in self.prefab:
            self.prefab[attr] = value
        return self

    def Get(self, attr):
        if attr in self.prefab:
            return self.prefab[attr]
        return None
    
    def Mount(self):
        return self.prefab

class POSE:
    lite = Assembly({
        "static_image_mode": False,
        "model_complexity": 0,
        "smooth_landmarks": False,
        "enable_segmentation": False,
        "smooth_segmentation": False,
        "min_detection_confidence": 0.3,
        "min_tracking_confidence": 0.3
    })

    normal = Assembly({
        "static_image_mode": False,
        "model_complexity": 1,
        "smooth_landmarks": True,
        "enable_segmentation": False,
        "smooth_segmentation": True,
        "min_detection_confidence": 0.5,
        "min_tracking_confidence": 0.5
    })

    heavy = Assembly({
        "static_image_mode": False,
        "model_complexity": 1,
        "smooth_landmarks": True,
        "enable_segmentation": False,
        "smooth_segmentation": True,
        "min_detection_confidence": 0.8,
        "min_tracking_confidence": 0.8
    })

class HANDS:
    lite = Assembly({
        "static_image_mode": False,
        "max_num_hands": 2,
        "model_complexity": 0,
        "min_detection_confidence": 0.3,
        "min_tracking_confidence": 0.3
    })

    normal = Assembly({
        "static_image_mode": False,
        "max_num_hands": 2,
        "model_complexity": 1,
        "min_detection_confidence": 0.5,
        "min_tracking_confidence": 0.5
    })

    heavy = Assembly({
        "static_image_mode": False,
        "max_num_hands": 2,
        "model_complexity": 2,
        "min_detection_confidence": 0.8,
        "min_tracking_confidence": 0.8
    })

class FACE:
    normal = Assembly({
        "static_image_mode": False,
        "max_num_faces": 1,
        "refine_landmarks": False,
        "min_detection_confidence": 0.5,
        "min_tracking_confidence": 0.5
    })

    heavy = Assembly({
        "static_image_mode": False,
        "max_num_faces": 1,
        "refine_landmarks": True,
        "min_detection_confidence": 0.8,
        "min_tracking_confidence": 0.8
    })

class ALL:
    lite = Assembly({
        "static_image_mode": False,
        "model_complexity": 0,
        "smooth_landmarks": False,
        "enable_segmentation": False,
        "smooth_segmentation": False,
        "refine_face_landmarks": False,
        "min_detection_confidence": 0.3,
        "min_tracking_confidence": 0.3
    })

    
    normal = Assembly({
        "static_image_mode": False,
        "model_complexity": 1,
        "smooth_landmarks": True,
        "enable_segmentation": False,
        "smooth_segmentation": True,
        "refine_face_landmarks": False,
        "min_detection_confidence": 0.5,
        "min_tracking_confidence": 0.5
    })
  
    heavy = Assembly({
        "static_image_mode": False,
        "model_complexity": 2,
        "smooth_landmarks": True,
        "enable_segmentation": False,
        "smooth_segmentation": True,
        "refine_face_landmarks": True,
        "min_detection_confidence": 0.8,
        "min_tracking_confidence": 0.8
    })

GPU_ACELERATION = Assembly({
    "enable": False,
    "memory_limit": None,
    "allow_growth": True,
    "per_process_gpu_memory_fraction": None,
    "gpu_indices": None
})

DETECT_POSE      = "100"
DETECT_HAND      = "010"
DETECT_FACE      = "001"
DETECT_POSE_HAND = "110"
DETECT_POSE_FACE = "101"
DETECT_HAND_FACE = "011"
DETECT_ALL       = "111"