from setuptools import setup

setup(
    name              = 'objectDetectionD3MWrapper',
    version           = '0.1.0',
    description       = 'Keras implementation of RetinaNet as a D3M primitive.',
    author            = 'Sanjeev Namjoshi',
    author_email      = 'sanjeev@yonder.co',
    packages          = ['objectDetectionD3MWrapper'],
    install_requires  = ['numpy>=1.15.4,<=1.17.3',
                         'object_detection_retinanet @ git+https://github.com/NewKnowledge/object-detection-retinanet@beca7ff86faa2295408e46fe221a3c7437cfdc81#egg=object_detection_retinanet'],                        
    entry_points      = {
        'd3m.primitives': [
            'object_detection.retinanet = objectDetectionD3MWrapper:ObjectDetectionRNPrimitive'
        ],
    },
)
