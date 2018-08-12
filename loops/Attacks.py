from enum import Enum, unique


@unique
class AttackTypes(Enum):
    GradientSignAttack = "GradientSignAttack"
    IterativeGradientSignAttack = "IterativeGradientSignAttack"
    GradientAttack = "GradientAttack"
    IterativeGradientAttack = "IterativeGradientAttack"
    LBFGSAttack = "LBFGSAttack"
    DeepFoolAttack = "DeepFoolAttack"
    DeepFoolL2Attack = "DeepFoolL2Attack"
    DeepFoolLinfinityAttack = "DeepFoolLinfinityAttack"
    SLSQPAttack = "SLSQPAttack"
    SaliencyMapAttack = "SaliencyMapAttack"
    SinglePixelAttack = "SinglePixelAttack"
    LocalSearchAttack = "LocalSearchAttack"
    ApproximateLBFGSAttack = "ApproximateLBFGSAttack"
    BoundaryAttack = "BoundaryAttack"
    GaussianBlurAttack = "GaussianBlurAttack"
    ContrastReductionAttack = "ContrastReductionAttack"
    AdditiveUniformNoiseAttack = "AdditiveUniformNoiseAttack"
    AdditiveGaussianNoiseAttack = "AdditiveGaussianNoiseAttack"
    SaltAndPepperNoiseAttack = "SaltAndPepperNoiseAttack"
    BlendedUniformNoiseAttack = "BlendedUniformNoiseAttack"
    PointwiseAttack = "PointwiseAttack"

    def __str__(self):
        return str(self.value)
