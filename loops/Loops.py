from typing import Any
from loops.FoolboxAttackWrapper import strike
from loops.Attacks import AttackTypes
import foolbox
import keras
import numpy as np
import random


class LoopAttack:
    loops = 10
    model = None

    def __init__(self, model, bounds, loops=10) -> None:
        super().__init__()
        self.loops = loops
        self.model = foolbox.models.KerasModel(model, bounds)

    def getLabel(self, input):
        if input is None:
            return input
        else:
            return np.argmax(self.model.predictions(input))

    def attack(self, loop, input, attack, preprocess=None, postprocess=None):
        labelOriginal = self.getLabel(input)
        if preprocess is not None:
            input = preprocess(loop, input, labelOriginal)
        labelOriginal = self.getLabel(input)
        advExample = strike(self.model, input, labelOriginal, attack)
        labelAdversarial = self.getLabel(advExample)
        if postprocess is not None:
            advExample = postprocess(loop, input, labelOriginal, attack, advExample, labelAdversarial)
        return {
            "loop": loop,
            "input": input,
            "labelOriginal": labelOriginal,
            "attack": attack,
            "adversarialExample": advExample,
            "labelAdversarial": labelAdversarial
        }

    def single(self, data, attack, preprocess=None, postprocess=None):
        adversarialExamples = []
        for loop in range(0, self.loops):
            advExample = self.attack(loop, data, attack, preprocess, postprocess)
            if advExample["adversarialExample"] is not None:
                data = advExample["adversarialExample"]
            adversarialExamples.append(advExample)
        return adversarialExamples

    def all(self, data, preprocess=None, postprocess=None):
        adversarialExamples = []
        attack = random.choice(list(AttackTypes))
        oldAttack = []
        for loop in range(0, self.loops):
            if len(oldAttack) == len(AttackTypes):
                oldAttack = []
            while attack in oldAttack:
                attack = random.choice(list(AttackTypes))
            advExample = self.attack(loop, data, attack, preprocess, postprocess)
            if advExample["adversarialExample"] is not None:
                data = advExample["adversarialExample"]
            adversarialExamples.append(advExample)
            oldAttack.append(attack)
        return adversarialExamples

    def any_of(self, data, attacks, preprocess=None, postprocess=None):
        adversarialExamples = []
        attack = random.choice(list(attacks))
        oldAttack = []
        for loop in range(0, self.loops):
            if len(oldAttack) == len(attacks):
                oldAttack = []
            while attack in oldAttack:
                attack = random.choice(list(attacks))
            advExample = self.attack(loop, data, attack, preprocess, postprocess)
            if advExample["adversarialExample"] is not None:
                data = advExample["adversarialExample"]
            adversarialExamples.append(advExample)
            oldAttack.append(attack)
        return adversarialExamples

    def all_except(self, data, attacks, preprocess=None, postprocess=None):
        adversarialExamples = []
        attack = random.choice(list(AttackTypes))
        oldAttack = []
        for loop in range(0, self.loops):
            if len(oldAttack) == (len(AttackTypes) - len(attacks)):
                oldAttack = []
            while attack in oldAttack or attack in attacks:
                attack = random.choice(list(AttackTypes))
            advExample = self.attack(loop, data, attack, preprocess, postprocess)
            if advExample["adversarialExample"] is not None:
                data = advExample["adversarialExample"]
            adversarialExamples.append(advExample)
            oldAttack.append(attack)
        return adversarialExamples
