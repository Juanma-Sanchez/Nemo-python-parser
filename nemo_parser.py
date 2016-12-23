class Nemo_Intent:

    sentences = []
    objects = []
    operations = []

    def __init__(self):
        self.objects = Nemo_objects()

class Nemo_objects:

    nodes = []
    flows = []
    connections = []

    def append_Node(self, name, node_type, subnodes=None, properties=None):
        self.nodes.append(Nemo_Node(name, node_type, subnodes, properties))

class Nemo_Node:

    name = None
    node_type = None
    sub_nodes = []
    properties = []

    def __init__(self, name, node_type, subnodes=None, properties=None):
        self.name = name
        self.node_type = node_type
        if subnodes:
            self.sub_nodes = subnodes
        if properties:
            self.properties = properties
    def __str__(self):
        string = "name: " + self.name + '\n' + "type: " + self.node_type
        return string

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

    #Get network nodes
    for sentence in Intent.sentences:
        sentence = sentence.replace(',','')
        sentence = sentence.replace(';','')
        words = sentence.split(' ')
        #print words
        if words[0] == 'CREATE' or words[0] == 'IMPORT':
            if words[1] == 'Node':
                name = words [2]
                node_type = words[4]
                if len(words) > 5:
                    if words[5] == 'Property':
                        print "property"
                Intent.objects.append_Node(name, node_type)       

    return Intent
