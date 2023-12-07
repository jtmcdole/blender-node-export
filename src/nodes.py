import bpy
import xml.etree.ElementTree as ET

class UI:

    def svg(self):
        return ET.Element('g')

class UINode(UI):
    
    node : bpy.types.Node

    def __init__(self, node):
        self.node = node
    def svg(self):
        group = ET.Element('g')
        ...

class UISocket(UI):
    
    socket : bpy.types.NodeSocket

    def __init__(self, socket):
        self.socket = socket

    def svg(self):
        group = ET.Element('g')
        # p272
        label = ET.Element('text')
        label.text = self.socket.name
        group.append(label)
        return group