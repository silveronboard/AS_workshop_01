IDs = []

APIs = ['API0', 'API1', 'API2']

for i in range (0,500):
    IDs.append("ID_" + str(i))

for k in range(0,500):
    apindex = int ( int( k % 300 ) / 100 )
    print( IDs[k], APIs[apindex])


