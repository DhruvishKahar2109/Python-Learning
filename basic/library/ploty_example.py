import plotly.express as px

months = ["Jan","Feb","Mar","Apr","May"]
sales = [100,150,130,180,220]

#line charts
fig = px.line(
    x = months,
    y = sales,
    title = "Monthly Sales",
)

# fig.show()

#bar charts

users = ["Dhruvish","Raj","Rohan","Amit","Jay"]
marks = [85,72,90,78,45]

fig2 = px.bar(
    x = users,
    y = marks,
    title = "Students Marks",
    labels = {
        "x":"Students",
        "y":"Marks"
    }
)

# fig2.show()

languages = ["python","ruby","java","PHP"]
students = [40,25,20,15]
fig3 = px.pie(
    names = languages,
    values = students,
    title = "Programming Languages",
)

fig3.show()