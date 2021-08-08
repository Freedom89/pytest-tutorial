# More on pytests and fixtures

[Full article post](www.dataraccoon.com/knowledge/testing_fixtures)

# Running locally with Make

To run the full suite of tests: 

```
make run
```

To run a small selection or marking:

```
make mark_session
```

or

```
make mark type=session
```

# Running it with docker

```
make d_build
make d_run
```

# Custom tests

For example if you only want to run the function section with pytestm mark:

```
make d_build
make d_run sel=func
```
