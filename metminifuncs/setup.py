# see - https://packaging.python.org/guides/hosting-your-own-index/
# run '$ pipenv run python setup.py bdist_wheel' to create a Wheel file

from setuptools import setup, find_packages

setup(version='1.0.7',
      description='Miscellaneous funcs for MetMiniWX',
      author='Richard Crouch',
      author_email='richard.crouch100@gmail.com',
      license='MIT',
      include_package_data=True,
      zip_safe=False,
      py_modules=[
            'sync_start_time',
            'jena_data',
            'append_mlearning_rec',
            'mqtt_client',
            'moving_averages',
            'moving_list'
            ],
      )
