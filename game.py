"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	UNARMED_POWER = 20
	def __init__(self,name,power, min_level) -> None:
		self.__name=name
		self.power =power
		self.min_level=min_level

	@property
	def name(self):
		return self.__name

	@classmethod
	def make_unarmed(cls):
		return cls("Unarmed",cls.UNARMED_POWER,1)




	


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name, max_hp, attack, defense, level) -> None:
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None
		self.hp = max_hp

	@property
	def name(self):
		return self.__name

	def compute_damage():
		pass

def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	pass


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	pass
