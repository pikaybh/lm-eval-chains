from langsmith import evaluate, Client

from criterion import ExactMatch, Korrectness



class PiRatingEvaluator:
    def __init__(self, dataset_name: str, target_chain, core_model, prefix: str | None = None):
        self.dataset_name = dataset_name
        self.target_chain = target_chain
        self.core_moeld = core_model
        self.prefix = prefix

    def __call__(self):
        client = Client()
        
        return evaluate(
            # lambda x: x["공정"] + "is a good question. I don't know the answer.",
            self.target_chain.invoke,  # Use full_chain.invoke for the LCEL chain
            # graph.invoke
            data=self.dataset_name,
            evaluators=[
                Korrectness(self.core_model),
                ExactMatch()
            ],
            experiment_prefix=self.prefix
        )



__all__ = ["PiRatingEvaluator"]