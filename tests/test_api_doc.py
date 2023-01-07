from .utils import get_paths
from .views import PetView


class TestPathHelpers:
    def test_class_view(self, app, spec):
        PetView.register(app, trailing_slash=False)
        spec.paths(PetView)
        paths = get_paths(spec)

        assert "get" in paths["/pet"]
        assert "post" in paths["/pet"]
        assert "put" in paths["/pet/{id}"]
        assert "delete" in paths["/pet/{id}"]
        assert "get" in paths["/pet/custom_route"]
        assert "/pet/_not_registered_route" not in paths
