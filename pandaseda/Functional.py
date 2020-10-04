import seaborn as sns
import pandas as pd
from IPython.core.display import HTML



def correlation_heat_map(df, figsize = (10,10)):
    ax = sns.heatmap(df.corr(), vmin = -1, vmax = 1)
    labels = [t.get_text() for t in ax.get_xticklabels()]
    ax.set_xticklabels(labels, rotation=30, horizontalalignment="right")
    sns.set(rc={'figure.figsize':figsize}, font_scale=1.4)



def desc(df, print_sorted = False):
    import seaborn as sns
    cm = sns.light_palette("gray", as_cmap=True)
    if print_sorted:
    	display(HTML('<h4><B><span style="padding-left: 30%";>' + f"shape {df.shape}" + "</span></h4>"))    
    desc = pd.DataFrame(
            {
                'dtypes' : df.dtypes,
                'nunique': df.nunique(),
                "nans": df.isna().sum()
            }
        ).reset_index(level=0).merge(df.describe().T.reset_index(level=0), how = 'left').sort_values('nunique')
    style1 = desc.style.background_gradient(cmap=cm, subset=['nunique'])
    style2 = desc.style.set_properties(**{'font-weight': 'bold'}, subset = ['index'])
    style2.use(style1.export())
    if print_sorted:
    	display(style2)
    return desc

def get_pearson(df, target, thresh = 0.5):
    correlation = df.corrwith(df[target]).sort_values()
    correlation = correlation[(correlation<-thresh).values | (correlation>thresh).values]
    correlation = correlation.loc[correlation.index != target]
    correlation = correlation.reset_index().rename({'index':'variable', 0:'pearson score'}, axis = 1)
    return correlation

