from base import *


# Add N Obs inside boxplot (optional)
def add_n_obs(df,group_col,y):
  medians_dict = {grp[0]:grp[1][y].median() for grp in df.groupby(group_col)}
  xticklabels = [x.get_text() for x in plt.gca().get_xticklabels()]
  n_obs = df.groupby(group_col)[y].size().values

  for (x, xticklabel), n_ob in zip(enumerate(xticklabels), n_obs):
    plt.text(x, medians_dict[float(xticklabel)]*1.01, "#images: "+str(n_ob), horizontalalignment='center', fontdict={'size':14}, color='black')


def plot_just_daily_boxplot(df, column, label, title, palette):
  sns.set_style("dark")
  sns.set_context("paper", font_scale=3) 
  plt.figure(figsize=(11,7), dpi= 80)
  ax = sns.boxplot(x='amount', y=column, data=df, notch=False, palette=palette)

  # add_n_obs(df,group_col='amount',y=column)    
  ax.set(xlabel='Category', ylabel=label)
  plt.xticks([0,1,2,3,4],['none','some','a lot','substantial','extensive'])
  plt.yticks()
  plt.tight_layout()
  # plt.title(title, fontsize=22)

