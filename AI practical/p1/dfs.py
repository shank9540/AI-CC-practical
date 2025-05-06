graph={
    'A' : ["B" , 'C' , 'D'],
    'B' : ['E'] ,
    'C' : ['D' , 'E'],
    'D' : [ ],
    'E' : [ ]
}
print (graph)

visited=set ( )

def dfs (visited , graph ,root):
    if root not in visited :
        print (root)
        visited . add (root)
        for negihbour in graph [root] :
            dfs (visited , graph , negihbour)

dfs (visited , graph , "A")            