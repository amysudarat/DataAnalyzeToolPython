import matplotlib.pyplot as plt
import pandas as pd
# plt.style.use('Solarize_Light2')
# plt.style.use('ggplot')

def plotCircumplex(IAPS_df,amp,indexs):
    
    ''' Plot the data '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(IAPS_df['Val_mn'],IAPS_df['Arou_mn'],s=amp*IAPS_df['Val_sd'],alpha=0.5,c='gold')
    # bx = fig.add_subplot(122)
    # bx.scatter(IAPS_df['Val_mn'],IAPS_df['Arou_mn'],s=amp*IAPS_df['Arou_sd'],alpha=0.5,c='gold')
    for index in indexs:    
        ax.annotate(IAPS_df['Description'][index],
                            xy=(IAPS_df['Val_mn'][index],IAPS_df['Arou_mn'][index]),xycoords='data',
                            xytext=(IAPS_df['Val_mn'][index],IAPS_df['Arou_mn'][index]), textcoords='data',
                            arrowprops=dict(facecolor='black',shrink=0.05))
        ax.annotate(IAPS_df['IAPS'][index],
                            xy=(IAPS_df['Val_mn'][index],IAPS_df['Arou_mn'][index]),xycoords='data',
                            xytext=(IAPS_df['Val_mn'][index],IAPS_df['Arou_mn'][index]+0.01), textcoords='data')
                            # arrowprops=dict(facecolor='black',shrink=0.05))
        # bx.annotate(IAPS_df['Description'][index],
        #                     xy=(IAPS_df['Val_mn'][index],IAPS_df['Arou_mn'][index]),xycoords='data',
        #                     xytext=(IAPS_df['Val_mn'][index],IAPS_df['Arou_mn'][index]), textcoords='data',
        #                     arrowprops=dict(facecolor='black',shrink=0.05))

    ''' Check with axis configuration here:
    https://stackoverflow.com/questions/31556446/drawing-axis-in-the-middle-of-the-figue-in-python
    https://matplotlib.org/examples/pylab_examples/spine_placement_demo.html'''

    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    # ax.spines['left'].set_smart_bounds(True)
    # ax.spines['bottom'].set_smart_bounds(True)

    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_title("Circumplex Model of affect (SD valence)")
    ax.set_xlabel("Valence")
    ax.set_ylabel("Arousal")

    # Set aspect ratio
    ax.set_aspect('equal', 'datalim')

    # Show plot
    plt.show()

'''
    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    bx.spines['left'].set_position('center')
    bx.spines['bottom'].set_position('center')
    # ax.spines['left'].set_smart_bounds(True)
    # ax.spines['bottom'].set_smart_bounds(True)

    # Eliminate upper and right axes
    bx.spines['right'].set_color('none')
    bx.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    bx.xaxis.set_ticks_position('bottom')
    bx.yaxis.set_ticks_position('left')
    bx.set_title("Circumplex (SD arousal)")
    bx.set_xlabel("Valence")
    bx.set_ylabel("Arousal")'''

    # plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    # plt.tight_layout()

def plotCircumplex_byImageFileName(IAPS_df,amp,indexs):
    ''' Plot the data '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(IAPS_df['Val_mn'],IAPS_df['Arou_mn'],s=amp*IAPS_df['Val_sd'],alpha=0.5,c='gold')
    # bx = fig.add_subplot(122)
    # bx.scatter(IAPS_df['Val_mn'],IAPS_df['Arou_mn'],s=amp*IAPS_df['Arou_sd'],alpha=0.5,c='gold')
    for idx in indexs:  
        index = IAPS_df.index[IAPS_df['IAPS'] == idx][0]
        # index = index[0]
        ax.annotate(IAPS_df['Description'][index],
                            xy=(IAPS_df['Val_mn'][index],IAPS_df['Arou_mn'][index]),xycoords='data',
                            xytext=(IAPS_df['Val_mn'][index],IAPS_df['Arou_mn'][index]), textcoords='data',
                            arrowprops=dict(facecolor='black',shrink=0.05))
        # ax.annotate(IAPS_df['IAPS'][index],
        #                     xy=(IAPS_df['Val_mn'][index],IAPS_df['Arou_mn'][index]),xycoords='data',
        #                     xytext=(IAPS_df['Val_mn'][index],IAPS_df['Arou_mn'][index]+0.01), textcoords='data')
                            # arrowprops=dict(facecolor='black',shrink=0.05))
        # bx.annotate(IAPS_df['Description'][index],
        #                     xy=(IAPS_df['Val_mn'][index],IAPS_df['Arou_mn'][index]),xycoords='data',
        #                     xytext=(IAPS_df['Val_mn'][index],IAPS_df['Arou_mn'][index]), textcoords='data',
        #                     arrowprops=dict(facecolor='black',shrink=0.05))

    ''' Check with axis configuration here:
    https://stackoverflow.com/questions/31556446/drawing-axis-in-the-middle-of-the-figue-in-python
    https://matplotlib.org/examples/pylab_examples/spine_placement_demo.html'''

    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    # ax.spines['left'].set_smart_bounds(True)
    # ax.spines['bottom'].set_smart_bounds(True)

    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_title("Moderate set")
    ax.set_xlabel("Valence")
    ax.set_ylabel("Arousal")

    # Set aspect ratio
    ax.set_aspect('equal', 'datalim')

    # Show plot
    plt.show()
