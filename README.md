# PythonAwesomeApp
A source-code template for Python3 applications.

## Road-map
- [x] Standard python source-code structure.
- [x] Unit testing (pytest) and test reports.
- [x] Mocking
- [x] Virtual environments & dependency mgmt.
- [x] Profiling (CPU, memory & I/O usage)
- [ ] Notes: Automate linting and enforcing code standards.
- [ ] Documentation: changelog, release notes and git-tagging.
- [ ] Application packaging & release.
- [ ] Notes: Async operation.
- [ ] Notes: Multi-threading.
- [ ] Notes: Multi-processing.
- [ ] Notes: PyPy.
- [ ] Notes: PyReverse.
- [ ] Polish this repository.
- [ ] Prepare slides.


## Quick-Start
* Clone this source-code repository:

  `git clone git@github.com:afaquejam/PythonAwesomeApp.git`

* Set up the Python's Virtual Env.
  ```
  python3 -m venv virtualenv
  source virtualenv/bin/activate
  ```
* Install dependencies:

  `pip3 install -r requirements.txt`

* Run the tests:

  `make test`
  
* If you'd like to upgrade the project's dependencies:

  `make upgrade-dependencies`

* Turn off the Python VirtualEnv.

  `deactivate`

## Source-Code Organization
```
.
├── awesome_app
├── awesome_app_test
├── _config.yml
├── docs
│   └── source_code_org.md
├── LICENSE
├── makefile
├── package_one
│   ├── config
│   │   └── integer_adder.cfg
│   ├── module_one.py
│   └── tests
│       └── test_integer_adder.py
├── package_two
│   ├── config
│   │   └── module_two.cfg
│   ├── errors.py
│   ├── module_two.py
│   └── tests
│       └── test_public_ip_address_class.py
├── README.md
└── requirements.txt

7 directories, 15 files
```

## Testing & Mocking
* Use Pytest.
  - Use pytest fixtures for set-up and teardown functions.
  - Use parametrized tests.
  - Use pytest-cov to generate test reports.
  - Use pytest plugins to enhance your test reports.
* Mocking
  - Use unittest.mock

## Profiling
* Measuing running time of a program:
  ```
  python3 -m cProfile -o app.prof awesome_app
  snakeviz app.prof
  ```
* Measuring Memroy Consumption of a program:
  ```
  mprof run ./awesome_app
  mprof plot
  ```

* Measuring I/O
  - Network: `nethogs`
  - Disk: `iotop`
  - Both provide rudimentary interface to view the I/O information.

## Linting
* PEP 8 style guide (https://bit.ly/1ARqSBt) is recommended.
* Automate linting in your favorite code-editor.
* For example, in Visual Studio Code, install the `Python` package which will automate the linting for your python source-code.

## Documentation
* Changelog, git-tagging & release notes.
  - Changelog guidelines by `Keep a Changelog` are recommended: https://keepachangelog.com/en/1.0.0/
  - Use `git-tags` to tag your git repository and keep it consistent with the changelog.
  - Maintaining release notes is up-to you how you maintain them. Example release notes: https://atom.io/releases
  - You might argue that what's the difference between between changelog and release notes? In my opinion, changelog is much more verbose than release notes. However it's up-to you how you differentiate between them.

* User documentation
  - Please make sure you have instructions how to install your software, it's dependencies and run it.

* Developer documentation
  - Make sure you have relevant documentation for developers such that they can navigate, read, understand and contribute to the project.

## Packaging & Release
* Information on packaging and release.

## Other Relevant Topics
* Async operation
* Multi-threading
* Multi-processing
* PyPy
* PyReverse
