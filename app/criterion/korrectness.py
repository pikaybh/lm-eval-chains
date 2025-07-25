from app.schemas import EvaluationOutput
from app.utils import get_prompt



class KorrectnessEvaluator:
    def __init__(self, core_model):
        self.prompt_template = get_prompt("korrectness")
        self.core_model = core_model.with_structured_output(EvaluationOutput)

    def __call__(self, inputs: dict, outputs: dict, reference_outputs: dict) -> bool:
        """
        TRUE if the output is factually accurate, complete, logically consistent, and matches the reference output in key information. FALSE if there are any factual errors, missing information, logical inconsistencies, or significant deviations from the reference output.
        """
        prompt = self.prompt_template.format(inputs=inputs, outputs=outputs, reference_outputs=reference_outputs)
        response = self.core_model.invoke(prompt)

        return str(response.correctness).lower() == "true"



__all__ = ["KorrectnessEvaluator"]