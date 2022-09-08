"""MODELS - COMMON
"""

# # Installed # #
import pydantic

__all__ = ("BaseModel",)

class BaseModel(pydantic.BaseModel):

    @pydantic.root_validator(pre=True)
    def _min_properties(cls, data):
        if not data:
            raise ValueError("Ao menos um parametro requerido")
        return data

    def dict(self, include_nulls=False, **kwargs):
        kwargs["exclude_none"] = not include_nulls
        return super().dict(**kwargs)

    class Config:
        extra = pydantic.Extra.forbid
        anystr_strip_whitespace = True
