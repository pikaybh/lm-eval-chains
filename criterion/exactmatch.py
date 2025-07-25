class ExactMatch:
    def __call__(self, outputs: dict, reference_outputs: dict) -> bool:
        return outputs == reference_outputs
    
__all__ = ["ExactMatch"]