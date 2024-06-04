#!/usr/bin/python3
"""This is the task_03_xml
Module
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """A func to Serializa dict to XML format
    """

    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """A func to Deserialize XML data to pytho dict
    """

    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary