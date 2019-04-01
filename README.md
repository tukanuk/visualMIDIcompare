![](VACUUM_banner.png)

VACUUM (Visual Audio Comparison Utilty Understanding Measurement) is an open-source tool created for the [Piano Project](http://www.david11n.myweb.cs.uwindsor.ca/60499/w/The_Piano_Project) to aid in the evaluation phase as part of my senior research project. 

The current version of VACUUM 0.1 inspects an audio file, detects small differences in simple audio files and display the results graphically. Future versions will handle the full complexity of our audio files and allows us to quickly compare the effectiveness of our construction techniques.

VACUUM 0.1 is a `Jupyter Notebook` based series of Python scripts that makes use of the `Librosa`, `matplotlib` and `OpenCV` libraries. VACUUM takes advantage of Python virtual environment tool `venv` to make gathering dependencies and installinbg on a new machine simple. 

## Dependencies

Like most Python scripts that use even a a single library, VACUUM has a long list of dependencies – ''good thing for'' `venv` ''and a'' `Requirements.txt`! Development and testing was done on Python 3.7 but it should work without problem on anything 3.4+.

	appnope==0.1.0
	astroid==2.2.5
	attrs==19.1.0
	audioread==2.1.6
	autopep8==1.4.3
	backcall==0.1.0
	bleach==3.1.0
	cffi==1.12.2
	cloudpickle==0.8.1
	cycler==0.10.0
	dask==1.1.4
	decorator==4.4.0
	defusedxml==0.5.0
	entrypoints==0.3
	imutils==0.5.2
	ipykernel==5.1.0
	ipython==7.4.0
	ipython-genutils==0.2.0
	ipywidgets==7.4.2
	isort==4.3.16
	jedi==0.13.3
	Jinja2==2.10
	joblib==0.13.2
	jsonschema==3.0.1
	jupyter==1.0.0
	jupyter-client==5.2.4
	jupyter-console==6.0.0
	jupyter-contrib-core==0.3.3
	jupyter-contrib-nbextensions==0.5.1
	jupyter-core==4.4.0
	jupyter-highlight-selected-word==0.2.0
	jupyter-latex-envs==1.4.6
	jupyter-nbextensions-configurator==0.4.1
	kiwisolver==1.0.1
	lazy-object-proxy==1.3.1
	librosa==0.6.3
	llvmlite==0.28.0
	lxml==4.3.3
	MarkupSafe==1.1.1
	matplotlib==3.0.3
	mccabe==0.6.1
	mistune==0.8.4
	nbconvert==5.4.1
	nbformat==4.4.0
	networkx==2.2
	notebook==5.7.6
	numba==0.43.1
	numpy==1.16.2
	opencv-contrib-python==4.0.0.21
	pandocfilters==1.4.2
	parso==0.3.4
	pexpect==4.6.0
	pickleshare==0.7.5
	Pillow==5.4.1
	prometheus-client==0.6.0
	prompt-toolkit==2.0.9
	ptyprocess==0.6.0
	pycodestyle==2.5.0
	pycparser==2.19
	pygame==1.9.4
	Pygments==2.3.1
	pylint==2.3.1
	pyparsing==2.3.1
	pyrsistent==0.14.11
	python-dateutil==2.8.0
	PyWavelets==1.0.2
	PyYAML==5.1
	pyzmq==18.0.1
	qtconsole==4.4.3
	resampy==0.2.1
	scikit-image==0.14.2
	scikit-learn==0.20.3
	scipy==1.2.1
	Send2Trash==1.5.0
	six==1.12.0
	SoundFile==0.10.2
	terminado==0.8.1
	testpath==0.4.2
	toolz==0.9.0
	tornado==6.0.2
	traitlets==4.3.2
	typed-ast==1.3.1
	wcwidth==0.1.7
	webencodings==0.5.1
	widgetsnbextension==3.4.2
	wrapt==1.11.1
