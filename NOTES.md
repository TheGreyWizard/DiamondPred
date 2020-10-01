# Features

0.  id - row id
1.  price - in USD
2.  carat - weight of diamond
3.  cut - quality of the cut
4.  color - diamond color
5.  clarity - a measurement of how clear the diamond is
6.  x - length
7.  y - width
8.  z - depth
9.  depth - total depth percentage
10. table - width of top of diamond relative to widest point

## Numeric Features (min - max)

1.  price - in USD ($326 - $18,823)
2.  carat - weight of diamond (0.2 - 5.01)
3.  x - length in mm (0 - 10.78)
4.  y - width in mm (0 - 58.90)
5.  z - depth in mm (0 - 31.80)
6.  depth - total depth percentage = z/ mean(x, y)
7.  table - width of top of diamond relative to widest point

## Categorical Features ranked worst to best (class_1,...class_n)

1.  cut - quality of the cut - 5 categories
    (Fair, Good, Very Good, Premium , Ideal)
2.  color - diamond color - 7 categories
    (J, I, H, G, F, E, D)
3.  clarity - a measurement of how clear the diamond is - 5 categories
    (I1, SI2 , SI1, VS2, VS1, VVS2 , VVS1 , IF)
