from lib import Message, DataBase, Gatherer, FrontEnd, Listener
# Aquí va la logica de fucnionamiento del condigo y la ejecucion normal del mismo

def hookDefinition(dataBase, frontEnd):
    assert isinstance(dataBase, DataBase)
    assert isinstance(frontEnd, FrontEnd)

    def hook(message):
        msg = Message(message)
        dataBase.push(msg)
        frontEnd.update(msg)

    return hook

vcan0 = Gatherer("vcan0", 1000000)
#can1 = Gatherer("can1", 500000)
db0 = DataBase("can0.csv")
# db1 = DataBase("can1.csv")
front = FrontEnd()

hook0 = hookDefinition(db0, front)
vcan0.setHook(hook0)
#hook1 = hookDefinition(db1, front)
#can1.setHook(hook1)
while True:
    pass
