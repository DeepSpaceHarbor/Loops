from loops.Attacks import AttackTypes
import random


def generate_attack_groups(groupCount, membersCount, sharedAttacks=True):
    if sharedAttacks is False and (groupCount * membersCount) > len(AttackTypes):
        return []
    groups = []
    seenAttacks = []
    for groupID in range(0, groupCount):
        tmpGroup = []
        for memberID in range(0, membersCount):
            attack = random.choice(list(AttackTypes))
            if sharedAttacks:
                tmpGroup.append(attack)
            else:
                while attack in seenAttacks:
                    attack = random.choice(list(AttackTypes))
                tmpGroup.append(attack)
                seenAttacks.append(attack)
        groups.append(tmpGroup)
    return groups


def generate_attack_groups_from(groupCount, membersCount, sharedAttacks=True, attacksList=[]):
    if sharedAttacks is False and (groupCount * membersCount) > len(attacksList):
        return []
    groups = []
    seenAttacks = []
    for groupID in range(0, groupCount):
        tmpGroup = []
        for memberID in range(0, membersCount):
            attack = random.choice(list(attacksList))
            if sharedAttacks:
                tmpGroup.append(attack)
            else:
                while attack in seenAttacks:
                    attack = random.choice(list(attacksList))
                tmpGroup.append(attack)
                seenAttacks.append(attack)
        groups.append(tmpGroup)
    return groups


def generate_attack_groups_without(groupCount, membersCount, sharedAttacks=True, excludedAttacks=[]):
    if sharedAttacks is False and (groupCount * membersCount) > len(AttackTypes) - len(excludedAttacks):
        return []
    approvedAttacks = []
    for attack in AttackTypes:
        if attack not in excludedAttacks:
            approvedAttacks.append(attack)
    return generate_attack_groups_from(groupCount,membersCount,sharedAttacks,approvedAttacks)
