class Nemo_Intent:

    sentences = []
    objects = []

class Nemo_objects:

    nodes = []
    flows = []
    operations = []

class Nemo_Node:

    node_type = []
    sub_nodes = []

def parse_Intent(intent_file):
    Intent = Nemo_Intent()

    #Read intent file
    f = open(intent_file, 'r')
    intent_text = f.read()

    #Get sentences
    sentences = intent_text.split('\n')
    while '' in sentences:
        sentences.remove('')
    Intent.sentences = sentences

    return Intent
