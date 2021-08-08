run:
	pytest

run_all:
	pytest tests/test_all.py

run_all_autouse:
	pytest tests/test_all_autouse.py

type=function
mark:
	pytest -m $(type)

mark_func: type=function
mark_func: mark

mark_class:type=class_
mark_class: mark

mark_module: type=module
mark_module: mark

mark_session: type=session
mark_session: mark

image=test_my_code
d_build:
	docker build -t $(image) . 

sel=run
d_run:
	docker run -it $(image) $(sel)

d_bash:
	docker run -it -p 8888:8888 --entrypoint bash $(image)