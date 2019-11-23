from setuptools import setup

setup(
    name              = 'objectDetectionD3MWrapper',
    version           = '0.1.0',
    description       = 'Keras implementation of RetinaNet as a D3M primitive.',
    author            = 'Sanjeev Namjoshi',
    author_email      = 'sanjeev@yonder.co',
    packages          = ['objectDetectionD3MWrapper'],
    install_requires  = ['numpy>=1.14.0',
                         'object_detection_retinanet @ git+https://github.com/NewKnowledge/object-detection-retinanet@5d67f89ca4b0d50eafb297a3074b1d7f10ff3aa1#egg=object_detection_retinanet'],                        
    entry_points      = {
        'd3m.primitives': [
            'object_detection.retinanet_convolutional_neural_network = objectDetectionD3MWrapper:ObjectDetectionRNPrimitive'
        ],
    },
)
