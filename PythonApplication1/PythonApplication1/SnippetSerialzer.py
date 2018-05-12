#!/usr/bin/python 
# coding=utf-8

from xml.dom.minidom import parse as xmlParse
from xml.dom.minidom import Document as xmlDocument
import xml.dom.minidom
import sys
import os

class DOMParserUtil(object):

    #通过 查找第一个元素
    @staticmethod
    def findFirstElementByTagName(InElement,InTagName):
        return InElement.getElementsByTagName(InTagName)[0]

    #通过 获取第一个元素的内容
    @staticmethod
    def getFirstElementContentByTagName(InElement,InTagName):
        #return str(InElement.getElementsByTagName(InTagName)[0].childNodes[0].data)
        return InElement.getElementsByTagName(InTagName)[0].childNodes[0].data

    #通过 查找所有元素
    @staticmethod
    def findElementsByTagName(InElement,InTagName):
        return InElement.getElementsByTagName(InTagName)

    #通过 获取元素内容
    @staticmethod
    def getElementContent(InElement):
        return InElement.childNodes[0].data

    #通过 获取元素属性值
    @staticmethod
    def getElementAttrib(InElement,inAttribName):
        return InElement.getAttribute(inAttribName)

    #通过 设置元素属性值
    @staticmethod
    def setElementAttrib(InElement,inAttribName,inAtrribValue):
        return InElement.setAttribute(inAttribName,inAtrribValue)

    #创建xml文档元素
    @staticmethod
    def createElement(xmlDoc,inTagName,ParentElem = None):
        NewElem = xmlDoc.createElement(inTagName)
        DOMParserUtil.appendChild(ParentElem,NewElem)
        return NewElem

    #挂接子节点到父节点身上
    @staticmethod
    def appendChild(xmlElemParent,xmlElemChild):
        if xmlElemParent:
            xmlElemParent.appendChild(xmlElemChild)

    #创建xml文本节点
    @staticmethod
    def createTextNode(xmlDoc,inText,ParentElem = None):
        txtNode = xmlDoc.createTextNode(inText)
        DOMParserUtil.appendChild(ParentElem,txtNode)
        return txtNode

    #创建xml文本节点
    @staticmethod
    def createCDATASection(xmlDoc,inText,ParentElem = None):
        newCDATA = xmlDoc.createCDATASection(inText)
        DOMParserUtil.appendChild(ParentElem,newCDATA)

    #创建xml文本标签<TagName>Content</TagName>
    @staticmethod
    def createTagNode(xmlDoc,inTagName,inText,ParentElem = None):
        tagNode = DOMParserUtil.createElement(xmlDoc,inTagName,ParentElem)
        DOMParserUtil.createTextNode(xmlDoc,inText,tagNode)
        return tagNode



class SnippetHeader(object):
    """
        代码片段头 
    """
    def __init__(self):
        #标题
        self.title = ""
        #作者
        self.author = ""
        #描述
        self.desc = ""
        #帮助URL
        self.helpUrl = ""
        #快捷键
        self.shortcut = ""
        #snippet types
        self.SnippetTypes = []
    def parse(self,xmlElement):

        for snippetType_node in DOMParserUtil.findElementsByTagName(xmlElement,"SnippetType"):
            self.SnippetTypes.append( DOMParserUtil.getElementContent(snippetType_node))

        self.title = DOMParserUtil.getFirstElementContentByTagName(xmlElement,"Title")
        self.author = DOMParserUtil.getFirstElementContentByTagName(xmlElement,"Author")
        self.desc = DOMParserUtil.getFirstElementContentByTagName(xmlElement,"Description")
        self.helpUrl = DOMParserUtil.getFirstElementContentByTagName(xmlElement,"HelpUrl")
        self.shortcut = DOMParserUtil.getFirstElementContentByTagName(xmlElement,"Shortcut")

    def write(self,xmlDoc,xmdElement):
        SnippetTypesNode = DOMParserUtil.createElement(xmlDoc,"SnippetTypes",xmdElement)
        for SnippetType in self.SnippetTypes:
            DOMParserUtil.createTagNode(xmlDoc,"SnippetType",SnippetType,SnippetTypesNode)

        DOMParserUtil.createTagNode(xmlDoc,"Title",self.title,xmdElement)
        DOMParserUtil.createTagNode(xmlDoc,"Author",self.author,xmdElement)
        DOMParserUtil.createTagNode(xmlDoc,"Decription",self.desc,xmdElement)
        DOMParserUtil.createTagNode(xmlDoc,"HelpUrl",self.helpUrl,xmdElement)
        DOMParserUtil.createTagNode(xmlDoc,"Shortcut",self.shortcut,xmdElement)


class SnippetBodyLiteral(object):
    """
        代码片段主体 替换声明
    """
    def __init__(self):
        #snippet 声明id
        self.id = ""
        #snippet 提示信息
        self.toolTips = ""
        #snippet 默认值
        self.defaultValue = ""
    def parse(self,xmlElement):
        self.id = DOMParserUtil.getFirstElementContentByTagName(xmlElement,"ID")
        self.toolTips = DOMParserUtil.getFirstElementContentByTagName(xmlElement,"ToolTip")
        self.defaultValue = DOMParserUtil.getFirstElementContentByTagName(xmlElement,"Default")
        
    def write(self,xmlDoc,xmdElement):
        DOMParserUtil.createTagNode(xmlDoc,"ID",self.id,xmdElement)
        DOMParserUtil.createTagNode(xmlDoc,"ToolTip",self.toolTips,xmdElement)
        DOMParserUtil.createTagNode(xmlDoc,"Default",self.defaultValue,xmdElement)


class SnippetBodyReplacement(object):
    """
        替代物对象，只有一个声明ID
    """
    def __init__(self):
        self.declarationId=""

class SnippetBodyCode(object):
    """
        Snippet Code
    """
    def __init__(self):
        self.language = "python"
        self.delimiter = "$"
        self.replacements =[]
    def parse(self,xmlElement):
        self.text = DOMParserUtil.getElementContent(xmlElement)
        self.language = DOMParserUtil.getElementAttrib(xmlElement,"Language")
        self.delimiter = DOMParserUtil.getElementAttrib(xmlElement,"Delimiter")


    def write(self,xmlDoc,xmdElement):
        DOMParserUtil.createCDATASection(xmlDoc,self.text,xmdElement)
        DOMParserUtil.setElementAttrib(xmdElement,"Language",self.language)
        DOMParserUtil.setElementAttrib(xmdElement,"Delimiter",self.delimiter)


class SnippetBody(object):
    def __init__(self):
        #代码片段 引用的 替代声明 key:id value:替代声明
        self.Literials = {}
        self.code = SnippetBodyCode()
    def parse(self,xmlElement):

        # 解析Literal
        for declaration_node in DOMParserUtil.findElementsByTagName(xmlElement,"Literal"):
            literal = SnippetBodyLiteral()
            literal.parse(declaration_node)
            self.Literials[literal.id] = literal

        code_node = DOMParserUtil.findFirstElementByTagName(xmlElement,"Code")
        self.code.parse(code_node)

    def write(self,xmlDoc,xmdElement):
        #创建literal节点
        DOMParserUtil.createElement(xmlDoc,"Literal",xmdElement)
        for literal in self.Literials.values():
            literal.write(xmlDoc,DOMParserUtil.createElement(xmlDoc,"Literal",xmdElement))

        self.code.write(xmlDoc,DOMParserUtil.createElement(xmlDoc,"Code",xmdElement))

class Snippet(object):
    def __init__(self):
        self.header = SnippetHeader()
        self.body = SnippetBody()
    def parse(self,xmdElement):
        self.header.parse(DOMParserUtil.findFirstElementByTagName(xmdElement,"Header"))
        self.body.parse(DOMParserUtil.findFirstElementByTagName(xmdElement,"Snippet"))

    #更新代码片段到XML
    def write(self,xmlDoc,xmdElement):
        headerXml = DOMParserUtil.createElement(xmlDoc,"Header",xmdElement)
        self.header.write(xmlDoc,headerXml)
        bodyXml = DOMParserUtil.createElement(xmlDoc,"Snippet",xmdElement)
        self.body.write(xmlDoc,bodyXml)
        pass

class SnippetSerialzer(object):

    @staticmethod
    def readXml(fileName):
        print("readXml",fileName)
        #获取DOM树 对象
        DOMTree = xml.dom.minidom.parse(fileName)
        #获取 节点集合 当前为 CodeSnippets 节点

        Snippets = []
        for snippet_node in DOMParserUtil.findElementsByTagName(DOMTree.documentElement,"CodeSnippet"):
            # create snippet object
            snippet = Snippet()
            snippet.parse(snippet_node)
            Snippets.append(snippet)

        return Snippets

    @staticmethod
    def writeXml(fileName,InSnippets):
        #新建XML文档对象
        xmlDoc = xmlDocument()

        #创建根节点
        root = DOMParserUtil.createElement(xmlDoc ,"CodeSnippets")

        DOMParserUtil.appendChild( xmlDoc , root)

        #更新根节点属性 xmlns="http://schemas.microsoft.com/VisualStudio/2005/CodeSnippet"
        DOMParserUtil.setElementAttrib(root,"xmlns","http://schemas.microsoft.com/VisualStudio/2005/CodeSnippet")

        #将所有snippet 数据写入到xml文档对象中
        for snippet in InSnippets:
            snippet.write(xmlDoc,root)

        #打印文档内容
        print(xmlDoc.toprettyxml(encoding='utf-8').decode("utf-8").encode("gbk"))

        # 保存xml文档
        with open(fileName,"w+") as f:
            f.write(xmdDoc.toprettyxml( encoding= "utf-8"))
        pass









def main():
    folder = "C:/Users/myzn/source/PythonEx/vs Snippets/python"
    Snippets = []
    for file in os.listdir(folder):
        if file.endswith(".snippet"):
            Snippets.extend( SnippetSerialzer.readXml( os.path.join(folder , file)) )

    SnippetSerialzer.writeXml("C:/Users/myzn/source/test.snippet",Snippets)
    pass

if __name__ == "__main__":
    main()
