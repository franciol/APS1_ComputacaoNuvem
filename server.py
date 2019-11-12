from flask import Flask, escape, request, jsonify
import json


class Tarefas():

    def __init__(self, id_self, quando, atividade):
        self.quando = quando
        self.atividade = atividade
        self.id = id_self

    def dicttify(self):
        return {
            "id": self.id,
            "quando": self.quando,
            "atividade": self.atividade
        }


app = Flask(__name__)


dict_main = {}


@app.route('/Tarefa/', methods=['GET'])
def get_tarefas():
    lista0 = {}
    for o in dict_main:
        a = dict_main[o].dicttify()
        lista0[o] = a
    print(lista0)
    return lista0


@app.route('/Tarefa/', methods=['POST'])
def post_tarefas():
    data = request.form.to_dict(flat=False)
    if(len(dict_main) > 0):
        id_atual = max(dict_main.keys())+1
    else:
        id_atual = 0
    taref = Tarefas(id_atual, data['quando'], data['atividade'])
    dict_main[id_atual] = taref
    return "O id da atividade foi adicionado em %d" % (id_atual)


@app.route('/Tarefa/<int:id>', methods=['GET'])
def lista_especiifca(id):
    lista0 = {}
    a = dict_main[id].dicttify()
    return a


@app.route('/Tarefa/<int:id>', methods=['DELETE'])
def apaga_especiifca(id):
    del dict_main[id]
    return "Item de Id %d não existe mais" % (id)


@app.route('/Tarefa/<int:id>', methods=['PUT'])
def altera_especiifca(id):
    data = request.form.to_dict(flat=False)

    taref = Tarefas(id, data['quando'], data['atividade'])
    dict_main[id] = taref
    return "A atividade de ID %d  foi alterada" % (id)


@app.route('/healthcheck/', methods=['GET'])
def helath():
    return ""


if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=5000,debug=False)
