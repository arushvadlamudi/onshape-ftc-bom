"""Tests for onshape_ftc_bom."""

from onshape_ftc_bom import OnshapeFtcBom, OnshapeFtcBomOptions


class TestOnshapeFtcBom:
    def test_create_instance_with_defaults(self) -> None:
        instance = OnshapeFtcBom()
        assert instance is not None

    def test_create_instance_with_options(self) -> None:
        options = OnshapeFtcBomOptions(verbose=True)
        instance = OnshapeFtcBom(options)
        assert instance.options.verbose is True

    def test_run_successfully(self) -> None:
        instance = OnshapeFtcBom()
        result = instance.run()
        assert result.success is True
        assert result.data is not None

    def test_run_returns_result_type(self) -> None:
        instance = OnshapeFtcBom()
        result = instance.run()
        assert result.error is None
