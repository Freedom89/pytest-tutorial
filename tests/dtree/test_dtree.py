from src.dtree import dtree
from src.dtree.types import RawData, IntFeat, Response, Category

sample_input = RawData(**dict(x=6, y=2, z=100, category=Category.A))
sample_feat = IntFeat(**{"x": 6, "x_times_y": 12, "y_div_z": 0.02, "cat_in_AB": True})
sample_response = Response.value4


def test_compute_int_feat():
    assert dtree.compute_int_feat(sample_input) == sample_feat, "something went wrong"


def test_compute_response():
    assert (
        dtree.compute_response(sample_feat) == sample_response
    ), "something went wrong"

# parametrize left as an exercise

