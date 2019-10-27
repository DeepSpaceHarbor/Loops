
Loops is a tool for generating lots of untargeted adversarial examples, created as part of my [bachelor's thesis](https://github.com/RandomAdversary/Presentations/tree/master/FCSE%20%202019%20%7C%20bachelor's%20thesis).

**This is proof of concept** code. It's not meant to be integrated with other tools.

## Why?
Lots of techiniques for adversarial examples are aimed are minimizing distance metrics such as L2 and L∞. This is good in theory, because it allows for an easy comparison between different attacks. In practice however, there are scenarious where these measures are irrelevant.

## How?

This version uses simple chaining with a subset of attack algorithms available in [Foolbox](https://github.com/bethgelab/foolbox).


## Usage
Some code examples can be found in the project [wiki](https://github.com/RandomAdversary/Loops/wiki).
