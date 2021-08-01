args:=pytest
localargs:=python -m pytest

dockerbuild:
	docker build -t docker_tests .

dockertests: dockerbuild
	docker run --rm -it \
	--env PYTHONPATH="${PYTHONPATH}:/workspaces/pytest-tutorial/" \
	docker_tests $(args)

dockerbash: dockerbuild
	docker run --rm -it -p 8888:8888 \
	-v $(shell pwd):/tutorial \
	--env PYTHONPATH="${PYTHONPATH}:/workspaces/pytest-tutorial/" \
	--entrypoint bash docker_tests

dockermain: dockerbuild
	docker run --rm -it \
	--env PYTHONPATH="${PYTHONPATH}:/workspaces/pytest-tutorial/" \
	docker_tests python src/main.py

c8_folder: 
	mkdir src/${f}
	touch src/${f}/__init__.py
	mkdir tests/${f}

c8_script:
	touch src/${f}/${n}
	touch tests/${f}/test_${n}
	
localtest:
	$(localargs)

testall:
	pytest tests

testverbose:
	pytest tests -v

testscript:
	pytest tests/eg_demo_mock.py

testbyname:
	pytest -k "rm_trailing"

testbyname2:
	pytest -k "rm and not numbers"

testcollect:
	pytest --collect-only

testfirstfail:
	pytest -x

