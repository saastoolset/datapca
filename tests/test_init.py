"""Tests for `datapca` package."""


def test_pca_namespace():
    """Test the package is accessible through the `pca` namespace"""
    from pca.packages import datapca

    assert hasattr(datapca, "VERSION")
