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

    def _getLabel(self, input):
        if input is None:
            return input
        else:
            return np.argmax(self.model.predictions(input))

    def _attack(self, loop, input, attack, preprocess=None, postprocess=None):
        print("Starting loop: " + str(loop))
        labelOriginal = self._getLabel(input)
        if preprocess is not None:
            print("Data preprocessing...")
            input = preprocess(loop, input, labelOriginal)
        print("Getting label...")
        labelOriginal = self._getLabel(input)
        print("Done.\nAttack in 3, 2, 1...")
        print("Attacking with: " + str(attack))
        advExample = strike(self.model, input, labelOriginal, attack)
        labelAdversarial = self._getLabel(advExample)
        if postprocess is not None:
            print("Data postprocessing...")
            advExample = postprocess(loop, input, labelOriginal, attack, advExample, labelAdversarial)
        print("Loop " + str(loop) + " is completed.")
        return {
            "loop": loop,
            "input": input,
            "labelOriginal": labelOriginal,
            "attack": attack,
            "adversarialExample": advExample,
            "labelAdversarial": labelAdversarial
        }

    def _best_of(self, loop, data, compare, attacksList, preprocess=None, postprocess=None):
        maxScore = None
        maxAdversarial = None
        for attack in attacksList:
            adversarial = self._attack(loop, data, attack, preprocess, postprocess)
            score = compare(adversarial)
            print("Attacked: ", attack,"Result: ",score)
            if maxScore is None:
                maxScore = score
                maxAdversarial = adversarial
            if score > maxScore:
                maxScore = score
                maxAdversarial = adversarial
        return maxAdversarial

    def single(self, data, attack, preprocess=None, postprocess=None):
        adversarialExamples = []
        for loop in range(0, self.loops):
            advExample = self._attack(loop, data, attack, preprocess, postprocess)
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
            advExample = self._attack(loop, data, attack, preprocess, postprocess)
            if advExample["adversarialExample"] is not None:
                data = advExample["adversarialExample"]
            adversarialExamples.append(advExample)
            oldAttack.append(attack)
        return adversarialExamples

    def all_random(self, data, preprocess=None, postprocess=None):
        adversarialExamples = []
        attack = random.choice(list(AttackTypes))
        loop = 0
        while loop < self.loops:
            loop += 1
            attack = random.choice(list(AttackTypes))
            advExample = self._attack(loop, data, attack, preprocess, postprocess)
            if advExample["adversarialExample"] is not None:
                data = advExample["adversarialExample"]
            adversarialExamples.append(advExample)
        return adversarialExamples

    def all_best_of(self, data, compare, preprocess=None, postprocess=None):
        adversarialExamples = []
        for loop in range(0, self.loops):
            advExample = self._best_of(loop, data, compare, AttackTypes, preprocess, postprocess)
            if advExample["adversarialExample"] is not None:
                data = advExample["adversarialExample"]
            adversarialExamples.append(advExample)
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
            advExample = self._attack(loop, data, attack, preprocess, postprocess)
            if advExample["adversarialExample"] is not None:
                data = advExample["adversarialExample"]
            adversarialExamples.append(advExample)
            oldAttack.append(attack)
        return adversarialExamples

    def any_of_random(self, data, attacks, preprocess=None, postprocess=None):
        adversarialExamples = []
        attack = random.choice(list(attacks))
        loop = 0
        while loop < self.loops:
            loop += 1
            attack = random.choice(list(attacks))
            advExample = self._attack(loop, data, attack, preprocess, postprocess)
            if advExample["adversarialExample"] is not None:
                data = advExample["adversarialExample"]
            adversarialExamples.append(advExample)
        return adversarialExamples


    def any_of_best_of(self, data, attacks, compare, preprocess=None, postprocess=None):
        adversarialExamples = []
        for loop in range(0, self.loops):
            advExample = self._best_of(loop, data, compare, attacks, preprocess, postprocess)
            if advExample["adversarialExample"] is not None:
                data = advExample["adversarialExample"]
            adversarialExamples.append(advExample)
        return adversarialExamples

    def all_except(self, data, excludedAttacks, preprocess=None, postprocess=None):
        attacksList = []
        for attack in AttackTypes:
            if attack not in excludedAttacks:
                attacksList.append(attack)
        return self.any_of(data,attacksList,preprocess,postprocess)

    def all_except_random(self, data, excludedAttacks, preprocess=None, postprocess=None):
        attacksList = []
        for attack in AttackTypes:
            if attack not in excludedAttacks:
                attacksList.append(attack)
        return self.any_of_random(data,attacksList,preprocess,postprocess)


    def all_except_best_of(self, data, excludedAttacks, preprocess=None, postprocess=None):
        attacksList = []
        for attack in AttackTypes:
            if attack not in excludedAttacks:
                attacksList.append(attack)
        return self.any_of_best_of(data,attacksList,preprocess,postprocess)
