all: jselect.py
	@chmod a+x jselect.py
	@sudo cp jselect.py /usr/local/bin/jselect
	@chmod a-x jselect.py
