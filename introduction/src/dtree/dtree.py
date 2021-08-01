from src.dtree.types import RawData, IntFeat, Response


def compute_int_feat(input: RawData) -> IntFeat:
    val_x = input.x
    val_xy = input.x * input.y
    val_y_div_z = input.y / input.z
    val_in_AB = input.category.value in ["A", "B"]
    return IntFeat(x=val_x, x_times_y=val_xy, y_div_z=val_y_div_z, cat_in_AB=val_in_AB)


def compute_response(input: IntFeat) -> Response:
    if input.x > 5:
        if input.x_times_y > 10:
            return Response.value4
        else:
            if input.y_div_z < 100:
                return Response.value3
            else:
                return Response.value2
    else:
        if input.cat_in_AB:
            return Response.value1
        else:
            return Response.value0
