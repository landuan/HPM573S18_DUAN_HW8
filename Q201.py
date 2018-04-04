import Q2 as Cls
import scr.FigureSupport as figureLibrary

# create a multiple game sets
multipleGameSets=Cls.MultipleGameSets(ids=range(1000), prob_head=0.45, n_games_in_a_set=10)
# simulate all game sets
multipleGameSets.simulation()

# print projected mean reward
print('Projected mean reward',
      multipleGameSets.get_mean_total_reward())
# print projection interval
print('95% projection interval of average rewards',
      multipleGameSets.get_PI_total_reward(0.05))

