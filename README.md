![](VACUUM_banner.png)

# VACUUM 0.1

VACUUM (Visual Audio Comparison Utilty Understanding Measurement) is an open-source tool created for the [Piano Project](http://www.david11n.myweb.cs.uwindsor.ca/60499/w/The_Piano_Project) to aid in the evaluation phase as part of my senior research project. 

The current version of VACUUM 0.1 inspects an audio file, detects small differences in simple audio files and display the results graphically. Future versions will handle the full complexity of our audio files and allows us to quickly compare the effectiveness of our construction techniques.

VACUUM 0.1 is a `Jupyter Notebook` based series of Python scripts that makes use of the `Librosa`, `matplotlib` and `OpenCV` libraries. VACUUM takes advantage of Python virtual environment tool `venv` to make gathering dependencies and installinbg on a new machine simple.

If you're reading this now you are seeing that I had to hit a deadline and uploaded a messy repository. Sorry that you have to see that! By the time you come back, I'll have the place all cleaned up. 

## Dependencies

Like most Python scripts that use even a a single library, VACUUM has a long list of dependencies – *good thing for* `venv` *and a* `Requirements.txt`! Development and testing was done on Python 3.7 but it should work without problem on anything 3.4+.

|                                     |                                          |                           |
| :---------------------------------: | :--------------------------------------: | :-----------------------: |
|           appnope==0.1.0            |            jupyter-core==4.4.0           |      pycparser==2.19      |
|           astroid==2.2.5            |  jupyter-highlight-selected-word==0.2.0  |       pygame==1.9.4       |
|            attrs==19.1.0            |         jupyter-latex-envs==1.4.6        |      Pygments==2.3.1      |
|          audioread==2.1.6           | jupyter-nbextensions-configurator==0.4.1 |       pylint==2.3.1       |
|           autopep8==1.4.3           |             kiwisolver==1.0.1            |      pyparsing==2.3.1     |
|           backcall==0.1.0           |         lazy-object-proxy==1.3.1         |    pyrsistent==0.14.11    |
|            bleach==3.1.0            |              librosa==0.6.3              |   python-dateutil==2.8.0  |
|            cffi==1.12.2             |             llvmlite==0.28.0             |     PyWavelets==1.0.2     |
|         cloudpickle==0.8.1          |                lxml==4.3.3               |        PyYAML==5.1        |
|           cycler==0.10.0            |             MarkupSafe==1.1.1            |       pyzmq==18.0.1       |
|             dask==1.1.4             |             matplotlib==3.0.3            |      qtconsole==4.4.3     |
|          decorator==4.4.0           |               mccabe==0.6.1              |       resampy==0.2.1      |
|          defusedxml==0.5.0          |              mistune==0.8.4              |    scikit-image==0.14.2   |
|          entrypoints==0.3           |             nbconvert==5.4.1             |    scikit-learn==0.20.3   |
|           imutils==0.5.2            |              nbformat==4.4.0             |        scipy==1.2.1       |
|          ipykernel==5.1.0           |               networkx==2.2              |     Send2Trash==1.5.0     |
|           ipython==7.4.0            |              notebook==5.7.6             |        six==1.12.0        |
|       ipython-genutils==0.2.0       |               numba==0.43.1              |     SoundFile==0.10.2     |
|          ipywidgets==7.4.2          |               numpy==1.16.2              |      terminado==0.8.1     |
|            isort==4.3.16            |      opencv-contrib-python==4.0.0.21     |      testpath==0.4.2      |
|            jedi==0.13.3             |           pandocfilters==1.4.2           |        toolz==0.9.0       |
|            Jinja2==2.10             |               parso==0.3.4               |       tornado==6.0.2      |
|           joblib==0.13.2            |              pexpect==4.6.0              |      traitlets==4.3.2     |
|          jsonschema==3.0.1          |            pickleshare==0.7.5            |      typed-ast==1.3.1     |
|           jupyter==1.0.0            |               Pillow==5.4.1              |       wcwidth==0.1.7      |
|        jupyter-client==5.2.4        |         prometheus-client==0.6.0         |    webencodings==0.5.1    |
|       jupyter-console==6.0.0        |           prompt-toolkit==2.0.9          | widgetsnbextension==3.4.2 |
|     jupyter-contrib-core==0.3.3     |             ptyprocess==0.6.0            |       wrapt==1.11.1       |
| jupyter-contrib-nbextensions==0.5.1 |            pycodestyle==2.5.0            |                           |

## Installation

Installation should be pretty straight forward. These instructions are tested on MacOS 10.13.6 and assume you have Python 3.7+ installed and running.

	git clone https://github.com/tukanuk/VACUUM.git
	cd VACUUM

Now, if I were you, I'd use `venv` or some other virtual environment tool to keep things tidy, but ultimately that's your call

	python3 -m venv venv 				# creates a vritual enviroment called `venv` in the current folder
	source ./venv/bin/activate  		# to activate
	
	pip3 install -r requirements.txt 	# install all the dependencies 

If you are using a virtual environment of have a fairly clean install of Python on your system, this will likely take several minutes. Make a coffee!

Once that's finished, you should be ready to go so let's start up Jupyter Notebooks

	python3 -m notebook					# start the notebook server
	
From there you should be able to see `VACUUM.ipynb` in the browsers. Click and go!
	
	deactivate							# don't forget turn off your venv when you are finished

## Built With

- [Librosa](http://librosa.github.io) - Audio framework
- [OpenCV](https://opencv.org) - Computer Vision framework
- [matplotlib](https://matplotlib.org) - Plotting library
- [Jupyter Notebook](https://jupyter.org) - Creating and sharing live code

## Authors

- **Ben Davidson** - *Initial work* - [web](https://idavidson.ca)

## Acknowledgements

- [Image Difference with OpenCV and Python](https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/) at [pyimagesearch](https://www.pyimagesearch.com) for the OpenCV tutorials