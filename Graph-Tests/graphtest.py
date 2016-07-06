import kivy
#kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.garden.graph import Graph, MeshLinePlot
from math import sin
  

class GraphWidget(BoxLayout):
    def __init__(self):
	#create the graph widget?
        super(GraphWidget, self).__init__()
	#identify where you want the graph to go
        self.graph = self.ids.graph_plot
  
	self.plot = MeshLinePlot(color=[1, 0, 0, 1])
	self.plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
	self.graph.add_plot(self.plot)

        #self.plot = [1,1,1,1]
        #self.plot.append(MeshLinePlot(color=[1, 0, 0, 1])) #X - Red
  
        #self.reset_plots()
  
        #for plot in self.plot:
            #self.graph.add_plot(plot)
  
    #def reset_plots(self):
        #for plot in self.plot:
            #plot.points = [(0,0)]



class GraphTest(App):

    def build(self):
        return GraphWidget()


if __name__ == '__main__':
    GraphTest().run()
