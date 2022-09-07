import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from PyQt5.QtCore import Qt



class TreadmillTask_barchart(QtGui.QWidget): #class for the widget containing the barchart
    
    def __init__(self, parent=None):
        super(QtGui.QWidget,self).__init__(parent)
        self.pause_button = QtGui.QPushButton('Pause barchart')
        self.pause_button.setEnabled(False)
        self.pause_button.setCheckable(True)

        self.performance_barchart=Performance_barchart(self)

        self.vertical_layout=QtGui.QGridLayout()
        self.vertical_layout.addWidget(self.performance_barchart.axis,0,0,1,1)
        self.vertical_layout.addWidget(self.pause_button,1,0,1,1,Qt.AlignCenter)
        self.setLayout(self.vertical_layout)

    def run_start(self):
        self.pause_button.setChecked(False)
        self.pause_button.setEnabled(True)
        self.performance_barchart.run_start()

    def run_stop(self):
        self.pause_button.setEnabled(False)

    def set_state_machine(self,sm_info):
        self.performance_barchart.set_state_machine(sm_info)
        
        
    def process_data(self, new_data):
        self.performance_barchart.process_data(new_data)

    def update(self):
        if not self.pause_button.isChecked():
            self.performance_barchart.update()

class Performance_barchart():

    def __init__ (self,parent=None):
        self.axis=pg.PlotWidget()
        self.axis.setTitle('Performance: rewards vs penalties (per session)')
        self.bars=pg.BarGraphItem(x=[1,2], height=[0,0], width=0.5, brushes=[(0,150,255),(255,0,0)])
        self.axis.addItem(self.bars)
        self.axis.setYRange(0,10)

    def run_start(self):
        self.axis.clear()
        self.axis.setYRange(0,10)
        self.axis.getAxis('bottom').setTicks([[(1,'Rewards'),(2,'Penalties')]])

        self.motion_number=0  #replace next 2 lines by the 4 lines commented below for the treadmill task
        self.motion_number_last=0
        #self.reward_number=0
        #self.penalty_number=0
        #self.reward_number_last=0
        #self.penalty_number_last=0

    def set_state_machine(self, sm_info):
        self.event_IDs = list(sm_info['events'].values()) #to replace these 2 lines by the 3 lines commented below for the treadmill task
        self.motion_ID=sm_info['events']['motion']

        #self.state_IDs=list(sm_info['states'].values())
        #self.penalty_ID=sm_info['states']['penalty']
        #self.reward_ID=sm_info['states']['reward']

    def process_data(self,new_data):
        new_events = [nd for nd in new_data if nd[0] == 'D' and nd[2] in self.event_IDs]  #see process_data and update methods for the treadmill task commented below
        if new_events:
            for ns in new_events:
                if ns[2]==self.motion_ID:
                    self.motion_number+=1

    def update(self):
        if self.motion_number!=self.motion_number_last:
            if self.motion_number+1>10:
                self.axis.enableAutoRange()
            self.axis.removeItem(self.bars)
            self.bars=pg.BarGraphItem(x=[1,2], height=[self.motion_number, self.motion_number+1], width=0.5, brushes=[(0,255,0),(255,0,0)])
            self.axis.addItem(self.bars)
            self.axis.getAxis('bottom').setTicks([[(1,'Rewards: {}'.format(self.motion_number)),(2,'Penalties: {}'.format(self.motion_number+1))]])
            self.motion_number_last=self.motion_number



    #def process_data(self,new_data):
        #new_states=[ns for ns in new_data if ns[0]=='D' and ns[2] in self.state_IDs] 
        #if new_states:
            #for ns in new_states:
                #if ns[2]==self.reward_ID:
                    #self.reward_number+=1
                #elif ns[2]==self.penalty_ID:
                    #self.penalty_number+=1

    #def update(self):
        #if self.reward_number!=self.reward_number_last or self.penalty_number!=self.penalty_number_last:
            #if self.reward_number>10 or self.penalty_number>10:
                #self.axis.enableAutoRange()
            #self.axis.removeItem(self.bars)
            #self.bars=pg.BarGraphItem(x=[1,2], height=[self.reward_number, self.penalty_number], width=0.5, brushes=[(0,255,0),(255,0,0)])
            #self.axis.addItem(self.bars)
            #self.axis.getAxis('bottom').setTicks([[(1,'Rewards: {}'.format(self.reward_number)),(2,'Penalties: {}'.format(self.penalty_number))]])
            #self.reward_number_last=self.reward_number
            #self.penalty_number_last=self.penalty_number


                    




 
