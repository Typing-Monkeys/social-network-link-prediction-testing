from setuptools import setup, find_packages


setup(
    name='social_network_link_prediction',
    version='0.1.1.1',
    license='MIT',
    author="Cristian Cosci, Fabrizio Fagiolo, Nicolò Vescera, Nicolò Posta, Tommaso Romani",
    author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Typing-Monkeys/social-network-link-prediction',
    keywords='example project',
    install_requires=[
          'numpy',
      ],

)