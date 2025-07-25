from pydantic import BaseModel, Field



class EvaluationOutput(BaseModel):
    comment: str = Field(default="",
                        description="A comment on the evaluation result, if any.")
    correctness: bool = Field(default=False,
                            description="Whether the output is factually correct and complete according to the evaluation criteria.")



__all__ = ["EvaluationOutput"]