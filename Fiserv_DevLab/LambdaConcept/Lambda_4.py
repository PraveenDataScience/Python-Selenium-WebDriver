def writer():
    title='Sir'
    name=lambda x:title+' '+x
    return name

who=writer()
print(who('VDS TECH'))