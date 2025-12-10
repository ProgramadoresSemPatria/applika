from datetime import date

from pydantic import BaseModel, model_validator
from typing_extensions import Literal

from app.application.dto import BaseSchema


class ApplicationCreateDTO(BaseModel):
    user_id: int
    company: str
    role: str
    mode: Literal['active', 'passive']
    platform_id: int
    application_date: date
    observation: str | None = None
    expected_salary: float | None = None
    salary_range_min: float | None = None
    salary_range_max: float | None = None


class ApplicationUpdateDTO(BaseModel):
    user_id: int
    company: str
    role: str
    mode: Literal['active', 'passive']
    platform_id: int
    application_date: date
    observation: str | None = None
    expected_salary: float | None = None
    salary_range_min: float | None = None
    salary_range_max: float | None = None


class FinalizeApplicationDTO(BaseModel):
    step_id: int  # only strict steps
    feedback_id: int
    finalize_date: date
    salary_offer: float | None = None
    observation: str | None = None


class ApplicationLastStep(BaseModel):
    id: int
    name: str
    color: str
    date: date


class ApplicationFeedback(BaseModel):
    id: int
    name: str
    color: str
    date: date


class ApplicationDTO(BaseSchema):
    company: str
    role: str
    mode: Literal['active', 'passive']
    platform_id: int
    application_date: date
    observation: str | None = None
    expected_salary: float | None = None
    salary_range_min: float | None = None
    salary_range_max: float | None = None
    salary_offer: float | None = None

    last_step: ApplicationLastStep | None = None
    feedback: ApplicationFeedback | None = None

    finalized: bool = False

    @model_validator(mode='after')
    def set_finalized(self) -> 'ApplicationDTO':
        self.finalized = self.feedback is not None
        return self
