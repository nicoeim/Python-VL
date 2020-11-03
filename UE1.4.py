# numbers = []
# a = [0, 1, 2, 3]
# b = [4, 5, 6]
#
# for i in range(10):
#     numbers.append(i)
#
# print(numbers)
#
# # ------------------------------------------------
#
# x = [2, 4, 1, 7, 6, 10, 9, 5, 3, 8]
# x_sort = []
# temp= int
# for n in range(len(x)):
#     for i in range(len(x)-1):
#         if x[i] > x[i + 1]:
#             temp=x[i+1]
#             x[i + 1] = x[i]
#             x[i] = temp
#
# print(x)

#--------------------------------------------------
4.3
MyText="Python ist eine universelle, üblicherweise interpretierte höhere Program-miersprache. Sie hat den Anspruch, " \
       "einen gut lesbaren, knappen Programmierstil zu för-dern. So werden beispielsweise Blöcke nicht durch " \
       "geschweifte Klammern, sondern durch Einrückungen strukturiert. Wegen seiner klaren und übersichtlichen Syntax " \
       "gilt Python als einfach zu erlernen. Python unterstützt mehrere Programmierparadigmen, " \
       "z.B. die objektorientierte, die aspektorientierte und die funktionale Programmierung. Ferner bietet es eine " \
       "dynamische Typisierung. Wie viele dynamische Sprachen wird Py-thon oft als Skriptsprache genutzt. Die Sprache " \
       "weist ein offenes, gemeinschaftsbasier-tes Entwicklungsmodell auf, das durch die gemeinnützige Python " \
       "Software Foundation gestützt wird, die de facto die Definition der Sprache in der Referenzumsetzung CPython " \
       "pflegt. "


print('nach Stichwort suchen')
stichwort=input()
l=len(stichwort)
a=MyText.count(stichwort)
print('kommt %d mal vor'  %a)
position=0
index=0
if a>0:
    for i in range(a):
        index=MyText.find(stichwort)
        position+=index
        print(position)
        MyText=MyText[index+l:]


else:
    print('Stichwort kommt nicht in Text vor')
    # print('Textlänge:', len(MyText))
    # print('Tritt zuerst bei Index %d auf:' % MyText.find(stichwort))
    # print('Kommt im Text %s mal vor' % MyText.count(stichwort))


# b=MyText[1]
# c=b+'d'
# e=MyText[0:8]
# print(b)
# print(c)
# print(e)