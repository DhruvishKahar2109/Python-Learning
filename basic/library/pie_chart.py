#pie chart

y = np.array([35,25,25,15])
mylabels = ["Apples","Bananas","Cherries","Dates"]

plt.pie(y, labels = mylabels,shadow = True)
plt.legend(title="Four Fruits:")
plt.show()