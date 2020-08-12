library(DiagrammeR)
mermaid("
        gantt
        dateFormat  YYYY-MM-DD
        title Cronograma de trabajo
        
        section Go ising
        Estancia en ABACUS              :done,          first_1,    2017-06-05, 2018-02-28
        Setup computacional                :crit,active,        first_2,    2017-06-09, 8w
        Simulaciones                 :active,               first_3,    after first_2, 10w
        Análisis de resultados             :active,               first_4,    after first_3, 4w
        Escritura articulo                    : crit, active,           first_5, after first_4, 10w
        
        section Interactoma
        Setup computacional     : crit,active,    import_1,   2017-07-01, 5w
        Simulaciones      : active,    import_2,   after import_1, 4w
        Análisis estadístico :crit, active,  import_3,   after import_2, 10w
        Escritura articulo            :crit, active,        import_4,   after import_3, 10w 
        
        ")

