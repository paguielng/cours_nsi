def test1(processus) :
    assert processus[0] == {'name':'P1','duree':7,'arrivee':3,'reste':7}
    print('P1 ok')
    assert processus[1] == {'name':'P2','duree':8,'arrivee':2,'reste':8}
    print('P2 ok')
    assert processus[2] == {'name':'P3','duree':14,'arrivee':0,'reste':14}
    print('P3 ok')
    assert processus[3] == {'name':'P4','duree':5,'arrivee':8,'reste':5}
    print('P4 ok')


def test_enfiler(enfiler) :
    P1 = {'name':'P1','duree':7,'arrivee':3,'reste':7}
    P2 = {'name':'P2','duree':8,'arrivee':2,'reste':8}
    P3 = {'name':'P3','duree':14,'arrivee':0,'reste':14}
    P4 = {'name':'P4','duree':5,'arrivee':8,'reste':5}
    processus = [P1,P2,P3,P4]
    print('test avec ',[processus[i]['name']+' duree :'+str(processus[i]['duree'])+" arrivee : "+str(processus[i]['arrivee'])+" " for i in range(len(processus)) ])
    file = []
    enfiler(file,P3)
    print([file[i]['name'] for i in range(len(file) ) ] )
    assert file == [P3]
    print('test 1 ok')
    enfiler(file,P2)
    print([file[i]['name'] for i in range(len(file) ) ] )
    assert file == [P3,P2]
    print('test 2 ok')
    enfiler(file,P4)
    print([file[i]['name'] for i in range(len(file) ) ] )
    assert file == [P3,P4,P2]
    print('test 3 ok')
    enfiler(file,P1)
    print([file[i]['name'] for i in range(len(file) ) ] )
    assert file == [P3,P4,P1,P2]
    print('test 4 ok')


def test2(f) :
    file = []
    P1 = {'name':'P1','duree':7,'arrivee':3}
    P2 = {'name':'P2','duree':8,'arrivee':2}
    P3 = {'name':'P3','duree':14,'arrivee':0}
    P4 = {'name':'P4','duree':5,'arrivee':8}
    processus = [P1,P2,P3,P4]
    f(processus,file,0)
    assert file == [P3]
    print('insertion t=0 ...ok')

    f(processus,file,1)
    assert file == [P3]
    print('insertion t=1 ...ok')

    f(processus,file,2)
    print(file)
    assert file == [P3,P2]
    print('insertion t=2 ...ok')

    f(processus,file,3)
    assert file == [P3,P1,P2]
    print('insertion t=3 ...ok')


def test3(exec_quantum) :
    P1 = {'name':'P1','duree':7,'arrivee':3,'reste':7}
    P2 = {'name':'P2','duree':6,'arrivee':2,'reste':8}
    P3 = {'name':'P3','duree':14,'arrivee':0,'reste':14}
    P4 = {'name':'P4','duree':6,'arrivee':5,'reste':8}

    file = [P1]
    assert exec_quantum(file,3) == 'P1'
    assert P1['reste'] == 6,"la duree  de P1 n'a pas été modifiée correctement"
    print('test 1...ok : le processus élu est correctement renvoyé')
    assert file == [P1]
    print("test 2...ok, la file n'a pas été modifiée")
    print("\ntest avec un processus dont ka duree est égale à 1")
    P2 = {'name':'P2','duree':1,'arrivee':2,'reste':1}
    file = [P2,P3]
    assert exec_quantum(file,0) == 'P2'
    print('test 3...ok : le processus élu est correctement renvoyé')
    assert file == [P3]
    print("test 4...ok, la file a été correctement modifiée")

