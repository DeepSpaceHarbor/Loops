import foolbox
from loops.Attacks import AttackTypes


# List of attack modules:
# https://foolbox.readthedocs.io/en/latest/modules/attacks.html

# Gradient-based attacks
def GradientSignAttack(model, image, label):
    attack = foolbox.attacks.FGSM(model)
    return attack(image, label)


def IterativeGradientSignAttack(model, image, label):
    attack = foolbox.attacks.IterativeGradientSignAttack(model)
    return attack(image, label)


def GradientAttack(model, image, label):
    attack = foolbox.attacks.GradientAttack(model)
    return attack(image, label)


def IterativeGradientAttack(model, image, label):
    attack = foolbox.attacks.IterativeGradientAttack(model)
    return attack(image, label)


def LBFGSAttack(model, image, label):
    attack = foolbox.attacks.LBFGSAttack(model)
    return attack(image, label)


def DeepFoolAttack(model, image, label):
    attack = foolbox.attacks.DeepFoolAttack(model)
    return attack(image, label)


def DeepFoolL2Attack(model, image, label):
    attack = foolbox.attacks.DeepFoolL2Attack(model)
    return attack(image, label)


def DeepFoolLinfinityAttack(model, image, label):
    attack = foolbox.attacks.DeepFoolLinfinityAttack(model)
    return attack(image, label)


def SLSQPAttack(model, image, label):
    attack = foolbox.attacks.SLSQPAttack(model)
    return attack(image, label)


def SaliencyMapAttack(model, image, label):
    attack = foolbox.attacks.SaliencyMapAttack(model)
    return attack(image, label)


# Score-based attacks
def SinglePixelAttack(model, image, label):
    attack = foolbox.attacks.SinglePixelAttack(model)
    return attack(image, label)


def LocalSearchAttack(model, image, label):
    attack = foolbox.attacks.LocalSearchAttack(model)
    return attack(image, label)


def ApproximateLBFGSAttack(model, image, label):
    attack = foolbox.attacks.ApproximateLBFGSAttack(model)
    return attack(image, label)


# Decision-based attacks
def BoundaryAttack(model, image, label):
    attack = foolbox.attacks.BoundaryAttack(model)
    return attack(image, label)


def GaussianBlurAttack(model, image, label):
    attack = foolbox.attacks.GaussianBlurAttack(model)
    return attack(image, label)


def ContrastReductionAttack(model, image, label):
    attack = foolbox.attacks.ContrastReductionAttack(model)
    return attack(image, label)


def AdditiveUniformNoiseAttack(model, image, label):
    attack = foolbox.attacks.AdditiveUniformNoiseAttack(model)
    return attack(image, label)


def AdditiveGaussianNoiseAttack(model, image, label):
    attack = foolbox.attacks.AdditiveGaussianNoiseAttack(model)
    return attack(image, label)


def SaltAndPepperNoiseAttack(model, image, label):
    attack = foolbox.attacks.SaltAndPepperNoiseAttack(model)
    return attack(image, label)


def BlendedUniformNoiseAttack(model, image, label):
    attack = foolbox.attacks.BlendedUniformNoiseAttack(model)
    return attack(image, label)


def PointwiseAttack(model, image, label):
    attack = foolbox.attacks.PointwiseAttack(model)
    return attack(image, label)


def strike(model, input, label, attack):
    if attack is AttackTypes.GradientSignAttack:
        return GradientSignAttack(model, input, label)
    if attack is AttackTypes.IterativeGradientSignAttack:
        return IterativeGradientSignAttack(model, input, label)
    if attack is AttackTypes.GradientAttack:
        return GradientAttack(model, input, label)
    if attack is AttackTypes.IterativeGradientAttack:
        return IterativeGradientAttack(model, input, label)
    if attack is AttackTypes.LBFGSAttack:
        return LBFGSAttack(model, input, label)
    if attack is AttackTypes.DeepFoolAttack:
        return DeepFoolAttack(model, input, label)
    if attack is AttackTypes.DeepFoolL2Attack:
        return DeepFoolL2Attack(model, input, label)
    if attack is AttackTypes.DeepFoolLinfinityAttack:
        return DeepFoolLinfinityAttack(model, input, label)
    if attack is AttackTypes.SLSQPAttack:
        return SLSQPAttack(model, input, label)
    if attack is AttackTypes.SaliencyMapAttack:
        return SaliencyMapAttack(model, input, label)
    if attack is AttackTypes.SinglePixelAttack:
        return SinglePixelAttack(model, input, label)
    if attack is AttackTypes.LocalSearchAttack:
        return LocalSearchAttack(model, input, label)
    if attack is AttackTypes.ApproximateLBFGSAttack:
        return ApproximateLBFGSAttack(model, input, label)
    if attack is AttackTypes.BoundaryAttack:
        return BoundaryAttack(model, input, label)
    if attack is AttackTypes.GaussianBlurAttack:
        return GaussianBlurAttack(model, input, label)
    if attack is AttackTypes.ContrastReductionAttack:
        return ContrastReductionAttack(model, input, label)
    if attack is AttackTypes.AdditiveUniformNoiseAttack:
        return AdditiveUniformNoiseAttack(model, input, label)
    if attack is AttackTypes.AdditiveGaussianNoiseAttack:
        return AdditiveGaussianNoiseAttack(model, input, label)
    if attack is AttackTypes.SaltAndPepperNoiseAttack:
        return SaltAndPepperNoiseAttack(model, input, label)
    if attack is AttackTypes.BlendedUniformNoiseAttack:
        return BlendedUniformNoiseAttack(model, input, label)
    if attack is AttackTypes.PointwiseAttack:
        return PointwiseAttack(model, input, label)

    raise ValueError('Invalid attack.', attack)
