from distutils.core import setup
setup(
  name = 'fake_numberphone_id',         
  packages = ['fake_numberphone_id'],   
  version = '0.5.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Generator mobile number indonesia',   # Give a short description about your library
  author = 'harigro',                   # Type in your name
  author_email = 'trierbank@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/harigro/fake-number-id',   # Provide either the link to your github or to your website
  keywords = "mobile number generator for all operators in Indonesia",   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'Faker',
          'phonenumbers',
      ],
  python_requires=">=3.8",
  platforms=["any"],
  project_urls={
        "Source Code": 'https://github.com/harigro/fake-number-id',
    },
  classifiers=[
    "Development Status :: 5 - Production/Stable",
      "Environment :: Console",
      "Intended Audience :: Developers",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3 :: Only",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Programming Language :: Python :: 3.11",
      "Programming Language :: Python :: Implementation :: CPython",
      "Programming Language :: Python :: Implementation :: PyPy",
      "Topic :: Software Development :: Libraries :: Python Modules",
      "Topic :: Software Development :: Testing",
      "Topic :: Utilities",
      "License :: OSI Approved :: MIT License",
  ],
)
