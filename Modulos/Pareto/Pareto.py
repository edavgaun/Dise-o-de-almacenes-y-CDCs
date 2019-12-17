def pareto_plot(df, x=None, y=None, titulo=None, decimal_acum_y=2, sindecimal=True):
    import pandas as pd
    import seaborn as sns

    import matplotlib.pyplot as plt
    %matplotlib inline
    '''
    La siguiente función sirve para crear un Pareto a partir de cualquier DataFrame creado en Pandas
    Es necesario seleccionar la columna x (Cualitativa) y la columna y (Cuantitativa)
    '''
    xlabel = x
    ylabel = y
    tmp= pd.DataFrame({xlabel:df[x].values, ylabel:df[y].values})
    tmp = tmp.sort_values(ylabel, ascending=False)
    x = tmp[x].values
    y = tmp[y].values
    ponderado = y / y.sum()
    suma_acum = ponderado.cumsum()
    
    # https://pyformat.info/
    if sindecimal==True:
        sin_decimales="{0:,.0%}"
    else:
        sin_decimales="{0:,.2%}"
    
    
    dos_decimales="{0:,." + str(decimal_acum_y) + "%}"

    fig, ax1 = plt.subplots()
    
    fig.set_figwidth(12)
    
    ax1.bar(x, y)
    ax1.set_xlabel(xlabel)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
    ax1.set_ylabel(ylabel)

    # Creamos una gráfica en el eje y opuesta a la original mediante el método twinx
    ax2 = ax1.twinx()

    # "-ro": el doble guión medio indica que será una línea segmentada, la g es el color verde, 
    #        y la o indica marcadores con forma de puntos
    # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
    ax2.plot(x, suma_acum, "--go", alpha=0.5)
    ax2.set_ylabel("% acumulado", color='g')
    ax2.tick_params("y", colors='g')

    vals = ax2.get_yticks()
    ax2.set_yticklabels([dos_decimales.format(i) for i in vals])


    # Las siguientes instrucciones sirven para colocar las anotaciones de porcentaje en la 
    # línea de valores acumulados.
    ponderaciones_pct = [sin_decimales.format(i) for i in suma_acum]
    for j, txt in enumerate(ponderaciones_pct):
        ax2.annotate(txt, (x[j], suma_acum[j]), fontweight='heavy')    


    plt.title(titulo)
    # Código para determinar los puntos donde colocar las líneas verticales que dividan
    # las secciones A, B, y C
    
    punto1=0
    punto2=0
    for k1,valor1 in enumerate(suma_acum,0):
        if valor1>=0.79:
            punto1=k1
            for k2,valor2 in enumerate(suma_acum,0):
                if valor2>=0.89:
                    punto2=k2
                    break
            break
    plt.axvline(x=x[punto1],color='red', linestyle='--')
    plt.axvline(x=x[punto2],color='red', linestyle='--')
    
    plt.text(round(punto1/2,0), 0.95, "A", size=16, color='r')
    plt.text(punto1+0.5, 0.95, "B", size=16, color='r')
    plt.text(punto2+0.5, 0.95, "C", size=16, color='r')
    plt.tight_layout()
    
    tmp["ponderado"]=ponderado
    tmp[" % acumulado"]=ponderaciones_pct
    print("\nTabla Pareto\n")
    print(tmp.head(10))
    print()
    plt.show()
