def both_paths(sofar = "S"):
    print(sofar)
    def up():
        return both_paths(sofar + 'U')
    
    def down():
        return both_paths(sofar + 'D')

    return up, down
