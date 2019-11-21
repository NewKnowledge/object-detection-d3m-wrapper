from setuptools import setup

setup(
    name              = 'object-detection-d3m-wrapper',
    version           = '0.1.0',
    description       = 'Keras implementation of RetinaNet as a D3M primitive.',
    author            = 'Sanjeev Namjoshi',
    author_email      = 'sanjeev@yonder.co',
    packages          = ['object-detection-d3m-wrapper'],
    install_requires  = ["object-detection @ git+https://github.com/NewKnowledge/object-detection-retinanet@dcfdb2442564893a92a0ba0eb0aac9958a28f59d#egg=object-detection-retinanet"]
                        ],
    entry_points      = {
        'd3m.primitives': [
            'object_detection.retinanet_convolutional_neural_network = object-detection-d3m-wrapper:ObjectDetectionRNPrimitive'
        ],
    },
)