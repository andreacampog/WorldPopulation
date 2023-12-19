
import matplotlib.pyplot as plt  #importamos una parte especial de la libreria matplotlib y le pongo un alias plt

def generate_bar_chart(labels,values):  
    fig,ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()

def generate_pie_chart(labels,values):
    fig,ax =plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal') #forma de circulo
    plt.show()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]  
    
    generate_bar_chart(labels,values)
    #generate_pie_chart(labels,values)


    





